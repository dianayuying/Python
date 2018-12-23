"""
Create a class called Warrior which calculates and keeps track of their level and skills, and ranks them as the warrior they've proven to be.

Business Rules:

    A warrior starts at level 1 and can progress all the way to 100.
    A warrior starts at rank "Pushover" and can progress all the way to "Greatest".
    The only acceptable range of rank values is "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest".
    Warriors will compete in battles. Battles will always accept an enemy level to match against your own.
    With each battle successfully finished, your warrior's experience is updated based on the enemy's level.
    The experience earned from the battle is relative to what the warrior's current level is compared to the level of the enemy.
    A warrior's experience starts from 100. Each time the warrior's experience increases by another 100, the warrior's level rises to the next level.
    A warrior's experience is cumulative, and does not reset with each rise of level. The only exception is when the warrior reaches level 100, with which the experience stops at 10000
    At every 10 levels, your warrior will reach a new rank tier. (ex. levels 1-9 falls within "Pushover" tier, levels 80-89 fall within "Champion" tier, etc.)
    A warrior cannot progress beyond level 100 and rank "Greatest".
    Battle Progress Rules & Calculations:

    If an enemy level does not fall in the range of 1 to 100, the battle cannot happen and should return "Invalid level".
    Completing a battle against an enemy with the same level as your warrior will be worth 10 experience points.
    Completing a battle against an enemy who is one level lower than your warrior will be worth 5 experience points.
    Completing a battle against an enemy who is two levels lower or more than your warrior will give 0 experience points.
    Completing a battle against an enemy who is one level higher or more than your warrior will accelarate your experience gaining. The greater the difference between levels, the more experinece your warrior will gain. The formula is 20 * diff * diff where diff equals the difference in levels between the enemy and your warrior.
    However, if your warrior is at least one rank lower than your enemy, and at least 5 levels lower, your warrior cannot fight against an enemy that strong and must instead return "You've been defeated".
    Every successful battle will also return one of three responses: "Easy fight", "A good fight", "An intense fight". Return "Easy fight" if your warrior is 2 or more levels higher than your enemy's level. Return "A good fight" if your warrior is either 1 level higher or equal to your enemy's level. Return "An intense fight" if your warrior's level is lower than the enemy's level.
"""
class Warrior():
    ranking = {0:"Pushover",1:"Novice",2:"Fighter",3:"Warrior",4:"Veteran",
    5:"Sage",6:"Elite",7:"Conqueror", 8:"Champion", 9:"Master", 10:"Greatest"}
    def __init__(self):
        self.level = 1
        self.rank = "Pushover"
        self.experience = 100
        self.achievements=[]

    def training(self, desc_list):
        if desc_list[2]>self.level:
            return "Not strong enough"
        else:
            self.achievements.append(desc_list[0])
            if self.experience+desc_list[1]>10000:
                self.experience=10000
            else:
                self.experience +=desc_list[1]
        
            self.level=int(self.experience/100)
            self.rank=Warrior.ranking[int(self.level/10)]
            return desc_list[0]
    
    def battle(self, n):
        if n<1 or n>100:
            return "Invalid level"
        else:
            diff = n-self.level
            if n==self.level:
                self.experience +=10
            elif n==self.level-1:
                self.experience +=5
            elif n>self.level:
                if n>=self.level+5 and int(n/10)>=int(self.level/10)+1:
                    return "You've been defeated"
                else:
                    self.experience += 20*((n-self.level)**2)
        if self.experience>10000:
            self.experience=10000
        self.level=int(self.experience/100)
        self.rank=Warrior.ranking[int(self.level/10)]
        if diff<=-2: return "Easy fight"
        elif diff==-1 or diff==0: return "A good fight"
        else: return "An intense fight"
      
        