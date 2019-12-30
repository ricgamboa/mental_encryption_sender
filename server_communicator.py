# This module must be replaced with communication between the local client in the sender side
# and the remote server that manages the questions and save the answers

from pathlib import Path
import def_classes, rw_database

class Communicator():

    def __init__(self):
        self.question = def_classes.Question(0,0)
        self.answer = []
        self.senderid = 0

    def string_to_list(self, string):
        # change string to list
        del_bracket = string.lstrip('[').rstrip(']')
        temp_li = list(del_bracket.split(","))
        li = []
        for item in temp_li:
            item = item.strip('\n')
            item = item.strip(']')
            item = item.strip('[')
            li.append(item)
        return li

    def request_question(self):
        # This method must be replaced by server communication
        # Request the server to send a question
        # The method reads the question, and save the values
        # to the member variable question changing to the right format

        question_database_path = Path.cwd().joinpath("project_files", "question_database")
        with open(question_database_path, "rt") as question_database:
            line = question_database.readline()
            question_split = line.split('*%')
            self.question.id = int(question_split[0])
            self.question.num_answer_letters = int(question_split[1])
            #save the set of icons in the question
            str_icons = question_split[2].split('%ic_list_')
            for ic_li in range(len(str_icons)):
                temp_icons = self.string_to_list(str_icons[ic_li])
                icons_list = [int(i) for i in temp_icons]
                self.question.append_icon_set(icons_list)
            #save the position list
            str_position = question_split[3].split('%pos_list_')
            for pos_li in range(len(str_position)):
                temp_position = self.string_to_list(str_position[pos_li])
                pos_list = [int(i) for i in temp_position]
                self.question.append_position_list(pos_list)


    def send_answer(self):
        #This method must be replaced by server comunicatio
        #send the answer to the server
        rw_database.save_answer(self.senderid, self.answer, self.question.id)

