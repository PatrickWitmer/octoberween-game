# Text Adventure Game

# Initialize inventory and current room
inventory = []
current_room = "Hall"

# Define rooms with descriptions, items, and puzzles
rooms = {
    "Hall": {
        "description": "You are in a dimly lit hall, shadows dance on the walls as you hear a faint whispering.",
        "north": "Library",
        "south": "Kitchen",
        "item": "ancient key",
    },
    "Library": {
        "description": "The library is filled with dusty old books. A large tome lies open on the table, and you feel a chill.",
        "south": "Hall",
        "item": "magic book",
        "puzzle_solved": False,  # Track if the puzzle has been solved
        "riddle": "What has keys but can't open locks?",
        "answer": "piano",  # Correct answer
    },
    "Kitchen": {
        "description": "The kitchen smells of decay. An old fridge stands against the wall, slightly ajar.",
        "north": "Hall",
        "item": "rusty knife",
    },
}


def describe_current_room():
    """Prints the description of the current room and any items present."""
    room = rooms[current_room]
    print(room["description"])
    if room["item"]:
        print(f"You see a {room['item']} here.")


def take_item(item_name):
    """Allows the player to take an item from the current room."""
    room = rooms[current_room]

    # Check if the item exists in the room
    if item_name == room["item"]:
        inventory.append(item_name)
        room["item"] = None  # Remove item from room after taking
        print(f"You have taken the {item_name}.")
    else:
        print(f"There is no {item_name} here.")


def attempt_puzzle():
    """Allows the player to attempt solving the puzzle in the Library."""
    if current_room == "Library" and not rooms["Library"]["puzzle_solved"]:
        print(rooms["Library"]["riddle"])
        answer = input("Enter your answer: ").strip().lower()

        if answer == rooms["Library"]["answer"]:
            print(
                "Correct! The hidden compartment opens, revealing a powerful spell scroll."
            )
            rooms["Library"]["puzzle_solved"] = True  # Mark the puzzle as solved
            inventory.append(
                "spell scroll"
            )  # Add the new item to the player's inventory
        else:
            print("That's not correct. Try again.")


def show_inventory():
    """Displays the player's current inventory."""
    if inventory:
        print("You are carrying: " + ", ".join(inventory))
    else:
        print("Your inventory is empty.")


while True:
    describe_current_room()  # Describe the current room
    command = (
        input(
            "Enter your command (e.g., 'take [item]', 'solve puzzle', 'go [direction]', 'inventory', 'quit'): "
        )
        .strip()
        .lower()
    )

    if command.startswith("take "):
        item_name = command[5:]  # Get the entire input after "take "
        take_item(item_name)  # Call the function to take an item
    elif command == "solve puzzle":
        attempt_puzzle()  # Call the puzzle attempt function
    elif command.startswith("go "):
        direction = command[3:]  # Get the direction after "go "
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.")
    elif command == "inventory":
        show_inventory()  # Call the function to show the inventory
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print(
            "Invalid command. Try 'take [item]', 'solve puzzle', 'go [direction]', 'inventory', or 'quit'."
        )
