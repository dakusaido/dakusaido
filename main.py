import random

path = 'base.txt'


def read_file():
    with open(path) as file:
        return eval(file.read())


class Base:

    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
        self._ability = read_file()

    @staticmethod
    def remake(type_player, ability, dictionary):
        value = dictionary[type_player]
        for kj in range(len(value)):
            for y in range(len(value[kj])):
                if value[kj][y] == ability:
                    return value[kj][0]
        return 0

    def hit_player(self, hit_player, hit_player_ability):
        damage_point = self.remake(hit_player, hit_player_ability, self._ability)
        if self.armor > 0:
            self.health -= round(damage_point * 0.7)
        else:
            self.health -= damage_point
        # print(self.health, self.__class__.__name__)

    def stealing_mana(self, ability, player_mana):
        value = read_file()[self.__class__.__name__]
        lst = [value[xq][-1] for xq in range(len(value)) for y in range(len(value[xq])) if value[xq][y] == ability]
        player_mana -= int(lst[0])
        # print(player_mana, self.__class__.__name__)


class Ork(Base):

    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)
        self.mana = 100

    def hit_ork(self, hit_player, hit_player_ability):
        self.hit_player(hit_player, hit_player_ability)


class Wizard(Base):

    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)
        self.mana = 300

    def hit_wizard(self, hit_player, hit_player_ability):
        self.hit_player(hit_player, hit_player_ability)


class Archer(Base):

    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)
        self.mana = 100

    def hit_archer(self, hit_player, hit_player_ability):
        self.hit_player(hit_player, hit_player_ability)


def random_ability(player):
    value = read_file()[player]
    lst = [value[i][y] for i in range(len(value)) for y in range(len(value[i])) if not str(value[i][y]).isdigit()]
    key = lst[random.randint(0, len(lst) - 1)]
    # print(key)
    return key


def return_name_player(name):
    if name == 'player_ork':
        return 'Ork'
    elif name == 'player_wizard':
        return 'Wizard'
    elif name == 'player_archer':
        return 'Archer'


# player_ork = Ork('asd', 200, 200)  # Creating an Orc Unit
# player_wizard = Wizard('qwe', 100, 100)  # Creating Wizard Unit
# player_archer = Archer('zxc', 100, 60)  # Creating Archer unit
#
# player_ork.hit_ork('Archer', random_ability('Archer'))  # Hit Ork(Unit, ability)
# player_wizard.hit_wizard('Ork', random_ability('Ork'))  # Hit Wizard(Unit, ability)
# player_archer.hit_archer('Wizard', random_ability('Wizard'))  # Hit Archer(Unit, ability)
#
# player_archer.stealing_mana('Hail of arrows', player_archer.mana)  # Stealing mana Archer(ability, player mana)
# player_wizard.stealing_mana('Flame', player_wizard.mana)  # Stealing mana Wizard(ability, player mana)
# player_ork.stealing_mana('Double strike', player_ork.mana)  # Stealing mana Ork(ability, player mana)

if __name__ == '__main__':
    list_player = ['player_ork', 'player_wizard', 'player_archer']
    player_ork = Ork('Orkinshtein', 200, 100)  # Creating an Orc Unit
    player_wizard = Wizard('Shaman', 100, 100)  # Creating Wizard Unit
    player_archer = Archer('Archer', 200, 150)  # Creating Archer unit
    get_damage_player = None
    moves = 0
    while True:
        moves += 1
        rubbish_lst = []
        random_attack_player = list_player[random.randint(0, 2)]
        for x in list_player:
            if x != random_attack_player:
                rubbish_lst.append(x)
        get_damage_player = rubbish_lst[random.randint(0, 1)]
        # print(random_attack_player, get_damage_player)
        if player_ork.health > 0 and player_archer.health > 0 and player_wizard.health > 0:
            if get_damage_player == 'player_ork':
                player_ork.hit_ork(return_name_player(random_attack_player),
                                   random_ability(return_name_player(random_attack_player)))
            elif get_damage_player == 'player_wizard':
                player_wizard.hit_wizard(return_name_player(random_attack_player),
                                         random_ability(return_name_player(random_attack_player)))
            elif get_damage_player == 'player_archer':
                player_archer.hit_archer(return_name_player(random_attack_player),
                                         random_ability(return_name_player(random_attack_player)))
        else:
            min_health = min(player_archer.health, player_ork.health, player_wizard.health)
            aa = 0

            # Polymorphism
            for count in [player_ork, player_wizard, player_archer]:
                if count.health == min_health:
                    print(f'{count.name} is lose! {moves} moves')
                    break
            break
