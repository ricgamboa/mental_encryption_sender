# Main program used by the sender to receive question and send encrypted answer


import server_communicator, user_interface


def main():

    ALPHABET_SIZE = 4

    # Request question
    communicator = server_communicator.Communicator()
    communicator.request_question()

    interface = user_interface.UserInterface(communicator.question)
    # Request sender id
    interface.request_senderid()

    # Show general information to the sender
    interface.show_general_info()

    # Show the list of random positions to the sender and the encrypt alphabet
    # for each letter
    for num_letter in range(communicator.question.num_answer_letters):
        interface.show_position_list(num_letter)
        interface.show_icon_groups(ALPHABET_SIZE, num_letter)

    # Read the encrypted answer
    interface.read_answer()

    # Send the answer
    communicator.answer = interface.answer
    communicator.senderid = interface.senderid
    communicator.send_answer()


if __name__ == "__main__":
    main()
