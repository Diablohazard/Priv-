class Produit:

    # ========= Attributs de classe =========
    __DENSITY = {
        "Bois":  700,
        "Verre":  2500,
        "Acier":  7700,
        "Aluminium": 2700
    }

    # ========= Attributs d'instance =========
    def __init__(self, material=str, length_mm=int, width_mm=int, height_mm=int):
        self.__material = material
        self.__length_m = length_mm / 1000
        self.__width_m = width_mm / 1000
        self.__height_m = height_mm / 1000
        self.__volume_m3 = self.__length_m * self.__width_m * self.__height_m
        self.__mass_kg = self.__volume_m3 * self.__DENSITY[self.__material]

    # ========= Méthodes =========
    def ComputeVolume(self):
        self.__volume_m3 = self.__length_m * self.__width_m * self.__height_m
        return self.__volume_m3

    def ComputeMass(self):
        self.__mass_kg = self.__volume_m3 * self.__DENSITY[self.__material]
        return self.__mass_kg

    def __str__(self):
        return f"material={self.__material} longueur=({self.__length_m}, largeur={self.__width_m}, hauteur={self.__height_m}) volume={self.__volume_m3}m3 mass={self.__mass_kg}kg"


# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    p1 = Produit("Bois", 500, 500, 500)  # première instance

    print(p1)

    p1.__length_m = 1
    print(p1)

    p1.ComputeVolume()
    print(p1)

    p1.__volume_m3 = p1.ComputeVolume()
    p1.__mass_kg = p1.ComputeMass()
    print(p1)
