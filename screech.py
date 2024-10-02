# Define the rooms in the game and thier connections

rooms = {
    "hall": {
        "description": "You are in a grand hall with a chandelier overhead. There are doors to the north and east.",
        "north": "kitchen",
        "east": "living room",
        "item": "candle",
    },
    "kitchen": {
        "description": "You are in a small kitchen. There is a door to the south.",
        "south": "hall",
        "item": "magic book",
    },
    "living room": {
        "description": "You are in a cozy living room with a  fireplace. There is a door to the west.",
        "west": "hall",
    },
}

# Initialize player's inventory
inventory = []

# Player starts in the hall
current_room = "hall"

# Basic game loop
while True:
    # Print the current room description
    print(rooms[current_room]["description"])

    # If there's an item in the room, display it
    if "item" in rooms[current_room]:
        item_in_room = rooms[current_room]["item"]
        print(f"You see a {item_in_room} here.")

    # Get the player's input, show the item in the room if it exists
    if item_in_room:
        command = input(
            f"\nEnter a command: (north, south, east, west, take {item_in_room}, inventory, quit): "
        ).lower()
    else:
        command = input(
            "\nEnter a command: (north, south, east, west, inventory, quit): "
        ).lower()

    # Quit the game if the player enters 'quit'
    if command == "quit":
        print("Thanks for playing!")
        break

    # Check if the player is trying to take an item
    if command.startswith("take"):
        try:
            # Split the command, allowing for mulitple word items
            _, item_name = command.split(maxsplit=1)
        except ValueError:
            print("You must enter a valid item to take.")
            continue

        # Check if the item exists in the room
        if "item" in rooms[current_room] and item_name == rooms[current_room]["item"]:
            # Add the item to the player's inventory
            inventory.append(item_name)
            print(f"You take the {item_name}.")
            # Remove the item from the room
            del rooms[current_room]["item"]
        else:
            print(f"There is no {item_name} here to take.")

    # Check if the player wants to check their inventory
    elif command == "inventory":
        print("You are carrying: ", ", ".join(inventory) if inventory else "nothing")

    # Move to the next room if the command is valid
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
    else:
        print("\nYou shall not pass (you can't go that way).")
