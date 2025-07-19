from core.player import Player
from core.items import Items
from core.monster import Monsters
from utilities.log_system import log
from core.inventory import Inventory
from core.fight import Fight
import sys

#19-07-2025
#Reforger alpha

#@@IN-PROGRESS@@
# - damage calculation
# - saving system
# - eq system
# - inventory system
# - monster class
# - drop system
# - battle system
# - quest system
# - shop
# - durability system
# - status system (attack, defense, critical hit chance,hp)
# ***MAP***
# ***GATHERING SYSTEM***
# ***CRAFTING SYSTEM***
# ***LOG SYSTEM***



log.log("Game started", 0)


if __name__ == "__main__":
    # Example usage of Player class
    player = Player(name="Hero", health=150, level=1, experience=0, balance=200)
    
    # # Display player information
    # log.log(f"Player Name: {player.get_name()}",9)
    # log.log(f"Health: {player.get_health()}",9)
    # log.log(f"Level: {player.get_level()}",9)
    # log.log(f"Experience: {player.get_experience()}/{player.get_experience_need()}",9)
    # log.log(f"Balance: {player.get_balance()}",9)

    # Example usage of Items class
    items_list = Items()
    all_weapons = items_list.get_all_weapons()
    all_shields = items_list.get_all_shields()

    # log.log("Available Weapons:",9)
    # for weapon in all_weapons:
        # log.log(weapon,9)

    # log.log("Available Shields:",9)
    # for shield in all_shields:
        # log.log(shield,9)


# # Simulate gaining experience
#     player.add_experience(510)
#     # Display player information
#     log.log(f"Player Name: {player.get_name()}",9)
#     log.log(f"Health: {player.get_health()}",9)
#     log.log(f"Level: {player.get_level()}",9)
#     log.log(f"Experience: {player.get_experience()}/{player.get_experience_need()}",9)
#     log.log(f"Balance: {player.get_balance()}",9)

# Creating monster instance
    baza_potworow = Monsters()
    baza_potworow.load_monsters()
    potworek_1 = baza_potworow.get_monster_by_id(1)
    # log.log(f"Monster ID: {potworek_1.id}",2)
    # log.log(f"Monster Name: {potworek_1.name}",2)
    # print(log.get_logs_by_id(1))

    walka_pierwsza = Fight(player,potworek_1)
    walka_pierwsza.walka()

