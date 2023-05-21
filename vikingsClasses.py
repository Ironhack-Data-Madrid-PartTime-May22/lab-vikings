import random

# Soldier
class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self. strength = strength
    
    def attack(self):
        '''
        Returns the strength property of the Soldier
        '''
        return self.strength
    
    def receiveDamage(self, damage):
        '''
        Removes the received damage from the health property
        Receives 1 argument (the damage)
        '''
        self.health -= damage


# Viking
class Viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        '''
        Removes the received damage from the health property
        Receives 1 argument (the damage)
        If the Viking is still alive, it returns "NAME has received DAMAGE points of damage"
        If the Viking dies, it returns "NAME has died in act of combat"
        '''
        self.health -= damage

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        '''
        Returns "Odin Owns You All!"
        '''
        return 'Odin Owns You All!'


# Saxon
class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        '''
        Removes the received damage from the health property
        Receives 1 argument (the damage)
        If the Saxon is still alive, it returns "A Saxon has received DAMAGE points of damage"
        If the Saxon dies, it returns "A Saxon has died in combat"
        '''
        self.health -= damage

        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        
        else:
            return f'A Saxon has died in combat'

# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        '''
        Adds the received Viking to the army
        Receives 1 argument (a Viking object)
        '''
        self.vikingArmy.append(Viking)
        

    def addSaxon(self, Saxon):
        '''
        Adds the received Saxon to the army
        Receives 1 argument (a Saxon object)
        '''
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        '''
        Makes a Saxon receiveDamage() equal to the strength of a Viking
        Removes dead saxons from the army
        Returns result of calling receiveDamage() of a Saxon with the strength of a Viking
        '''
        if random.choice(self.saxonArmy).health <= 0:
            self.vikingArmy.remove(random.choice(self.saxonArmy))
        else:
            pass

        return random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).attack())

    def saxonAttack(self):
        '''
        Makes a Viking receiveDamage() equal to the strength of a Saxon
        Removes dead vikings from the army
        Returns result of calling receiveDamage() of a Viking with the strength of a Saxon
        '''
        if random.choice(self.vikingArmy).health <= 0:
            self.vikingArmy.remove(random.choice(self.vikingArmy))
        else:
            pass

        return random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).attack())

    def showStatus(self):
        '''
        If the Saxon array is empty, returns "Vikings have won the war of the century!"
        If the Viking array is empty, returns "Saxons have fought for their lives and survive another day..."
        If there are at least 1 Viking and 1 Saxon, returns "Vikings and Saxons are still in the thick of battle."
        '''
        if not any(self.saxonArmy):
            return 'Vikings have won the war of the century!'
        
        elif not any(self.vikingArmy):
            return 'Saxons have fought for their lives and survive another day...'
        
        else:
            return 'Vikings and Saxons are still in the thick of battle.'

