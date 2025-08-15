import base64
import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Tuple

# ---------- 1) Filter 构建器 ----------

@dataclass
class TransactionFilter:
    """
    负责组装 WHERE 子句、参数、排序字段等。
    """
    _date_start: Optional[datetime] = None
    _date_end: Optional[datetime] = None
    _user_ids: Optional[List[int]] = None
    _min_amount: Optional[float] = None
    _max_amount: Optional[float] = None

    # 排序键（用于 keyset pagination），与 cursor 要保持一致
    _order_key: str = "start_date"   # 可换成 "end_date" 或 "amount" 等
    _order_dir: str = "ASC"          # 仅演示正向翻页（ASC）

    def set_date_range(self, start: Optional[datetime], end: Optional[datetime]) -> "TransactionFilter":
        self._date_start = start
        self._date_end = end
        return self

    def set_user_id(self, user_id: int) -> "TransactionFilter":
        self._user_ids = [user_id]
        return self

    def set_user_ids(self, user_ids: Iterable[int]) -> "TransactionFilter":
        ids = list(user_ids)
        self._user_ids = ids if ids else None
        return self

    def set_amount_range(self, min_amount: Optional[float], max_amount: Optional[float]) -> "TransactionFilter":
        self._min_amount = min_amount
        self._max_amount = max_amount
        return self

    def set_order(self, order_key: str, order_dir: str = "ASC") -> "TransactionFilter":
        # 允许的排序键（与表字段一致）
        allowed = {"start_date", "end_date", "amount", "id", "created_at"}
        if order_key not in allowed:
            raise ValueError(f"order_key must be one of {allowed}")
        if order_dir.upper() not in {"ASC", "DESC"}:
            raise ValueError("order_dir must be ASC or DESC")
        self._order_key = order_key
        self._order_dir = order_dir.upper()
        return self

    def build_where_clause(self) -> Tuple[str, List[Any]]:
        clauses = []
        params: List[Any] = []

        if self._date_start is not None:
            clauses.append("start_date >= %s")
            params.append(self._date_start)
        if self._date_end is not None:
            clauses.append("start_date <= %s")
            params.append(self._date_end)

        if self._user_ids:
            # IN 列表
            placeholders = ", ".join(["%s"] * len(self._user_ids))
            clauses.append(f"user_id IN ({placeholders})")
            params.extend(self._user_ids)

        if self._min_amount is not None:
            clauses.append("amount >= %s")
            params.append(self._min_amount)
        if self._max_amount is not None:
            clauses.append("amount <= %s")
            params.append(self._max_amount)

        where_sql = " WHERE " + " AND ".join(clauses) if clauses else ""
        return where_sql, params

    def build_order_clause(self) -> str:
        # 复合排序：order_key + id（保证稳定且唯一）
        return f" ORDER BY {self._order_key} {self._order_dir}, id {self._order_dir}"

    # 用于生成/解析 cursor 的排序键名
    def order_key(self) -> str:
        return self._order_key

    def order_dir(self) -> str:
        return self._order_dir


# ---------- 2) Cursor 编解码 ----------

def encode_cursor(order_key_value: Any, last_id: int) -> str:
    payload = {"k": order_key_value, "id": last_id}
    raw = json.dumps(payload, default=str).encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("ascii")

def decode_cursor(cursor: str) -> Dict[str, Any]:
    raw = base64.urlsafe_b64decode(cursor.encode("ascii"))
    payload = json.loads(raw.decode("utf-8"))
    # payload: {"k": <order_key_value>, "id": <int>}
    return payload


# ---------- 3) Repository：执行业务查询（PostgreSQL 例子） ----------

@dataclass
class TransactionRepository:
    """
    依赖一个 DB 连接（例如 psycopg2 或 asyncpg）。这里只给出同步示例接口。
    表结构假定：
      transactions(
        id BIGSERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL,
        amount NUMERIC(18,2) NOT NULL,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NULL,
        created_at TIMESTAMP NOT NULL DEFAULT now()
      )
    """
    conn: Any  # e.g., psycopg2 connection

    def fetch_page(
        self,
        tx_filter: TransactionFilter,
        page_size: int,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        返回 { "items": [...], "next_cursor": "..." or None }
        """
        base_sql = """
            SELECT id, user_id, amount, start_date, end_date, created_at
            FROM transactions
        """

        where_sql, params = tx_filter.build_where_clause()

        # 处理 cursor（键集翻页）
        # 注意：cursor 的 order_key 必须与当前 filter 的 _order_key 一致
        order_key = tx_filter.order_key()
        order_dir = tx_filter.order_dir()

        # 针对 ASC / DESC 方向，使用 > 或 < 做键集条件
        cmp_op = ">" if order_dir == "ASC" else "<"

        cursor_clause = ""
        if cursor:
            c = decode_cursor(cursor)
            # 复合比较：(order_key, id) > (k, id)  —— PostgreSQL 支持行值比较
            cursor_clause = f" ({order_key}, id) {cmp_op} (%s, %s) "
            params.extend([c["k"], c["id"]])

            # 如果已有 WHERE，用 AND 链接；否则补 WHERE
            if where_sql:
                where_sql += " AND " + cursor_clause
            else:
                where_sql = " WHERE " + cursor_clause

        order_sql = tx_filter.build_order_clause()
        limit_sql = " LIMIT %s"
        params.append(page_size + 1)  # 多取一条，用于判断是否还有下一页

        sql = base_sql + where_sql + order_sql + limit_sql

        # --- 执行查询 ---
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()

        # 多取一条判断是否还有下一页
        has_more = len(rows) > page_size
        items = rows[:page_size]

        next_cursor = None
        if has_more and items:
            last = items[-1]
            # 按 SELECT 列顺序：id, user_id, amount, start_date, end_date, created_at
            col_idx = {
                "id": 0,
                "user_id": 1,
                "amount": 2,
                "start_date": 3,
                "end_date": 4,
                "created_at": 5,
            }
            last_order_value = last[col_idx[order_key]]
            last_id = last[col_idx["id"]]
            next_cursor = encode_cursor(last_order_value, last_id)

        # 也可转成字典列表
        def to_obj(r):
            return {
                "id": r[0],
                "user_id": r[1],
                "amount": float(r[2]),
                "start_date": r[3].isoformat() if isinstance(r[3], datetime) else r[3],
                "end_date": r[4].isoformat() if isinstance(r[4], datetime) else r[4],
                "created_at": r[5].isoformat() if isinstance(r[5], datetime) else r[5],
            }

        return {
            "items": [to_obj(r) for r in items],
            "next_cursor": next_cursor,
        }




#################
#
#
#
#\
from datetime import datetime, timedelta
import psycopg2

conn = psycopg2.connect("dbname=app user=app password=secret host=127.0.0.1")

repo = TransactionRepository(conn)

# 1) 构建过滤条件
tx_filter = (
    TransactionFilter()
    .set_date_range(datetime(2025, 1, 1), datetime(2025, 12, 31))
    .set_user_ids([101, 102, 103])
    .set_amount_range(10.0, 1000.0)
    .set_order("start_date", "ASC")  # 与 cursor 一致
)

# 2) 首次取第一页
page_size = 50
page1 = repo.fetch_page(tx_filter, page_size=page_size, cursor=None)
print("count:", len(page1["items"]), "next_cursor:", page1["next_cursor"])

# 3) 取下一页
if page1["next_cursor"]:
    page2 = repo.fetch_page(tx_filter, page_size=page_size, cursor=page1["next_cursor"])
    print("count:", len(page2["items"]), "next_cursor:", page2["next_cursor"])
