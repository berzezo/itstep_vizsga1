# from users import User
# from quiz import Quiz
# from quiz import ScoreBoard

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def save_files(self, data):
        ''' Saves data to file. Expect dictionary or list of dictionaries.'''
        lines = ""
        for block in data:
            for item in block:
                (key, val) = item.items()
                lines += f"{key}: {val}\n"
            lines += "\n"
        with open(self.file_name, "w") as file:
            file.write(lines)

    def read_all(self):
        with open(self.file_name, "r") as file:
            return file.read()
    
    def read_in_blocks(self):
        read_file = self.read_all()
        object_blocks = read_file.split("\n\n")
        return object_blocks #as a list of single or multiline string blocks
    
    def blocks_to_dict(self):
        blocks = self.read_in_blocks()
        block_list = []

        for block in blocks:
            block = block.splitlines()
            temp_dict = {}
            for item in block:
                a = item.split(":")
                (key, val) = (a[0].strip(), a[1].strip())
                temp_dict.update({key: val})
            block_list.append(temp_dict)
        return block_list
