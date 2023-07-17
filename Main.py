from Admin import Admin
from User import User

def main():
    shakil = User('1111', 'shakil', 'shakil@gmail.com', '4321') # User
    shakil.create_account('1111', 'shakil', 'shakil@gmail.com', '4321') # User
    shakil.deposit(5000)
    shakil.check_balance() # User

    tamim = User('1112', 'tamim', 'tamim@gmail.com', '4322') # User
    tamim.create_account('1112', 'tamim', 'tamim@gmail.com', '4322') # User

    
    shakil.deposit(4000) # User

    forhad = Admin('1234', 'forhad', 'forhad@gmail.com', '5432') # Admin
    forhad.create_account('1234', 'forhad', 'forhad@gmail.com', '5432') # Admin
    forhad.check_total_balance() # Admin

    tamim.deposit(30000) # User
    tamim.check_balance() # User

    forhad.check_total_balance() # Admin

    sakib = Admin('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.create_account('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.check_total_balance() # Admin

    tamim.check_balance() # User

    tamim.withdraw(1000) # User
    tamim.check_balance() # User

    tamim.transfer(shakil, 5000) # User
    shakil.check_balance() # User

    sakib.check_transaction() # Admin
    sakib.check_total_balance() # Admin

    shakil.take_loan(5000) # User
    shakil.check_balance() # User

    sakib.check_total_balance() # Admin

    tamim.check_balance() # User

    forhad.toggle_loan_feature(False) # Admin

    shakil.take_loan(5000) # User
    tamim.take_loan(5000) # User
    tamim.check_balance() # User
    shakil.check_balance() # User

    forhad.check_total_loan() # Admin
    forhad.check_transaction() # Admin

    shakil.check_transaction_history() # User
    tamim.check_transaction_history() # User

if __name__ == '__main__':
    main()
