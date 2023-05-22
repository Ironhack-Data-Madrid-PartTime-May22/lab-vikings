
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


class Viking():
    def __init__(self, health, strength, name):
        
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage
        
        if health > 0:
            return f"{name} ha recibido {damage} puntos de daño"
        else:
            return f"{name} ha muerto en combate"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon:
    pass

# War


class War:
    pass
