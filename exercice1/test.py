
from animal import Animal, Chien, Chat, Vache,Robot, faire_parler 

if __name__=="__main__":

     mon_chien = Chien()
     mon_chat = Chat()
     chien_voisin = Chien()
     ma_vache = Vache()

       

#Stocker tous les animaux dans une collection et les faire parler sans connaître leur type.
     animaux = [mon_chien, mon_chat, chien_voisin, ma_vache]
     for animal in animaux:
          faire_parler(animal)

#Démontrer l’utilisation de duck typing avec une classe Robot ayant aussi une méthode parler().
     mon_robot = Robot()
     faire_parler(mon_robot)