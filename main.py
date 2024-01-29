import users
import quiz
import menu
import sys

def main():
    print(menu.quiz_app)
    # print(menu.login_menu)

    temp_user = users.User()
    temp_quiz = quiz.Quiz()
    temp_scoreboard = quiz.ScoreBoard()

    obj_list = [temp_user, temp_quiz, temp_scoreboard]

    #menu selection
    menu.menu_selector(menu.login_menu, obj_list)

    quiz_on = "y"
    round = -1
    quiz_list = []

    
    while quiz_on == "y":
        quiz_n = menu.menu_selector(menu.quiz_menu, obj_list)
        if "Quiz" in type(quiz_n).__name__:
            round += 1
            quiz_list.append(quiz_n)
            print(menu.quiz_categories)
            print(quiz_list[round])
            print(f"You started a new quiz with score {quiz_list[round].score}")
            choice = menu.select_menu_item(menu.quiz_categories)
            quiz_list[round].topic = choice
            quiz_list[round].ask_question()
            temp_scoreboard.score += quiz_list[round].score
            quiz_on = input("Do you want one more round? (y/n)").lower()
        else: quiz_on = "n"
        
    
    menu.menu_selector(menu.quiz_menu, obj_list)
        

main()

if __name__ == "__main__":
    sys.exit(main())