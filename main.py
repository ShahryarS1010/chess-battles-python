class Player:
    name = ""
    health_points = 10
    max_health_points = 10
    energy_points = 5
    max_energy_points = 5
    attack_power = 2
    defense_power = 1

    items = []

    def set_name(self, name_input):
        self.name = name_input

    def get_name(self):
        return self.name

    def set_hp(self, hp):
        self.health_points = hp

    def hp_increase(self, hp):
        self.health_points += hp

        if self.health_points > self.max_health_points:
            self.health_points = self.max_health_points

    def hp_decrease(self, hp):
        self.health_points -= hp

        if self.health_points < 0:
            self.health_points = 0

    def get_hp(self):
        return self.health_points

    def set_ep(self, ep):
        self.energy_points = ep

    def ep_increase(self, ep):
        self.energy_points += ep

        if self.energy_points > self.max_energy_points:
            self.energy_points = self.max_energy_points

    def ep_decrease(self, ep):
        self.energy_points -= ep

        if self.energy_points < 0:
            self.energy_points = 0

    def get_ep(self):
        return self.energy_points

    def set_attack(self, attack):
        self.attack_power = attack

    def attack_increase(self, attack):
        self.attack_power += attack

    def get_attack(self):
        return self.attack_power

    def set_defense(self, defense):
        self.defense_power = defense

    def defense_increase(self, defense):
        self.defense_power += defense

    def get_defense(self):
        return self.defense_power

    def add_item(self, item):

        self.items.append(item)

    def remove_item(self, item):

        self.items.remove(item)

    def equipped(self, equip):

        if equip.get_updated_attack() > 0:
            self.attack_power *= equip.get_updated_attack()

        elif equip.get_updated_defense() > 0:
            self.defense_power *= equip.get_updated_defense()

    def fallen(self):

        if self.health_points == 0:
            return True
        else:
            return False


class Boss:
    name = ""
    health_points = 20
    max_health_points = 20
    attack_power = 4
    defense_power = 0

    def set_name(self, name_input):
        self.name = name_input

    def get_name(self):
        return self.name

    def set_hp(self, hp):
        self.health_points = hp

    def hp_increase(self, hp):
        self.health_points += hp

        if self.health_points > self.max_health_points:
            self.health_points = self.max_health_points

    def hp_decrease(self, hp):
        self.health_points -= hp

        if self.health_points < 0:
            self.health_points = 0

    def get_hp(self):
        return self.health_points

    def set_attack(self, attack):
        self.attack_power = attack

    def get_attack(self):
        return self.attack_power

    def set_defense(self, defense):
        self.defense_power = defense

    def get_defense(self):
        return self.defense_power

    def fallen(self):

        if self.health_points == 0:
            return True
        else:
            return False


class Item:
    name = ""
    hp_increase = 0
    ep_increase = 0
    attack_increase = 0
    defense_increase = 0

    def set_name(self, name_input):
        self.name = name_input

    def get_name(self):
        return self.name

    def update_stats(self, hp, ep, attack, defense):
        self.hp_increase = hp
        self.ep_increase = ep
        self.attack_increase = attack
        self.defense_increase = defense

    def get_updated_hp(self):
        return self.hp_increase

    def get_updated_ep(self):
        return self.ep_increase

    def get_updated_attack(self):
        return self.attack_increase

    def get_updated_defense(self):
        return self.defense_increase


print("Welcome to Chess Battles 1.0")
print("You will fight against 6 bosses, which are the Chess pieces (Pawn, Knight, Bishop, Rook, Queen, and King).")
print("For this version, you will only be fighting the pawn.")
print("Note: Your base attack and defense are 1 and 2 respectively while the boss's attack and defense are 4 and 0 respectively.")
print("The Red Apple restores 10 HP, while the Orange Carrot restores 5 EP.")

while True:

    player1 = Player()
    player1.set_name(input("Please enter your name: "))
    print("Hello " + player1.get_name())

    boss1 = Boss()
    boss1.set_name("Pawn")

    red_apple = Item()
    red_apple.set_name("Red Apple")
    red_apple.update_stats(10, 0, 0, 0)
    orange_carrot = Item()
    orange_carrot.set_name("Orange Carrot")
    orange_carrot.update_stats(0, 5, 0, 0)

    sword = Item()
    sword.set_name("Sword")
    sword.update_stats(0, 0, 2, 0)
    shield = Item()
    shield.set_name("Shield")
    shield.update_stats(0, 0, 0, 2)

    while True:
        item_list = [red_apple, orange_carrot]
        player1.add_item(red_apple)
        player1.add_item(orange_carrot)

        while True:

            print("What would you like to equip?")
            print("1: Sword (2 -> 4 Attack)")
            print("2: Shield (1 -> 2 Defense")

            while True:

                equipment_choice = int(input("Select Equipment: "))

                if equipment_choice == 1:

                    player1.equipped(sword)

                    break

                elif equipment_choice == 2:

                    player1.equipped(shield)

                    break

                else:

                    print("Error, Invalid Input.")

            print("Let's start the first battle.")

            break

        break

    def player_attack():

        print("Which move will you use?")
        print("1: Punch")
        print("2: Kick (2 EP) (+3 Attack)")

        while True:

            attack_choice = int(input("Select Action: "))

            if attack_choice == 1:

                boss1.hp_decrease(player1.get_attack() - boss1.get_defense())

                break

            if attack_choice == 2 and player1.get_ep() < 3:
                print("You do not have enough EP.")

            elif attack_choice == 2:

                player1.ep_decrease(2)

                boss1.hp_decrease(player1.get_attack() + 3)

                break

            else:

                print("Error, Invalid Input.")

        return

    def player_item():

        index = 1
        print("Which item will you use?")
        print("0: No Item, go to Move Selection")
        for i in item_list:
            print(str(index) + ": " + i.get_name())
            index += 1

        while True:

            item_choice = int(input("Select Item: "))

            if item_choice < 0 or item_choice > len(item_list):

                print("Error, Invalid Input.")

            elif item_choice == 0:

                player_attack()

                break

            else:

                player1.hp_increase(item_list[item_choice-1].get_updated_hp())
                player1.ep_increase(item_list[item_choice-1].get_updated_ep())
                player1.attack_increase(item_list[item_choice-1].get_updated_attack())
                player1.defense_increase(item_list[item_choice-1].get_updated_defense())

                player1.remove_item(item_list[item_choice-1])
                item_list.pop(item_choice-1)

                break

        return

    while True:

        print("[" + player1.get_name() + " Stats]" + " HP: " + str(player1.get_hp()) + " EP: " + str(player1.get_ep()))
        print("[" + boss1.get_name() + " Stats]" + " HP: " + str(boss1.get_hp()))
        print("What will you do " + player1.get_name() + "?")
        print("1: Attack")
        print("2: Item")
        print("3: Quit")

        while True:

            battle_choice = int(input("Select Action: "))

            if battle_choice == 1:

                player_attack()

                break

            elif battle_choice == 2 and len(item_list) == 0:

                print("You have no items.")

            elif battle_choice == 2:

                player_item()

                break

            elif battle_choice == 3:

                print("Thanks for Playing. Hope you see you in Version 2.0.")
                exit()

            else:

                print("Error, Invalid Input.")

                break

        if boss1.fallen():
            print("Boss has been defeated.")
            print("Congratulations.")
            break

        print (boss1.get_name() + " Attacks")
        player1.hp_decrease(boss1.get_attack() - player1.get_defense())

        if player1.fallen():
            print("Player health hits 0, Game Over.")
            break

    while True:

        play = input("Would you like to play again? (Y/N): ")

        if str(play) == "Y":

            break

        elif str(play) == "N":

            print("Thanks for Playing. Hope you see you in Version 2.0.")

            exit()

        else:

            print("Error, Invalid Input.")

