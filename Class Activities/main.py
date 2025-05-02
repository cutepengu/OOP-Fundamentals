from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character1 = Player("'Melody', 'Elf', 'Conquerer', '8', '50'")
player_character2 = Player("'Guhm', 'Golem', 'Tanker', '12', '300'")
player_character3 = Player("'Bob', 'Human', 'Fighter', '2', '20'")
player_character4 = Player("'Gabriel', 'Angel', 'Healer', '6', '250'")

# TODO: Create an instance of Weapon with random damage between 12 and 15
player_weapon = Weapon("'12', '13', '14', '15'")

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
player_enemy = Enemy(random.randint(15, 18))

# Print the player character details
print(f"Player Name: {player_character1.name}")
print(f"Player Race: {player_character1.race}")
print(f"Player Class: {player_character1.cls}")
print(f"Player Attack: {player_character1.atk}")
print(f"Player Health: {player_character1.health}")

# TODO: Print the player weapon details
print(f"Player Weapon: {player_weapon.name}")
print(f"Player Category: {player_weapon.cat}")
print(f"Player Damage: {player_weapon.dmg}")

# TODO: Print the enemy character details
print(f"Enemy Name: {player_enemy.name}")
print(f"Enemy Race: {player_enemy.race}")
print(f"Enemy Damage: {player_enemy.dmg}")
print(f"Enemy Health: {player_enemy.health}")