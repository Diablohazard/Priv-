import encapsulation

#------------------------------

class ProduitSurface(encapsulation.Produit):
    "Modelisation d'un produit avec traitement de surface herite de la classe Produit"
    __surface = ("Vernis", "Peinture", "Galvanisé")

    def __init__(self, mat, l, w, h, trait): #constructeur
        "Constructeur du produit avec traitement"
        super().__init__(mat, l, w, h) # classe de base/mere
        self.__traitement = trait # attribut de la classe derivee/fille

    def __str__(self):
        "Affichage caracteristiques du produit traite"
        str_trait = '{' + self.__traitement + '}'
        return f"{super().__str__()} {str_trait}"
    

# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    p1 = ProduitSurface("Bois", 500, 500, 500, "Vernis")

    print(p1)

    print(p1.length)

    p1.length = 1000
    print(p1)
