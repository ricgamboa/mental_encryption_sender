# This module must be replaced with communication between the local client in the sender side
# and the remote server that manages the questions and save the answers

from pathlib import Path
import json
import me_components

class Communicator():

    def __init__(self):
        self.question = me_components.Question(0, 0)
        self.answer = []
        self.senderid = 0


    def request_question(self):
        # This method must be replaced by server communication
        # Request the server to send a question
        # The method reads the question, and save the values
        # to the member variable question changing to the right format

        question_info_path = Path.cwd().joinpath("project_files", "question_info")
        with open(question_info_path, "rt") as question_info:
            # read the line from the server
            line = question_info.readline()
            # change format and save the question in the current object
            question_dic = json.loads(line)
            self.question.id = question_dic["question_id"]
            self.question.num_answer_letters = question_dic["number_letters"]
            # save the set of icons in the question
            icons_list = question_dic["icons_lists_all"]
            for ic_li in icons_list:
                self.question.append_icon_set(ic_li["icon_list"])
            # save the position list
            position_list = question_dic["positions_lists_all"]
            for pos_li in position_list:
                self.question.append_position_list(pos_li["position_list"])


    def send_answer(self):
        #This method must be replaced by server comunication
        #send the answer to the server

        answer_info_path = Path.cwd().joinpath("project_files", "answer_info")
        answer_dic = {"user_id":self.senderid, "answer":self.answer, "question_id":self.question.id}
        answer_string = json.dumps(answer_dic)
        # send answer to server
        with open(answer_info_path, "w") as answer_info:
            answer_info.write(answer_string)
