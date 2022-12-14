from pandas.core.algorithms import SelectNFrame
import random as rd

class hero(): 
  #инициализация героев и их параметров
  def __init__(self, name, health, speed, attack, defense, agility, critical_chance):
    try:
      self.name = name
      self.hp = float(health)
      self.spd = float(speed)
      self.att = attack
      self.defs = defense
      self.ag = float(agility)
      self.critical = critical_chance
      self.i = 100
      self.hero = 1
      self.ko = 0
      self.init_hp = self.hp
    except:
      raise ('compilation error')
  #уклонение героя (возвращает тру если герой уклонился)
  def evasion(self):
    return self.ag > rd.randint(0,99)
    #return other.ag > rd.randint(0,100)
  #критический удар (возвращает тру, если герой способен нанести двойной урон противнику)
  def critical_chance(self):
    return self.critical > rd.randint(0, 99)
    #return other.critical > rd.randint(0, 100)
  #функция нанесения урона (пытаюсь сделать ее с учетом уклонения и с учетом критического удара)
  def starting_punch(self, other):
      if self.spd > other.spd:
        self.hero = 1
      elif other.spd > self.spd:
        self.hero = 2
      elif self.spd == other.spd:
        self.hero = 1
      #print(self.hero)
      return self.hero
  def damage_deal(self, other):
    self.hero = hero.starting_punch(self, other)
    while self.hp > 0 and other.hp > 0:
      if self.hero == 1:
        if hero.evasion(other):
          other.hp += 0
        else:
          if hero.critical_chance(self):
            other.hp = other.hp - 2*(self.att - other.defs)
          else:
            other.hp -= self.att - other.defs
        self.hero = 2
      if self.hero == 2:
        if hero.evasion(self):
          self.hp += 0
        else:
          if hero.critical_chance(other):
            self.hp = self.hp - 2*(other.att - self.defs)
          else:
            self.hp -= other.att - self.defs
        self.hero = 1
      #print(str(self.hp) + '  ' + str(other.hp))
      if self.hp <= 0:
        other.ko += 1
      elif other.hp <= 0:
        self.ko += 1
    self.hp = self.init_hp
    other.hp = other.init_hp
  def battle(self, other):
    for i in range(100):
      hero.damage_deal(self,other)
    print(self.ko, other.ko)
    if self.ko > other.ko:
      print("Winner is " + str(self.name))
    elif other.ko > self.ko:
      print("Winner is " + str(other.name))
#экземпляры класса - два борющихся друг с другом героя с разными жизненными характеристиками
pers1 = hero("elf", 10, 1, 2, 1, 50, 50)
pers2 = hero("dwarf", 10, 1, 2, 1, 50, 50)
pers1.battle(pers2)
