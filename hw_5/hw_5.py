class PlayerManager:

    def __init__(self):
        self.players = []

    def find_player(self, player_id):
        for player in self.players:
            if player[0] == player_id:
                return player
        return None

    def add_player(self, player_id, name, age):
        new_player = [player_id, name, age]
        self.players.append(new_player)

    def remove_player(self, player_id):
        for i, player in enumerate(self.players):
            if player[0] == player_id:
                del self.players[i]
                return True
        return False

    def update_player(self, player_id, new_name, new_age):
        for i, player in enumerate(self.players):
            if player[0] == player_id:
                player[1] = new_name
                player[2] = new_age
                return True
        return False

    def clear_data(self):
        self.players = []


def main():

    print(
        "Choose an action:"
        "\n1. Find player by ID"
        "\n2. Add player."
        "\n3. Remove player."
        "\n4. Update player information."
        "\n5. Clear all data."
        "\n6. Exit.\n"
    )

    manager = PlayerManager()

    while True:
        try:
            choice = int(input("\nEnter the action number: "))
            if choice == 1:
                player_id = int(input("Enter ID of the player to find: "))
                found_player = manager.find_player(player_id)
                if found_player:
                    print(f"Player found: {found_player}\n")
                else:
                    print(f"Player with ID {player_id} not found.\n")
            elif choice == 2:
                player_id = int(input("Enter player ID: "))
                name = input("Enter player name: ")
                age = int(input("Enter player age: "))
                manager.add_player(player_id, name, age)
            elif choice == 3:
                player_id = int(input("Enter ID of the player to remove: "))
                if manager.remove_player(player_id):
                    print("Player removed successfully.")
                else:
                    print(f"Player with ID {player_id} not found.\n")
            elif choice == 4:
                try:
                    player_id = int(
                        input("Enter ID of the player to update: ")
                    )
                    new_name = input("Enter new player name: ")
                    new_age = int(input("Enter new player age: "))
                    if manager.update_player(player_id, new_name, new_age):
                        print("Player information updated successfully.\n")
                except ValueError:
                    print(
                        "Invalid input. Please enter a valid number for ID and age.\n"
                    )
            elif choice == 5:
                manager.clear_data()
                print("Data deleted successfully!\n")
            elif choice == 6:
                print("Exiting program...\n")
                break
            else:
                print(
                    "Invalid choice. Please enter a number between 1 and 6.\n"
                )
        except ValueError:
            print("Invalid input.\n")


if __name__ == "__main__":
    main()
