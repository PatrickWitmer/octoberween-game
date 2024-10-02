# Define the rooms in the game and thier connections

rooms = {
    "Hall": {
        "description": "\nYou are in a dimly lit hall, shadows dance on the walls as you hear a faint whispering.",
        "north": "Library",
        "south": "Kitchen",
        "item": "ancient key",
    },
    "Library": {
        "description": "\nThe library is filled with dusty old books. A large tome lies open on the table, and you feel a chill.",
        "south": "Hall",
        "item": "magic book",
        "puzzle_solved": False,  # Track if the puzzle has been solved
        "riddle": "\nA voice whispers to you, wwwhat has keys but can't open locks?",
        "answer": "piano",  # Correct answer
    },
    "Kitchen": {
        "description": "\nThe kitchen smells of decay. An old fridge stands against the wall, slightly ajar.",
        "north": "Hall",
        "item": "rusty knife",
    },
}


# Initialize player's inventory
inventory = []

# Player starts in the hall
current_room = "Hall"


def attempt_puzzle():
    if current_room == "Library" and not rooms["Library"]["puzzle_solved"]:
        print(rooms["Library"]["riddle"])
        answer = input("Enter the answer: ").strip().lower()
        if answer == rooms["Library"]["answer"]:
            print(
                "\nCorrect! The hidden compartment opens, revealing a powerful spell scroll."
            )
            rooms["Library"]["puzzle_solved"] = True  # Mark the puzzle as solved
            inventory.append("spell scroll")
        else:
            print("\nIncorrect. The compartment remains closed.")


# Basic game loop
while True:
    # Print the current room description
    print(rooms[current_room]["description"])

    # If there's an item in the room, display it
    if "item" in rooms[current_room]:
        item_in_room = rooms[current_room]["item"]
        print(f"\nYou see a {item_in_room} here.")

    # Get the player's input, show the item in the room if it exists
    if item_in_room:
        command = input(
            f"\nEnter a command: (north, south, east, west, take {item_in_room}, inventory, solve puzzle, quit): "
        ).lower()
    else:
        command = input(
            "\nEnter a command: (north, south, east, west, inventory, quit): "
        ).lower()

    # Quit the game if the player enters 'quit'
    if command == "quit":
        print("\nThanks for playing!")
        break

    # Check if the player is trying to take an item
    if command.startswith("take"):
        try:
            # Split the command, allowing for mulitple word items
            _, item_name = command.split(maxsplit=1)
        except ValueError:
            print("\nYou must enter a valid item to take.")
            continue

        # Check if the item exists in the room
        if "item" in rooms[current_room] and item_name == rooms[current_room]["item"]:
            # Add the item to the player's inventory
            inventory.append(item_name)
            print(f"\nYou take the {item_name}.")
            # Remove the item from the room
            del rooms[current_room]["item"]
        else:
            print(f"\nThere is no {item_name} here to take.")

    # Check if the player wants to check their inventory
    elif command == "inventory":
        print("\nYou are carrying: ", ", ".join(inventory) if inventory else "nothing")

    elif command == "solve puzzle":
        attempt_puzzle()  # Call the puzzle attempt function
    # Move to the next room if the command is valid
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
    else:
        print("\nYou shall not pass (you can't go that way).")
