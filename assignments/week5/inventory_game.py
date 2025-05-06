inventory = []
MAX_ITEMS = 5

rooms = {
    "Forest Entrance": [
        {"name": "Wooden Knife", "type": "tool"},
        {"name": "Deer Tracks", "type": "track"},
        {"name": "Bow and Arrows", "type": "tool"},
        {"name": "Berries", "type": "food"}
    ],
    "Hunting Grounds": [
        {"name": "Deer", "type": "prey", "health": 10},
        {"name": "Fish", "type": "prey", "health": 5}
    ],
    "Supply Station": [
        {"name": "First Aid Kit", "type": "healing", "uses": 1},
        {"name": "Apple", "type": "food"},
        {"name": "Water Bottle", "type": "food"},
        {"name": "Axe", "type": "tool"},
        {"name": "Rations", "type": "food"},
        {"name": "Trap", "type": "tool"}
    ]
}

current_room = "Forest Entrance"
escaped = False

# Show items in the current room
def show_room_items():
    print(f"Items in [{current_room}]:")
    items = rooms[current_room]
    if not items:
        print("- None")
    else:
        for item in items:
            print(f"- {item['name']} ({item['type']})")

def show_rooms():
    print("\nAvailable rooms to move to:")
    for room in rooms:
        if room != current_room:
            print(f"- {room}")

def show_inventory():
    print("🎒 Current Inventory:")
    if not inventory:
        print("- Empty")
    else:
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")

def pick_up(item_name):
    global inventory
    if len(inventory) >= MAX_ITEMS:
        print("❌ Inventory is full. You need to drop an item.")
        return
    for item in rooms[current_room]:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            rooms[current_room].remove(item)
            print(f"✅ '{item['name']}' added to your inventory.")
            return
    print(f"❌ '{item_name}' is not in this room.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room].append(item)
            print(f"🗑️ '{item['name']}' dropped.")
            return
    print(f"❌ You don't have '{item_name}' in your inventory.")

def use(item_name):
    global current_room, escaped
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["name"] == "Wooden Knife" and current_room == "Hunting Grounds":
                print("🪓 Using the Wooden Knife to hunt a Deer!")
                rooms["Hunting Grounds"].remove({"name": "Deer", "type": "prey", "health": 10})
                print("🎯 You hunted a Deer and gained some meat!")
                return
            elif item["name"] == "Bow and Arrows" and current_room == "Hunting Grounds":
                print("🏹 Using Bow and Arrows to hunt a Deer!")
                rooms["Hunting Grounds"].remove({"name": "Deer", "type": "prey", "health": 10})
                print("🎯 You successfully hunted a Deer with your Bow and Arrows!")
                return
            elif item["type"] == "healing":
                if "uses" in item and item["uses"] > 0:
                    item["uses"] -= 1
                    print(f"💊 Used '{item['name']}'. (Remaining uses: {item['uses']})")
                    if item["uses"] == 0:
                        inventory.remove(item)
                        print(f"'{item['name']}' is used up and disappeared.")
                    return
            elif item["type"] == "food":
                print(f"🍴 '{item['name']}' eaten for some energy!")
                inventory.remove(item)
                return
            elif item["name"] == "Water Bottle":
                print("💧 Drinking the Water Bottle to quench your thirst!")
                inventory.remove(item)
                return
            elif item["name"] == "Rations":
                print("🍖 Eating the Rations to recover energy!")
                inventory.remove(item)
                return
            elif item["name"] == "Trap":
                print("🔧 Setting up a trap to catch prey!")
                rooms["Hunting Grounds"].append({"name": "Rabbit", "type": "prey", "health": 5})
                return
            else:
                print(f"🔧 '{item['name']}' cannot be used right now.")
                return
    print(f"❌ '{item_name}' is not in your inventory.")

def examine(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            print(f"🔍 You examined '{item['name']}'. Type: {item['type']}")
            return
    print(f"❌ '{item_name}' is not in your inventory.")

def handle_command(command):
    global escaped
    global current_room
    if command == "":
        return
    parts = command.lower().split()
    if parts[0] == "help":
        print("📜 Available commands:")
        print("inventory, pickup [item], drop [item], use [item], examine [item], look, move [room], quit")
    elif parts[0] == "inventory":
        show_inventory()
    elif parts[0] == "pickup":
        if len(parts) < 2:
            print("❌ You need to specify the item name to pick up. For example, 'pickup Wooden Knife'.")
        else:
            pick_up(" ".join(parts[1:]))
    elif parts[0] == "drop":
        if len(parts) < 2:
            print("❌ You need to specify the item name to drop. For example, 'drop Wooden Knife'.")
        else:
            drop(" ".join(parts[1:]))
    elif parts[0] == "use":
        if len(parts) < 2:
            print("❌ You need to specify the item name to use. For example, 'use First Aid Kit'.")
        else:
            use(" ".join(parts[1:]))
    elif parts[0] == "examine":
        if len(parts) < 2:
            print("❌ You need to specify the item name to examine. For example, 'examine Wooden Knife'.")
        else:
            examine(" ".join(parts[1:]))
    elif parts[0] == "look":
        show_room_items()
        show_rooms()  # Show available rooms after showing items
    elif parts[0] == "move":
        move_to = " ".join(parts[1:])
        if move_to in rooms:
            current_room = move_to
            print(f"🚶‍♀️ You moved to '{move_to}'.")
        else:
            print("❌ This room doesn't exist.")
    elif parts[0] == "quit":
        escaped = True
    else:
        print("❓ Unknown command. Type 'help' for a list of commands.")

print(f"\nIn the '{current_room}', you can find the following items:")
show_room_items()
print("\n Survive in the hunting grounds and gather resources to escape! Type 'help' for instructions.")

while not escaped:
    command = input("\n>>> ")
    handle_command(command)

print("\n🎉 The game has ended!")
