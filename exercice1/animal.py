class Animal :
     def parler(self):
          raise NotImplementedError("La méthode parler doit être implémentée par les sous-classes.")



#sous classes 
#chien
class Chien (Animal):
     def parler(self):
          return "Woof!"



#chat
class Chat (Animal):
     def parler(self):
          return "Meow!"


#vache
class Vache (Animal):
     def parler(self):
          return "Moo!"



class Robot:
     def parler(self):
          return "Beep Boop!"

def faire_parler(animal):
     print(animal.parler())
