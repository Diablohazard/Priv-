class MultiRobot:
    """
    Classe MultiRobot
    """

    # ========= Attributs de classe =========
    marque = "FANUC"

    # Positions outil (X, Y, Z)
    POSITIONS = {
        "init":  [0, 0, 0],
        "Home":  [10, 10, 500],
        "Pick":  [100, 30, 120],
        "Place": [100, 150, 230]
    }

    # ========= Attributs d'instance =========
    def __init__(self, id=1):
        self.id = id
        self.state_OK = True
        self.nb_alarme = 0
        self.pos_Tool = [0, 0, 0]

    # ========= Méthodes =========
    def Moveinit(self):
        self.pos_Tool = MultiRobot.POSITIONS["init"]

    def MoveHome(self):
        self.pos_Tool = MultiRobot.POSITIONS["Home"]

    def MovePick(self):
        self.pos_Tool = MultiRobot.POSITIONS["Pick"]

    def MovePlace(self):
        self.pos_Tool = MultiRobot.POSITIONS["Place"]

    def RaiseDefault(self):
        self.state_OK = False
        self.nb_alarme += 1

    def ClearDefault(self):
        self.state_OK = True

    def __str__(self):
        return f"MultiRobot id={self.id} state={'OK' if self.state_OK else 'DEFAULT'} pos={self.pos_Tool} alarms={self.nb_alarme}"


# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    print(MultiRobot.marque)  # utilisation attribut de classe sans instanciation

    rob1 = MultiRobot()  # première instance
    rob2 = MultiRobot(2)  # deuxième instance

    # Ordres sur robot 1
    print(rob1)
    rob1.MoveHome()
    rob1.RaiseDefault()
    print(rob1)
    rob1.ClearDefault()
    rob1.MovePick()
    print(rob1)

    # Ordres sur robot 2
    print(rob2)
    rob2.RaiseDefault()
    print(rob2)