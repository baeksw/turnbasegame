
class Unit:
    hp = None
    mp = None
    level = 1
    normal_attack_dmg = None

    def attack(self, enemy_hp):
        pass

class Warrior(Unit):
    hp = 200

def test_attack_warrior_enemy():
    pass


if __name__ == '__main__':
    test_attack_warrior_enemy()