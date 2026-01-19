'''

Docstring for Class01_Cellule
test Eric

'''
#------------------------------
class Cellule: #declaration d'une classe objet, mot clef 'class'
    "Modelisation de la cellule machine"
    mode = ("Arret", "Manuel", "Auto") #attribut
    mode_courant = 0 #attribut

    def Marche(self): #methode attachee par le mot clef 'self'
        "Demarrage de la cellule"
        self.mode_courant = 1 #procedure appelant les attributs via self

    def GetMode(self): #methode
        "Retourne le mode de la cellule"
        return self.mode[self.mode_courant] #retour de la fonction
    
    def Arret(self): #methode
        "Arret de la cellule"
        pass #traitement de la fonction non encore definit
    