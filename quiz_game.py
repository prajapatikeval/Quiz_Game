import random


class QuizGame:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": "Paris",
            "What is the largest ocean in the world?": "Pacific Ocean",
            "What is the currency of Japan?": "Japanese yen"
        }
        self.userid = {
            "example@gmail.com": "example1234",
            "example1@gmail.com": "example1111",
            "1": "1",
        }
        self.score = 0

    def Start(self, username):

        print("\n<<<  Welcome to the quiz game!  >>>", username, "\n")

        i = 0
        for question in self.questions:

            answer = input(f"Quetion No.{i+1} : {question} : ")
            i = i+1
            if answer.lower() == self.questions[question].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect. The correct answer is",
                      self.questions[question])
        print("You scored", self.score, "out of", len(self.questions))

        again = input("You want to Play Again!! : ")
        if again != "yes".lower():
            Main_Menu()

    def Login(self):
        print("\n<<<<  Welcome to Login Page  >>>>\n")

        username = input("Enter a Username : ")
        password = input("Enter a password : ")

        for key, value in self.userid.items():

            if username == key and password == value:
                while True:
                    print(
                        "\nType 1 : -----------------Create Quetion---------------------")
                    print(
                        "Type 2 : -----------------Delete Quetion --------------------")
                    print(
                        "Type 3 : -----------------Play game -------------------------")
                    print(
                        "Type 4 : -----------------Back ------------------------------\n")

                    admin_choice = input("Ente Type : ")

                    if admin_choice == "1":
                        quetion = input("Enter a Quetion : ")
                        answer = input("ENter a Answer Of given quetion : ")
                        self.questions[quetion] = answer
                        continue
                    elif admin_choice == "2":
                        for i, (key, value) in enumerate(self.questions.items()):
                            print(f"{i+1}: {key}")

                        del_quetion = int(input(
                            "Enter No to Delete | Or type 0 for Back : "))

                        for i, (key, value) in enumerate(self.questions.items()):
                            if del_quetion == i+1:
                                del self.questions[key]
                                break
                            elif del_quetion == "0":
                                game.Login()
                                break

                    elif admin_choice == "3":
                        game.Start(username)

                    elif admin_choice == "4":
                        Main_Menu()
                    else:
                        print("\n<<<  Unapropriate Input Type  >>>")
                        continue


game = QuizGame()


def Main_Menu():
    while True:
        print("\n")

        print("\n<<<<<  Main Menu  >>>>>\n")

        print("Type 1 : -----------------Login------------------------------")
        print("Type 2 : -----------------To play game ----------------------")
        print("Type 3 : -----------------Exit ------------------------------\n")
        admin = input("Which type : ")

        username = "Unknown"
        if admin == "1":
            game.Login()
        elif admin == "2":
            game.Start(username)
        elif admin == "3":
            quit()
        else:
            print("\n<<<  Unapropriate Input Type  >>>")
            continue


Main_Menu()
