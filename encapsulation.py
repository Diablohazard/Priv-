class Produit:

    # ========= Attributs de classe =========
    DENSITY = {
        "Bois":  700,
        "Verre":  2500,
        "Acier":  7700,
        "Aluminium": 2700
    }

    # ========= Attributs d'instance =========
    def __init__(self, id=1):
        self.material = "Bois"
        self.length_m = 0.5
        self.width_m = 0.5
        self.height_m = 0.5
        self.volume_m3 = 0.125
        self.mass_kg = 87.5

    # ========= Méthodes =========
    def ComputeVolume(self):
        self.volume_m3 = self.length_m * self.width_m * self.height_m

    def ComputeMass(self):
        self.mass_kg = self.volume_m3 * self.DENSITY[self.material]

    def __str__(self):
        return f"material={self.material} longueur=({self.length_m}, largeur={self.width_m}, hauteur={self.height_m}) volume={self.volume_m3}m3 mass={self.mass_kg}kg"


# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    p1 = Produit("bois", 500, 500, 500)  # première instance

    print(p1)

    p1.length_m = 1
    print(p1)

    p1.ComputeVolume()
    print(p1)

    p1.volume_m3 = p1.ComputeVolume()
    p1.mass_kg = p1.ComputeMass()
    print(p1)
