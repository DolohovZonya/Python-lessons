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
    except:
      raise ('compilation error')
  #уклонение героя (возвращает тру если герой уклонился)
  def evasion(self):
    return self.ag > rd.randint(0,100)
    #return other.ag > rd.randint(0,100)
  #критический удар (возвращает тру, если герой способен нанести двойной урон противнику)
  def critical_chance(self):
    return self.critical > rd.randint(0, 100)
    #return other.critical > rd.randint(0, 100)
  #функция нанесения урона (пытаюсь сделать ее с учетом уклонения и с учетом критического удара)
  def damage_deal(self, other):
      if self.spd > other.spd:
        if hero.evasion(self):
          other.hp += 0
        else:
          if hero.critical_chance(self):
            other.hp = other.hp - 2*(self.att - other.defs)
          else:
            other.hp -= self.att - other.defs
        self.hero = 1
      elif other.spd > self.spd:
        if hero.evasion(other):
          self.hp += 0
        else:
          if hero.critical_chance(other):
            self.hp = self.hp - 2*(other.att - self.defs)
          else:
            self.hp -= other.att - self.defs
        self.hero = 2
      elif self.spd == other.spd:
        if hero.evasion(self):
          other.hp += 0
        else:
          if hero.critical_chance(self):
            other.hp = other.hp - 2*(self.att - other.defs)
          else:
            other.hp -= self.att - other.defs
        self.hero = 1
      #print(self.hero)
      while self.i > 1:
        if self.hero == 1:
          if hero.evasion(self):
            other.hp += 0
          else:
            if hero.critical_chance(self):
              other.hp = other.hp - 2*(self.att - other.defs)
            else:
              other.hp -= self.att - other.defs
          self.hero = 2
        if self.hero == 2:
          if hero.evasion(other):
            self.hp += 0
          else:
            if hero.critical_chance(other):
              self.hp = self.hp - 2*(other.att - self.defs)
            else:
              self.hp -= other.att - self.defs
          self.hero = 1
        self.i -= 1
        if self.hp < 0:
          print("Winner is " + str(other.name))
          break
        elif other.hp < 0:
          print("Winner is " + str(self.name))
          break
#экземпляры класса - два борющихся друг с другом героя с разными жизненными характеристиками
pers1 = hero("elf", 100, 5, 51, 6, 54, 8)
pers2 = hero("dwarf", 100, 5, 34, 29, 68, 7)
pers1.damage_deal(pers2)
pers2.damage_deal(pers1)
