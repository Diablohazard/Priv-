import encapsulation

#------------------------------

class ProduitSurface(encapsulation.Produit):
    "Modelisation d'un produit avec traitement de surface herite de la classe Produit"
    __surface = ("Vernis", "Peinture", "Galvanisé")

    def __init__(self, mat, l, w, h, trait): #constructeur
        "Constructeur du produit avec traitement"
        super().__init__(mat, l, w, h) # classe de base/mere
        assert trait in self.__surface, 'fatal: traitement inexistant %s' % trait
        self.__traitement = trait # attribut de la classe derivee/fille

    @property
    def traitement(self):
        return self.__traitement

    @traitement.setter
    def traitement(self, trait):
        assert trait in self.__surface, 'fatal: traitement inexistant %s' % trait
        self.__traitement = trait


# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    p1 = ProduitSurface("Bois", 500, 500, 500, "Vernis")

    print(p1)

    print(p1.length)

    p1.length = 1000
    print(p1)

    p1.traitement = "Peinture"
    print(p1)

    try:
        p1.traitement = "Sablage" # traitement inexistant
        print(p1)
    except Exception as e:
        print(e)

    p1.traitement = "Ebavurage" # traitement inexistant
    print(p1)
