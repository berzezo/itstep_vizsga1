import users

# questions_file = file_handler.FileHandler("questions.txt")
# questions_blocks = questions_file.read_in_blocks()
# question_list = []


# for q_block in questions_blocks:
#     q_block = q_block.splitlines()
#     temp_dict = {}
#     for q_item in q_block:
#         a = q_item.split(":")
#         (key, val) = (a[0], a[1])
#         temp_dict.update({key: val})
#     question_list.append(temp_dict)
# print(question_list)


# import quiz

# q = quiz.pick_random_question(quiz.get_questions())

# print("\nCategory:" + q["Topic"])
# print("Question:" + q["Question"])
# print("Choices:")
# keys = ["a", "b", "c", "d"]
# for key in keys:
#     print(key + ": " + q[key])
# print("\n")


# user = users.User()
func_name ="login"
attr = getattr(users.User, func_name, None)
print(attr)