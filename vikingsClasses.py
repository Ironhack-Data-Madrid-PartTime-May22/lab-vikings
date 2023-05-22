
# Soldier


class Soldier:
    def __init__(self, health, strength):
       
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
   
    def receiveDamage(self, damage):
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, health, strength, name):
        Soldier.__init__(self, health, strength)
        
        self.strength = strength
        self.name = name
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health -= int(damage)
        
        if self.health > 0:
            return f"{self.name} ha recibido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en combate"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon:
    pass

# War


class War:
    pass
