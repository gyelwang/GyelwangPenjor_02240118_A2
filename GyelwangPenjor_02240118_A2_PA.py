import random

class ScoreBoard:
    def __init__(self):
        self.scores = {
            "Number Guessing": [],
            "Rock Paper Scissors": [],
            "Quiz": []
        }

    def add_score(self, game, score):
        self.scores[game].append(score)

    def show_scores(self):
        print("\n======= SCOREBOARD =======")
        for game, score_list in self.scores.items():
            if score_list:
                print(f"{game}: {score_list} (Avg: {sum(score_list)/len(score_list):.2f})")
            else:
                print(f"{game}: No scores yet.")

class NumberGuessingGame:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        while True:
            target = random.randint(1, 10)
            attempts = 0

            while True:
                try:
                    guess = input("Guess a number between 1 and 10 (or 'q' to quit): ").strip()
                    if guess.lower() == 'q':
                        return
                    guess = int(guess)
                    attempts += 1

                    if guess < target:
                        print("Too low! Try a larger number.")
                    elif guess > target:
                        print("Too high! Try a smaller number.")
                    else:
                        print("Nice! You got it right.")
                        score = max(0, 10 - attempts)
                        print(f"Your score: {score}")
                        self.scoreboard.add_score("Number Guessing", score)
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            again = input("Want to try again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Goodbye! Thanks for playing.")
                break


class RockPaperScissors:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        wins = 0
        options = ["rock", "paper", "scissors"]

        while True:
            player = input("Choose (rock, paper, or scissors): ").lower()
            if player not in options:
                print("Invalid choice.")
                continue

            bot = random.choice(options)
            print(f"The computer picked: {bot}")

            if player == bot:
                print("It's a draw!")
            elif (player == "rock" and bot == "scissors") or \
                 (player == "paper" and bot == "rock") or \
                 (player == "scissors" and bot == "paper"):
                print("You win this round!")
                wins += 1
            else:
                print("You lost this round!")

            again = input("Play again? (yes/no): ").lower()
            if again != "yes":
                print(f"Total wins: {wins}")
                print("Thanks for playing!")
                self.scoreboard.add_score("Rock Paper Scissors", wins)
                break


class MultipleChoiceQuiz:
    questions = [
        {"q": "Which of the following animals can survive in space (without protection) for a short time?",
         "options": ["A) Cockroach", "B) Jellyfish", "C) Tardigrade", "D) Frog"], "answer": "C"},
        {"q": "In coding, what does the acronym 'API' stand for?",
         "options": ["A) Automated Programming Interface", "B) Application Programming Interface", "C) Applied Protocol Integration", "D) Advanced Python Interface"], "answer": "B"},
        {"q": "Which planet has the most moons?",
         "options": ["A) Jupiter", "B) Neptune", "C) Saturn", "D) Uranus"], "answer": "C"},
        {"q": "Which animal is known to be biologically immortal?",
         "options": ["A) Tardigrade", "B) Hydra", "C) Starfish", "D) Clam"], "answer": "B"},
        {"q": "What color is the blood of an octopus?",
         "options": ["A) Red", "B) Green", "C) Blue", "D) Yellow"], "answer": "C"},
        {"q": "How many hearts does an octopus have?",
         "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "C"},
        {"q": "Which was the first programmable computer?",
         "options": ["A) ENIAC", "B) UNIVAC", "C) Z3", "D) IBM 701"], "answer": "C"},
        {"q": "What shape is wombat poop?",
         "options": ["A) Spherical", "B) Cube-Shaped", "C) Cone-Shaped", "D) Flat"], "answer": "B"},
        {"q": "What animal's milk is pink?",
         "options": ["A) Hippo", "B) Cow", "C) Whale", "D) Dolphin"], "answer": "A"},
        {"q": "Which is the only food that never spoils?",
         "options": ["A) Salt", "B) Sugar", "C) Honey", "D) Vinegar"], "answer": "C"}
    ]

    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        while True:
            responses = []
            score = 0

            for item in self.questions:
                print("\n" + item["q"])
                for option in item["options"]:
                    print(option)

                ans = input("Your answer (A/B/C/D): ").strip().upper()
                responses.append(ans)

                if ans == item["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {item['answer']}.")

            print("\n====== QUIZ SUMMARY ======")
            print(f"Score: {score} out of {len(self.questions)}")
            print(f"Percentage: {int((score / len(self.questions)) * 100)}%")
            self.scoreboard.add_score("Quiz", score)

            again = input("Play again? (yes/no): ").lower()
            if again != "yes":
                print("Thanks for playing!")
                break
class PokemonCardBinder:
    def __init__(self):
        self.binder = {}
        self.max_entries = 1025

    def get_slot(self, pokedex_no):
        pos = pokedex_no - 1 
        return pos // 64 + 1, (pos % 64) // 8 + 1, (pos % 8) + 1

    def add_entry(self):
        try:
            num = int(input("Enter Pokedex number (1–1025): "))
            if num < 1 or num > self.max_entries:
                print("Invalid number.")
                return
            if num in self.binder:
                page, row, col = self.binder[num]
                print(f"Already exists -> Page {page}, Row {row}, Column {col}")
            else:
                slot = self.get_slot(num)
                self.binder[num] = slot
                print(f"Added -> Page {slot[0]}, Row {slot[1]}, Column {slot[2]}")
                if len(self.binder) == self.max_entries:
                    print("You've collected them all!")
        except ValueError:
            print("Please enter a valid number.")

    def reset_binder(self):
        confirm = input("Type 'CONFIRM' to clear all data: ")
        if confirm == "CONFIRM":
            self.binder.clear()
            print("Binder reset complete.")

    def show_binder(self):
        print("\nYour Binder:")
        if not self.binder:
            print("It's currently empty.")
        else:
            for num in sorted(self.binder):
                p, r, c = self.binder[num]
                print(f"#{num}: Page {p}, Row {r}, Column {c}")
        print(f"Total cards: {len(self.binder)} / {self.max_entries}")
        print(f"Completion: {round(len(self.binder) / self.max_entries * 100, 1)}%")

    def play(self):
        while True:
            print("\nPokémon Binder Manager")
            print("1. Add card")
            print("2. Clear binder")
            print("3. View binder")
            print("4. Exit")
            option = input("Choose: ")

            if option == "1":
                self.add_entry()
            elif option == "2":
                self.reset_binder()
            elif option == "3":
                self.show_binder()
            elif option == "4":
                print("Exiting binder manager.")
                break
            else:
                print("Invalid option.")



class MainMenu:
    def __init__(self):
        self.scoreboard = ScoreBoard()
        self.games = {
            "1": NumberGuessingGame(self.scoreboard),
            "2": RockPaperScissors(self.scoreboard),
            "3": MultipleChoiceQuiz(self.scoreboard),
            "4": PokemonCardBinder()
        }

    def show(self):
        while True:
            print("\n================= M A I N  M E N U =================")
            print("1. Number Guessing Game")
            print("2. Rock Paper Scissors")
            print("3. Multiple Choice Quiz")
            print("4. Pokémon Card Binder")
            print("5. View Scoring System")
            print("6. Exit")

            choice = input("Select an option: ").strip()

            if choice in self.games:
                self.games[choice].play()
            elif choice == "5":
                self.scoreboard.show_scores()
            elif choice == "6":
                print("Program exited. Goodbye!")
                break
            else:
                print("Invalid menu option.")


if __name__ == "__main__":
    menu = MainMenu()
    menu.show()