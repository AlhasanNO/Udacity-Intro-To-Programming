"""A simple text-based adventure game where the player fights enemies."""

import time
import random


def get_random_enemy():
    """Return a random enemy from the list."""
    enemies = ["pirate", "troll", "goblin"]
    return random.choice(enemies)


def get_random_weapon():
    """Return a random weapon from the list."""
    weapons = ["sword", "bow", "dagger"]
    return random.choice(weapons)


def print_pause(message, delay=2):
    """
    Print a message and pause for two sec.

    Args:
        message (str): The message to print.
        delay (int): Time to pause in seconds.
    """
    print(message)
    time.sleep(delay)


def combat(player_weapon, enemy):
    """
    Simulate combat between the player and the enemy.

    Args:
        player_weapon (str): The weapon the player is using.
        enemy (str): The type of enemy being fought.

    Returns:
        str: The result of the battle ("win", "lose", or "tie").
    """
    player_damage = random.randint(5, 15)
    enemy_damage = random.randint(5, 15)
    print_pause(
        f"You attack the {enemy} with your {player_weapon}, "
        f"dealing {player_damage} damage."
    )
    print_pause(
        f"The {enemy} strikes back, dealing {enemy_damage} damage to you."
    )

    if player_damage > enemy_damage:
        return "win"
    elif player_damage < enemy_damage:
        return "lose"
    else:
        return "tie"


def scene(weapon):
    """
    Discripe initial game scene to the player.

    Args:
        weapon (str): The weapon the player is holding.
    """
    print_pause(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a wicked fairie is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your {weapon}.")


def player_choice(choice):
    """
    Handle the player's choice of action.

    Args:
        choice (str): The player's input choice ("1" or "2").
    """
    if choice == "1":
        print_pause(
            "You knock on the door. A strange voice calls out, "
            "'Who dares disturb me?'"
        )
    elif choice == "2":
        print_pause(
            "You peer into the cave and see glowing eyes staring back at you!"
        )
    else:
        print("Invalid input.")


def play_again():
    """
    Ask if the playew wants to play again.

    Returns:
        bool: True if the player wants to play again, False if he dont.
    """
    while True:
        response = input("Would you like to play again? (y/n) ").lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def start_game():
    """Start the game."""
    enemy = get_random_enemy()
    weapon = get_random_weapon()
    scene(weapon)
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")

    while True:
        choice = input("What would you like to do? (Please enter 1 or 2): ")
        player_choice(choice)

        print_pause(f"You encounter a fearsome {enemy}!")
        print_pause(f"You ready your {weapon} for battle.")

        result = combat(weapon, enemy)
        if result == "win":
            print_pause("You win the battle and the game!")
        elif result == "lose":
            print_pause("You have been defeated. You lose the game.")
        else:
            print_pause("The battle is a tie.")

        if play_again():
            start_game()
        else:
            print_pause("Thank you for playing!")
            break


start_game()
