from forme import *
if __name__ == "__main__":
    
     cercle = Cercle(5)
     rectangle = Rectangle(4, 6)
     triangle = Triangle(3, 4)
     carre = Carre(4)

     formes = [cercle, rectangle, triangle, carre]

     for forme in formes:
          print(forme)
          print(f"Aire: {forme.aire()}")
     