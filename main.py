#abstract class
from abc import ABC, abstractmethod

#class abstract BomboSapiens,hp,spd,jarak maju(),meledak(),berhenti()
class BomboSapiens(ABC):
      def __init__(self,hp,spd,jarak):
         self.hp = hp
         self.spd = spd
         self.jarak = jarak
      @abstractmethod
      def maju(self):
         pass
      @abstractmethod
      def meledak(self):
         pass
      @abstractmethod
      def berhenti(self):
         pass

#class abstract Senjata ammo,dmg,reload tembak(),reload()
class Senjata(ABC):
      def __init__(self,ammo,dmg,reload):
         self.ammo = ammo
         self.dmg = dmg
         self.reload = reload
      @abstractmethod
      def tembak(self):
         pass
      @abstractmethod
      def reloadf(self):
         pass

#class normalBombo inherit from BomboSapiens
class NormalBombo(BomboSapiens):
      def __init__(self,hp,spd,jarak):
         super().__init__(hp,spd,jarak)
      def maju(self):
         pass
      def meledak(self):
         pass
      def berhenti(self):
         pass

#class GiantBombo inherit from BomboSapiens
class GiantBombo(BomboSapiens):
      def __init__(self,hp,spd,jarak):
         super().__init__(hp,spd,jarak)   
      def maju(self):
         pass
      def meledak(self):
         pass
      def berhenti(self):
         pass

#class Glock inherit from Senjata tembak(),tembak2(),reload()
class Glock(Senjata):
      def __init__(self,ammo,dmg,reload):
         super().__init__(ammo,dmg,reload)   
      def tembak(self):
         pass
      def reload(self):
         pass

#class revolver inherit from Senjata boost(),mantul()
class Revolver(Senjata):
      def __init__(self,ammo,dmg,reload):
         super().__init__(ammo,dmg,reload)   
      def boost(self):
         pass
      def mantul(self):
         pass
      def tembak(self):
         pass
      def reload(self):
         pass

#class skill1 cost active()
class Skill1:
      def __init__(self,cost):
         self.cost = cost
      def active(self):
         pass

#class skill2 cost,charge,dmg active()
class Skill2:
      def __init__(self,cost,charge,dmg):
         self.cost = cost
         self.charge = charge
         self.dmg = dmg
      def active(self):
         pass
#class skill3 cost,area,dmg active()
class Skill3:
      def __init__(self,cost,area,dmg):
         self.cost = cost
         self.area = area
         self.dmg = dmg
      def active(self):
         pass