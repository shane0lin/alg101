# 721 Accounts Merge

# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Example 2:

# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

parent = []

def initialize(n):
    global parent
    parent = [i for i in range(n)]

def union(x, y):
    global parent
    parent[find(x)] = find(y)

def find(x):
    global parent
    path = []
    while parent[x] != x:
        path.append(x)
        x = parent[x]

    for u in path:
        parent[u] = x
    return x

def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """

   
    initialize(len(accounts))


    # build a map, email: id
    id_m = {} # email: id
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email not in id_m:
                id_m[email] = i
            else:
                union(i, id_m[email])

    # build a map, id: email_set
    id_to_email = {} # id: email_set
    for i, account in enumerate(accounts):
        root_id = find(i)
        emailset = id_to_email.get(root_id, set())
        emailset |= set(account[1:])
        id_to_email[root_id] = emailset
        

    merged = []
    for root_id, emailset in id_to_email.items():
        merged.append([accounts[root_id][0]] + sorted(emailset))
    
    return merged

# print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
# print(accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))

import unittest

class TestAccountMerge(unittest.TestCase):
    
    def test_example_1(self):
        """Test with the first example from the problem statement."""
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ]
        
        result = accountsMerge(accounts)
        
        # Since the order of accounts doesn't matter, we'll sort them for comparison
        result = sorted(result, key=lambda x: x[0] + ''.join(x[1:]))
        
        expected = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        expected = sorted(expected, key=lambda x: x[0] + ''.join(x[1:]))
        
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """Test with the second example from the problem statement."""
        accounts = [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]
        ]
        
        result = accountsMerge(accounts)
        
        # Sort for comparison
        result = sorted(result, key=lambda x: x[0])
        
        expected = [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"]
        ]
        
        self.assertEqual(result, expected)
    
    def test_single_account(self):
        """Test with a single account."""
        accounts = [["John", "john@example.com"]]
        result = accountsMerge(accounts)
        expected = [["John", "john@example.com"]]
        self.assertEqual(result, expected)
    
    def test_no_common_emails(self):
        """Test with accounts that have no common emails."""
        accounts = [
            ["John", "john1@example.com"],
            ["John", "john2@example.com"],
            ["John", "john3@example.com"]
        ]
        
        result = accountsMerge(accounts)
        
        # Sort for comparison
        result = sorted(result, key=lambda x: ''.join(x[1:]))
        
        expected = [
            ["John", "john1@example.com"],
            ["John", "john2@example.com"],
            ["John", "john3@example.com"]
        ]
        expected = sorted(expected, key=lambda x: ''.join(x[1:]))
        
        self.assertEqual(result, expected)
    
    def test_all_accounts_merge(self):
        """Test where all accounts should merge into one."""
        accounts = [
            ["John", "email1@example.com"],
            ["John", "email1@example.com", "email2@example.com"],
            ["John", "email2@example.com", "email3@example.com"],
            ["John", "email3@example.com", "email4@example.com"]
        ]
        
        result = accountsMerge(accounts)
        
        expected = [["John", "email1@example.com", "email2@example.com", "email3@example.com", "email4@example.com"]]
        
        # Check if all emails are present in the result
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "John")
        self.assertCountEqual(result[0][1:], ["email1@example.com", "email2@example.com", "email3@example.com", "email4@example.com"])
    
    # def test_different_names_same_email(self):
    #     """Test with different names but same email (should not merge)."""
    #     accounts = [
    #         ["John", "john@example.com"],
    #         ["Jane", "john@example.com"]
    #     ]
        
    #     result = accountsMerge(accounts)
        
    #     # This is a bit tricky as the problem states people with same name can have different accounts,
    #     # but doesn't explicitly handle the case where different names have the same email.
    #     # The expected behavior would depend on the problem's constraints.
    #     # For this test, we'll assume they should be separate accounts.
        
    #     # Sort for comparison
    #     result = sorted(result, key=lambda x: x[0])
        
    #     expected = [
    #         ["Jane", "john@example.com"],
    #         ["John", "john@example.com"]
    #     ]
    #     expected = sorted(expected, key=lambda x: x[0])
        
    #     self.assertEqual(result, expected)
    
    def test_complex_merging(self):
        """Test with a more complex merging scenario."""
        accounts = [
            ["John", "email1@example.com", "email2@example.com"],
            ["Mary", "email3@example.com"],
            ["John", "email2@example.com", "email4@example.com"],
            ["Bob", "email5@example.com"],
            ["Mary", "email6@example.com", "email3@example.com"],
            ["John", "email7@example.com", "email8@example.com"],
            ["Bob", "email9@example.com", "email5@example.com"]
        ]
        
        result = accountsMerge(accounts)
        
        # Sort accounts by name and then by first email for comparison
        result = sorted(result, key=lambda x: (x[0], x[1] if len(x) > 1 else ""))
        
        # Expected: John has two separate accounts, Mary has one, Bob has one
        expected = [
            ["Bob", "email5@example.com", "email9@example.com"],
            ["John", "email1@example.com", "email2@example.com", "email4@example.com"],
            ["John", "email7@example.com", "email8@example.com"],
            ["Mary", "email3@example.com", "email6@example.com"]
        ]
        expected = sorted(expected, key=lambda x: (x[0], x[1] if len(x) > 1 else ""))
        
        self.assertEqual(result, expected)
    def test_leetcode_1(self):
        accounts = [
            ["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]
        ]
        result = accountsMerge(accounts)
        expected = [
            ["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()