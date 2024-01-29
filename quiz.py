from file_handler import FileHandler
import menu
import random
import datetime

N_OF_QUESTIONS = 20

class Quiz:
    file = FileHandler("itstep_vizsga1/questions.txt")
    questions = file.blocks_to_dict()

    def __init__(self, score = 0, question_number = 1, topic = ""):
        # self.questions = questions
        self.score = score
        self.question_number = question_number
        self.topic = topic

    def select_topic(self):
        filtered_questions = []
        if self.topic == "General Knowledge (mixed)":
            return self.questions
        else:
            for q in self.questions:
                if self.topic == q["Topic"]:
                    filtered_questions.append(q)
            return filtered_questions

    def check_answer(self, right_answer):
        user_answer = input("Enter one or more answer, separated by comma in order:\n e.g.: a,c,d or a,b or b\n").replace(" ", "").lower()
        if user_answer == right_answer.replace(" ", "").lower():
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0

    def ask_question(self):
        rand_q_list = random.sample(self.select_topic(), N_OF_QUESTIONS)
        for q in rand_q_list:
            print(q["Right answer"]) #for checking operation
            print(f"\nQuestion number: {self.question_number}")
            print("\nCategory:" + q["Topic"])
            print("Question:" + q["Question"])
            print("Choices:")
            choice_keys = ["a", "b", "c", "d"]
            for key in choice_keys:
                print(key + ": " + q[key])
            print("\n")
            right_answer = q["Right answer"]
            self.score += self.check_answer(right_answer)
            self.question_number += 1
            print(f"Score: {self.score}")
    
    @classmethod
    def edit_quiz(cls):
        print(menu.editing_quiz)

    @classmethod
    def add_question(cls):
        more = "y"
        while more == "y":
            new_question = {"Question": input("Enter question: "),
            "Topic": input("Enter topic:\n History/Geography/Science & Nature/Music/Art and Literature\n"),
            "a": input("Enter choice a: "),
            "b": input("Enter choice b: "),
            "c": input("Enter choice c: "),
            "d": input("Enter choice d: "),
            "Right answer": input("Enter right answer: ")}

            topics = ["History", "Geography", "Science & Nature", "Music", "Art and Literature"]
            if new_question["Topic"] in topics:
                cls.questions.append(new_question)
                print("Question added...")
                more = input("Do you want to add more?\n(y)es or (n)o\n")
            else:
                print("Please enter a valid topic")
    
    @classmethod
    def remove_question(cls):
        cont_remove = "y"
        while cont_remove == "y":
            search_phrase = input("You can search in questions.\nEnter search phrase:\n")
            for question in cls.questions:
                if search_phrase.lower().strip() in question["Question"].lower().strip():
                    print(question)
                    if input("Do you want to remove this question?\n(y)es or (n)o\n") == "y":
                        cls.questions.remove(question)
                        print("Question removed...")
                        break
                    else:
                        print("No question removed")
                        break
            else:
                print("No question found")
            cont_remove = input("Do you want to continue removing questions?\n(y)es or (n)o\n")
    
    @classmethod
    def modify_question(cls):
        cont_modif = "y"
        while cont_modif == "y":
            search_phrase = input("You can search in questions.\nEnter search phrase:\n")
            for question in cls.questions:
                if search_phrase.lower().strip() in question["Question"].lower().strip():
                    print(question)
                    if input("Do you want to modify this question?\n(y)es or (n)o\n") == "y":
                        key = input("Enter what to modify:\n")
                        question[key] = input("Enter new value:\n")
                        print("Question modified...")
                        break
                    else:
                        print("No question modified")
                        break
                else:
                    print("No question found")
            cont_modif = input("Do you want to continue modifying questions?\n(y)es or (n)o\n")
    
    def save_files(self):
        self.file.save_files(self.questions)


class ScoreBoard:
    statfile = FileHandler("itstep_vizsga1/stats.txt")
    stats = statfile.blocks_to_dict()

    def __init__(self, score = 0, username = ""):
        self.score = score
        self.username = username

    def score_logger(self):
        self.stats.append({"Timestamp": datetime.datetime.now(), "Username": self.username, "Score": self.score})

    def view_scoreboard(self):
        print("Scoreboard:\n")
        for item in self.stats:
            [print(f"{key}: {value}") for key, value in item.items()]

    def view_top_twenty(self):
        print("Top 20:\n")
        sorted_list = sorted(self.stats, key=lambda k: (k['Score'], k['Timestamp']), reverse=True)
        for item in sorted_list[:20]:
            [print(f"{key}: {value}") for key, value in item.items()]

    def save_files(self):
        self.statfile.save_files(self.stats)
