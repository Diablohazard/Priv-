class Produit:

    # ========= Attributs de classe =========
    DENSITY = {
        "Bois":  700,
        "Verre":  2500,
        "Acier":  7700,
        "Aluminium": 2700
    }

    # ========= Attributs d'instance =========
    def __init__(self, material=str, length_mm=int, width_mm=int, height_mm=int):
        self.material = material
        self.length_m = length_mm / 1000
        self.width_m = width_mm / 1000
        self.height_m = height_mm / 1000
        self.volume_m3 = self.length_m * self.width_m * self.height_m
        self.mass_kg = self.volume_m3 * self.DENSITY[self.material]

    # ========= Méthodes =========
    def ComputeVolume(self):
        self.volume_m3 = self.length_m * self.width_m * self.height_m
        return self.volume_m3

    def ComputeMass(self):
        self.mass_kg = self.volume_m3 * self.DENSITY[self.material]
        return self.mass_kg

    def __str__(self):
        return f"material={self.material} longueur=({self.length_m}, largeur={self.width_m}, hauteur={self.height_m}) volume={self.volume_m3}m3 mass={self.mass_kg}kg"


# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    p1 = Produit("Bois", 500, 500, 500)  # première instance

    print(p1)

    p1.length_m = 1
    print(p1)

    p1.ComputeVolume()
    print(p1)

    p1.volume_m3 = p1.ComputeVolume()
    p1.mass_kg = p1.ComputeMass()
    print(p1)
