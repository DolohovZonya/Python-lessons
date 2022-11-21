import random as rd
class person():
  def __init__(self, name, health, speed, attack, defense, agility, critical_chance):
    try:
      self.name = name
      self.hp = float(health)
      self.spd = float(speed)
      self.att = attack
      self.defs = defense
      self.agility = float(agility)
      self.critical_chance = critical_chance
    except:
      raise ('compilation error')
  def damage_deal(self, other):
    spd1 = self.spd
    spd2 = other.spd
    if spd1 > spd2:
      other.hp = other.hp - (self.att - other.defs)
    if spd2 > spd1:
      self.hp = self.hp - (other.att - self.defs)
    return person(self.hp, other.hp)
  def evasion(self, other):
    ag1 = self.agility
    ag2 = other.agility
    if ag1 > rd.randint(0,100):
      self.hp = self.hp - 0
    if ag2 > rd.randint(0,100):
      other.hp = other.hp - 0
    return person(self.hp, other.hp)
  def critical_chance(self, other):
    cr1 = self.critical_chance
    cr2 = other.critical_chance
    if cr1 > rd.randint(0,100):
      other.hp = other.hp -2*(self.att - other.defs)
    if cr2 > rd.randint(0,100):
      self.hp = self.hp - 2*(other.att - self.defs)
    return person(self.hp, other.hp)
  def winner(self, other):
    if self.hp > other.hp:
      print(f"Winner: {self.name}")
    if other.hp > self.hp:
      print(f"Winner: {other.name}")
def battle():
  person1 = person("elf", 1, 3, 2, 3, 4, 3)
  person2 = person("dwarf", 1, 2, 4, 2, 1, 3)
  pers = person()
  for i in range(100):
    pers.damage_deal()
    pers.evasion()
    pers.critical_chance()
  print(pers.winner)
