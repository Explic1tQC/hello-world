class Player:

    def __init__(self, pseudo, health, attack) :
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "/ Attaque", attack)

        def get_pseudo(self):
            return self.pseudo

        def get_health(self):
            return self.health

        def get_attack_value(self):
            return self_attack

        def damage(self, damage):
            self.health -= damage

        def attack_player(self, target_player):
            target_player.damage(self.attack)

class Warrior:

    def __init__(self, pseudo, health, attack) :
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.armor = 3
        print("Bienvenue au warrior", pseudo, "/ Attaque", attack)

        def get_pseudo(self):
            return self.pseudo

        def get_health(self):
            return self.health

        def get_attack_value(self):
            return self_attack

        def damage(self, damage):

            if self.armor > 0:
                self.armor -= 1
                damage = 0

            self.health -+ damage

        def attack_player(self, target_player):
            target_player.damage(self.attack)

        def blade(self):
            self.armor = 3
            print("Les points d'armure sont recharge")

        def get_armor_point(self):
            return self.armor



player = Player("Graven", 20, 2)
player.damage(3)

warrior = Warrior("Le guerrier de ouf", 30, 4)
warrior.damage(4)
print('Vie', warrior.get_health(), "Armure", warrior.get_armor_point())