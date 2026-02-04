from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    parent = {}
    set_count = None

    def init(n: int):
        nonlocal parent, set_count
        for i in range(n):
            parent[i] = i
        set_count = n 
    
    def find(x: int):
        nonlocal parent
        # print(parent)
        path = []
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        
        root = x
        for node in path:
            parent[node] = root
        
        return root

    def union(id1: int, id2: int):
        nonlocal parent, set_count
        r1 = find(id1) 
        r2 = find(id2)
        parent[r1] = r2
        set_count -= 1

    ######
    #
    # Above is union find implementation
    #
    ######

    def gen_email_to_ids(accounts):
        email_to_ids = {} # key: emails, value: list of ids
        for id, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_ids:
                    email_to_ids[email].append(id)
                else:
                    email_to_ids[email] = [id]
        return email_to_ids
    
    def gen_id_to_email_set(accounts):
        id_to_email_set = {}
        for id, account in enumerate(accounts):
            root_id = find(id)
            email_set = set() if root_id not in id_to_email_set else id_to_email_set[root_id]
            for email in account[1:]:
                email_set.add(email)
            id_to_email_set[root_id] = email_set
        return id_to_email_set


    # main code flow
    init(len(accounts))
    email_to_ids = gen_email_to_ids(accounts=accounts)
    print(email_to_ids)

    # union
    for email, ids in email_to_ids.items():
        root = ids[0]
        for id in ids[1:]:
            union(root, id)
    

    # after union, we get id to emails set
    id_to_email_set = gen_id_to_email_set(accounts)
    print(id_to_email_set)

    # print(find(0))
    # print(find(1))

    
    # 按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按字典序排序后的电子邮件。
    merged_accounts = []
    for id, emails_set in id_to_email_set.items():
        merged_accounts.append([accounts[id][0], *sorted(emails_set)])
    
    # print(merged_accounts)

    return merged_accounts
    


# print(accountsMerge(accounts=[["id1", "a", "b", "c"], ["id2", "b", "d"], ["id1", "f", "e"]]))


print(accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))