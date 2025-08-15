# Level 1: Create Account, Transfer funds

# Level 2: Return the accounts with top k total outgoing funds
# Level 3， 需要实现支付功能，而且要Credit account 2% cashback，要在24小时以后到帐，更新账户的balance
# Level 4 是Merge Account
# Level 3: Implement Payment with Credit Account Cashback
# To implement the payment functionality with a 2% cashback feature that credits the account after 24 hours, we need to extend the existing codebase. Here's how we can approach this:        
# 1. **Add a new method to the `Account` class** to handle payments with cashback.
# 2. **Schedule the cashback credit** to occur after 24 hours.
# 3. **Update the account balance** after the cashback is credited.
# Here's the implementation:  

class Account:
    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance
        self.transactions = []
        self.cashback_scheduled = []
    def transfer(self, target_account: 'Account', amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f"Transferred {amount} to {target_account.account_id}")
            target_account.transactions.append(f"Received {amount} from {self.account_id}")
            return True
        return False
    def pay_with_cashback(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            cashback_amount = amount * 0.02
            # Schedule the cashback to be credited after 24 hours
            self.cashback_scheduled.append((cashback_amount, time.time() + 86400))
            self.transactions.append(f"Paid {amount} with 2% cashback scheduled")
            return True
        return False
    def credit_cashback(self):
        current_time = time.time()
        for cashback_amount, scheduled_time in self.cashback_scheduled[:]:
            if current_time >= scheduled_time:
                self.balance += cashback_amount
                self.transactions.append(f"Credited {cashback_amount} cashback")
                self.cashback_scheduled.remove((cashback_amount, scheduled_time))
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_id: str, initial_balance: float) -> bool:
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id, initial_balance)
            return True
        return False
    def get_account(self, account_id: str) -> Account:
        return self.accounts.get(account_id)
    def transfer_funds(self, source_id: str, target_id : float) -> bool:
        source_account = self.get_account(source_id)
        target_account = self.get_account(target_id)
        if source_account and target_account:
            return source_account.transfer(target_account, amount)
        return False
    def pay_with_cashback(self, account_id: str, amount: float) -> bool:
        account = self.get_account(account_id)
        if account:
            return account.pay_with_cashback(amount)
        return False
    def credit_cashback(self, account_id: str):
        account = self.get_account(account_id)
        if account:
            account.credit_cashback()
    def get_top_k_accounts_by_outgoing_funds(self, k: int) -> List[str]:
        outgoing_funds = {}
        for account_id, account in self.accounts.items():
            outgoing_funds[account_id] = sum(
                float(transaction.split()[1])
                for transaction in account.transactions
                if transaction.startswith("Transferred")
            )
        sorted_accounts = sorted(outgoing_funds.items(), key=lambda x: x[1], reverse=True)
        return [account_id for account_id, _ in sorted_accounts[:k]]
    def merge_accounts(self, account_id1: str, account_id2: str) -> bool:
        account1 = self.get_account(account_id1)
        account2 = self.get_account(account_id2)
        if account1 and account2:
            # Merge balances
            merged_balance = account1.balance + account2.balance
            # Create a new account with the merged balance
            merged_account_id = f"{account_id1}_{account_id2}"
            self.accounts[merged_account_id] = Account(merged_account_id, merged_balance)
            # Merge transactions
            self.accounts[merged_account_id].transactions = account1.transactions + account2.transactions
            # Remove the old accounts
            del self.accounts[account_id1]
            del self.accounts[account_id2]
            return True
        return False