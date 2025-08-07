# 给出一个数组[[borrower, lender, debt], ...]，返回正数的第二名欠钱最多的人的债务数字# 解题思路


# 1. **计算每个人的净债务**：首先，我们需要计算每个人的净债务。这意味着我们需要遍历所有的债务记录，对于每个债务记录，我们将债务从借款人中减去，并将债务加到借款人中。
# 2. **排序净债务**：接下来，我们需要将所有的净债务值排序，以便找到第二大的正数债务值。
# 3. **返回第二大的正数债务值**：在排序后的列表中，我们需要找到第二大的正数债务值，并将其返回。
# 解决代码

from collections import defaultdict
def second_max_debt(debts):
    # 计算每个人的净债务
    net_debts = defaultdict(int)
    for borrower, lender, debt in debts:
        net_debts[borrower] -= debt
        net_debts[lender] += debt
    # 获取所有正数的净债务值
    positive_debts = [debt for debt in net_debts.values() if debt < 0]
    # 排序正数的净债务值
    positive_debts.sort(reverse=True)
    # 返回第二大的正数债务值，如果不存在则返回0
    if len(positive_debts) >= 2:
        return positive_debts[1]
    else:
        return 0


# 示例用法
debts = [["A", "B", 10], ["C", "A", 5], ["D", "B", 13], ["E", "C", 20]]
print(second_max_debt(debts))  # 输出: 10