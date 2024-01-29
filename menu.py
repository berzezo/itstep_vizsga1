import quiz
import file_handler

quiz_app = '''
------------------------------------------------------------------------
------------------------------------------------------------------------
                        Welcome to the quiz app!
------------------------------------------------------------------------
------------------------------------------------------------------------
'''
login_menu = '''
------------------------------------------------------------------------
                        User Menu / Logged out
------------------------------------------------------------------------
        1. Login
        2. Register
        3. Exit
'''

quiz_menu = '''
------------------------------------------------------------------------
                            Quiz Main Menu
------------------------------------------------------------------------
        1. Start New Quiz
        2. Edit Quiz
        3. View Scoreboard
        4. View Top Twenty
        5. View User Data
        6. Modify User Data
        7. Save File
        8. Logout
'''

# user_menu_logged_in = '''
# ------------------------------------------------------------------------
#                         User Menu / Logged in
# ------------------------------------------------------------------------
#         1. View User Data
#         2. Modify User Data
#         3. Logout
#         4. Back
# '''

quiz_categories = '''
------------------------------------------------------------------------
                        Select Quiz Category
------------------------------------------------------------------------
        1. General Knowledge (mixed)
        2. History
        3. Geography
        4. Science & Nature
        5. Music
        6. Art and Literature
        7. Back
'''

editing_quiz = '''
------------------------------------------------------------------------
                            Quiz Modify Menu
------------------------------------------------------------------------
        1. Add Question
        2. Remove Question
        3. Modify Question
        4. Back
'''

# temp_user = users.User()
# temp_quiz = quiz.Quiz()
# temp_scoreboard = quiz.ScoreBoard()

def menu_choices(menu_type):
        menu_lines = menu_type.splitlines()
        menu_items ={}

        for i in range(4, len(menu_lines)):
                number, menu_text = menu_lines[i].split(".")
                number = number.strip()
                menu_text = menu_text.strip()
                menu_items.update({number: menu_text})
        return menu_items

def select_menu_item(menu_type):
        print(menu_type)
        input_menu = input("Enter a number from the menu to select: ")
        #TODO try-except dict.get: (KeyError)
        return menu_choices(menu_type)[input_menu]

def menu_selector(menu_item, object_list):
        choice = select_menu_item(menu_item)
        func_name = choice.strip().replace(" ", "_").lower()
        if func_name == "back":
                return menu_selector(quiz_menu, object_list)
        elif func_name == "start_new_quiz":
                return quiz.Quiz()
        elif func_name == "edit_quiz":
                return menu_selector(editing_quiz, object_list)
        elif func_name == "logout":
                object_list[0].logout()
                for val in object_list:
                        val.save_file()
                return menu_selector(login_menu, object_list)
        else:
                for val in object_list:
                        function_to_call = getattr(val, func_name, None)
                        if function_to_call and callable(function_to_call):
                                function_to_call()
