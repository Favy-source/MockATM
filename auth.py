# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# fav Bank

# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    print("Welcome to favBank")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("Enter your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("Enter your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            fav_bank(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("Enter your email address \n")
    first_name = input("Enter your first name \n")
    last_name = input("Enter your last name \n")
    password = getpass("Create a password for yourself \n")

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("SUCCESS! Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Dont didsclose it to anyone")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("registration failed, please try again")
        register()


def fav_bank(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("Do you want to (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_process()
    elif selected_option == 2:

        withdrawal_process()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        fav_bank(user)


def withdrawal_process():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_process():
    print("Deposit Process")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def setting_current_balance(user_details, balance):
    user_details[4] = balance


def getting_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
