# Referee Class
class Referee:
    def __init__(self, referee_id, name, expertise_level):
        self.referee_id = referee_id
        self.name = name
        self.expertise_level = expertise_level
        self.availability = True

    def update_availability(self, availability):
        self.availability = availability

    def _str_(self):
        return f"{self.name} (Expertise Level: {self.expertise_level})"


# Game Class
class Game:
    def __init__(self, game_id, game_name):
        self.game_id = game_id
        self.game_name = game_name
        self.referees_assigned = []

    def assign_referee(self, referee):
        if referee.availability:
            self.referees_assigned.append(referee)
            referee.update_availability(False)
            print(f"Assigned {referee.name} to {self.game_name}")
        else:
            print(f"{referee.name} is not available")

    def list_referees(self):
        return ", ".join([ref._str_() for ref in self.referees_assigned])


# Feedback Class
class Feedback:
    def __init__(self, feedback_id, referee_id, comments):
        self.feedback_id = feedback_id
        self.referee_id = referee_id
        self.comments = comments

    def update_feedback(self, comments):
        self.comments = comments

    def _str_(self):
        return f"Feedback for Referee {self.referee_id}: {self.comments}"


# RefereeManager Class
class RefereeManager:
    def __init__(self):
        self.referees = {}

    def add_referee(self, referee):
        self.referees[referee.referee_id] = referee

    def remove_referee(self, referee_id):
        if referee_id in self.referees:
            del self.referees[referee_id]

    def update_referee(self, referee_id, availability):
        if referee_id in self.referees:
            self.referees[referee_id].update_availability(availability)


# GameManager Class
class GameManager:
    def __init__(self):
        self.games = {}

    def add_game(self, game):
        self.games[game.game_id] = game

    def assign_referees_to_game(self, game_id, referees):
        if game_id in self.games:
            game = self.games[game_id]
            for ref in referees:
                game.assign_referee(ref)

    def list_all_games(self):
        return {game_id: game.game_name for game_id, game in self.games.items()}


# FeedbackManager Class
class FeedbackManager:
    def __init__(self):
        self.feedback_list = {}

    def add_feedback(self, feedback):
        self.feedback_list[feedback.feedback_id] = feedback

    def update_feedback(self, feedback_id, comments):
        if feedback_id in self.feedback_list:
            self.feedback_list[feedback_id].update_feedback(comments)


### Function to Create a Referee from User Input
def create_referee_from_input():
    try:
        referee_id = int(input("Enter Referee ID: "))
        name = input("Enter Referee Name: ")
        expertise_level = int(input("Enter Expertise Level (1-10): "))

        # Create an instance of the Referee class with user inputs
        new_referee = Referee(referee_id, name, expertise_level)
        print(f"Referee Created: {new_referee}\n")
        return new_referee
    except ValueError:
        print("Invalid input! Please enter the correct values.")
        return None


### Function to Create a Game from User Input
def create_game_from_input():
    try:
        game_id = int(input("Enter Game ID: "))
        game_name = input("Enter Game Name: ")

        # Create an instance of the Game class with user inputs
        new_game = Game(game_id, game_name)
        print(f"Game Created: {new_game.game_name} (ID: {new_game.game_id})\n")
        return new_game
    except ValueError:
        print("Invalid input! Please enter the correct values.")
        return None


# Example to Add the Referee to the Manager and Assign to Different Types of Games
def main():
    referee_manager = RefereeManager()
    game_manager = GameManager()

    while True:
        print("\nMenu:")
        print("1. Create Referee")
        print("2. Create Game")
        print("3. Assign Referee to Game")
        print("4. List Referees in a Game")
        print("5. List All Games")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Create a referee and add to the referee manager
            new_referee = create_referee_from_input()
            if new_referee:
                referee_manager.add_referee(new_referee)

        elif choice == '2':
            # Create a game and add to the game manager
            new_game = create_game_from_input()
            if new_game:
                game_manager.add_game(new_game)

        elif choice == '3':
            # Assign a referee to a game
            if not referee_manager.referees:
                print("No referees available to assign!")
                continue
            if not game_manager.games:
                print("No games available to assign referees to!")
                continue

            # Select referee
            referee_id = int(input("Enter Referee ID to assign: "))
            if referee_id in referee_manager.referees:
                # List all games
                print("\nAvailable games:")
                games = game_manager.list_all_games()
                for game_id, game_name in games.items():
                    print(f"{game_id}: {game_name}")
                
                game_id = int(input("\nEnter Game ID to assign the referee to: "))
                if game_id in game_manager.games:
                    game_manager.assign_referees_to_game(game_id, [referee_manager.referees[referee_id]])
                else:
                    print("Game not found!")
            else:
                print("Referee not found!")

        elif choice == '4':
            # List referees in a specific game
            if not game_manager.games:
                print("No games available!")
                continue
            print("\nAvailable games:")
            games = game_manager.list_all_games()
            for game_id, game_name in games.items():
                print(f"{game_id}: {game_name}")
            
            game_id = int(input("\nEnter Game ID to list referees: "))
            if game_id in game_manager.games:
                game = game_manager.games[game_id]
                print(f"Referees assigned to {game.game_name}:")
                print(game.list_referees())
            else:
                print("Game not found!")

        elif choice == '5':
            # List all games
            games = game_manager.list_all_games()
            if not games:
                print("No games available!")
            else:
                print("All games:")
                for game_id, game_name in games.items():
                    print(f"{game_id}: {game_name}")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()