from file_handler import FileHandler
import datetime
import sys


class User:
    file = FileHandler("itstep_vizsga1/users.txt")
    users = file.blocks_to_dict()
    
    def __init__(self, username = None, date_of_birth = None, password = None, logged_in = False):
        self.username = username
        self.date_of_birth = date_of_birth
        self.password = password
        self.logged_in = logged_in

    def user_logger(function):
        def wrapper(self, *args, **kwargs):
            result = function(self, *args, **kwargs)
            action = function.__name__
            with open("logs.txt", "a") as file:
                file.write(f"User {action} was performed by {self.username} at {datetime.datetime.now()}\n")
            return result
        return wrapper

    @user_logger
    def register(self):
        print("Registering user...")
        user_found = "a"
        while user_found == "a":
            self.username = input("Enter username: ")
            for user in self.users:
                if user["username"] == self.username:
                    user_found = input("Username already exists, please:\n(a) try again or\n(b) login\n")
                    break
                else:
                     user_found = "c"
        if user_found == "b":
            return self.login()
        elif user_found == "c":
            self.password = input("Enter password: ")
            self.date_of_birth = input("Enter date of birth: ")
            self.users.append({"username": self.username, "date_of_birth": self.date_of_birth, "password": self.password, "logged_in": self.logged_in})
            print("User registration completed. Please login.")
            return self.login()

    @user_logger
    def login(self):
        print("Logging in...")
        login_found = "a"
        while self.logged_in == False and login_found == "a":
            self.username = input("Enter username: ")
            self.password = input("Enter password: ")
            for user in self.users:
                if user["username"] == self.username and user["password"] == self.password:
                    self.logged_in = True
                    user["logged_in"] = True
                    self.date_of_birth = user["date_of_birth"]
                    return print("Successfully logged in\n")
                else:
                    self.logged_in = False
            login_found = input("Incorrect username or password. Please\n(a) try again or\n(b) register\n\n")
        if login_found == "b":
             return self.register()
    
    @user_logger
    def view_user_data(self):
        print("User data:")
        if self.logged_in == True:
            print(f"Username: {self.username}\nPassword: {self.password}\nDate of birth: {self.date_of_birth}\nLogged in: {self.logged_in}\n")

    @user_logger
    def modify_user_data(self):
        if self.logged_in == True:
            data_type = input("Choose data type:\n(a) date of birth\n(b) password\n\n")
            if data_type == "a":
                self.date_of_birth = input("Enter date of birth:\n")
            elif data_type == "b":
                    self.password = input("Enter new password:\n")
                    self.users.update({"username": self.username, "date_of_birth": self.date_of_birth, "password": self.password, "logged_in": self.logged_in})
            return print("Successfully changed data")
        else:
            print("Please login first")
            return self.login()
   
    @user_logger
    def logout(self):
        if self.logged_in == True:
            self.logged_in = False
            self.username = None
            self.password = None
            self.date_of_birth = None
            print("Successfully logged out")

    @user_logger
    def save_files(self):
        self.file.save_files(self.users)

    @user_logger
    def exit(self):
        sys.exit(0)
    