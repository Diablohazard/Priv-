class Produit:

    # ========= Attributs de classe =========
    TYPE = {
        "Bois":  700,
        "Verre":  2500,
        "Acier":  7700,
        "Aluminium": 2700
    }

    # ========= Attributs d'instance =========
    def __init__(self, id=1):
        self.material = "Bois"
        self.length_m = 0.0
        self.width_m = 0.0
        self.height_m = 0.0
        self.volume_m3 = 0.0
        self.mass_kg = 0.0