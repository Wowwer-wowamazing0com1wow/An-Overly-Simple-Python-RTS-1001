import random as rand

class Building:
    def __init__(self, Alliance, location:list):
        self.location = location
        self.Alliance = Alliance
        self.state = "Undamaged"
        self.Level = 1
        self.Health = 50
        
    def LvlUp(self):
        self.Level += 1
    def damage(self,dmg):
        self.state = "Damaged"
        self.Health -= dmg
        if self.Health <= 0:
            self.destroy()
    def destroy(self):
        self.state = "Destroyed"
        
class Troop: 
    def __init__(self, Alliance, location):
        self.location = location
        self.Alliance = Alliance
        self.state = "Alive"
        self.level = 1
        self.Health = 20
        self.Attack = 1
    def damage(self,dmg):
        self.state = "Hurt"
        self.Health -= dmg
        if self.Health <= 0:
            self.destroy()
    def kill(self):
        self.state = "Dead"
    
class Castle(Building):
    def __init__(self, Alliance, location:list, Special:str):
        self.location = location
        self.Alliance = Alliance
        self.state = "Undamaged"
        self.Level = 1
        self.Health = 50
        self.SpawnTime = 10 
        self.Special = Special
        self.stats()
        self.SpawnTimer = 1 * self.SpawnTime
        self.Spawning = False
        self.SpawnType = ""
        
        self.Health += (self.Level*50)
        self.SpawnTime = 11 - self.Level
        if self.SpawnTime < 1:
            self.SpawnTime = 1
        self.update()
        
        
    def stats(self):
        return ("Health: " + str(self.Health) + ", Spawn Time: "+ str(self.SpawnTime))
        
    def SummonInit(self, choice):
        if choice == 1:
            self.SpawnType = "Builder"
            self.SpawnTimer = 2 * (self.SpawnTime/10)
            self.Spawning = True
        elif choice == 2:
            self.SpawnType = self.Special
            self.SpawnTimer = 2 * (self.SpawnTime/2)
            self.Spawning = True
        
    def update(self):
        if self.Spawning == True:
            self.SpawnTimer -= 1
        if self.SpawnTimer <= 0:
            self.SpawnTimer = 1
            self.Spawning = False
            self.Summon()
        
class Mine(Building):
    def __init__(self,Alliance):
        self.GPT = 10*self.Level
        
    def getGPT(self):
        return self.GPT
    def update(self):
        self.GPT = 10*self.Level
        
class Builder(Troop):
    def __init__(self, Alliance, location):
        self.location = location
        self.Alliance = Alliance
        self.state = "Alive"
        self.level = 1
        self.Health = 20
        self.Attack = 1
        self.Attack /= self.Attack/2
        