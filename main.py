class Calculatrice:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 0 

    def addition(self):
       self.c=self.a+self.b
       print(f"{self.a}+{self.b}={self.c}\n")

    def soustraction(self):
       self.c=self.a-self.b
       print(f"{self.a}-{self.b}={self.c}\n")   

    def multiplication(self):
       self.c=self.a*self.b
       print(f"{self.a}X{self.b}={self.c}\n")

    def division(self):
       self.c=self.a/self.b
       print(f"{self.a}/{self.b}={self.c}\n")

    def puissance(self):
       self.c=self.a**self.b
       print(f"{self.a}^{self.b}={self.c}\n")

def afficher_menu():
    print("calculatrice")
    print("1. addition")
    print("2. soustraction")
    print("3. multiplication")
    print("4. division")
    print("5. puissance")
    print("0. Quitter")


while True:
    afficher_menu()
    choix = int(input("entrz un choix \n"))
    if choix==1:
        nombre1= int(input("entrez votre premier nombre\n"))
        nombre2= int(input("entrez votre deuxieme nombre\n"))
        calculatrice=Calculatrice(nombre1,nombre2)
        calculatrice.addition()

    elif choix==2:
        nombre1= int(input("entrez votre premier nombre\n"))
        nombre2= int(input("entrez votre deuxieme nombre\n"))
        calculatrice=Calculatrice(nombre1,nombre2) 
        calculatrice.soustraction()
    elif choix==3:
        nombre1= int(input("entrez votre premier nombre\n"))
        nombre2= int(input("entrez votre deuxieme nombre\n"))
        calculatrice=Calculatrice(nombre1,nombre2)
        calculatrice.multiplication()

    elif choix==4:
        nombre1= int(input("entrez votre premier nombre\n"))
        nombre2= int(input("entrez votre deuxieme nombre\n"))
        calculatrice=Calculatrice(nombre1,nombre2)  
        calculatrice.division()  

    elif choix==5:
        nombre1= int(input("entrez votre premier nombre\n"))
        nombre2= int(input("entrez la puissance de ce numero\n"))
        calculatrice=Calculatrice(nombre1,nombre2)
        calculatrice.puissance()
    elif choix==0:
        print("aurevoir")
        break
    else:
        print("choix invalide reesayer")        