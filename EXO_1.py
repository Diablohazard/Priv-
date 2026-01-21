class Robot:
    """
    Classe Robot
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
    def __init__(self):
        self.state_OK = True
        self.nb_alarme = 0
        self.pos_Tool = Robot.POSITIONS["init"]

    # ========= Méthodes =========
    def Moveinit(self):
        self.pos_Tool = Robot.POSITIONS["init"]

    def MoveHome(self):
        self.pos_Tool = Robot.POSITIONS["Home"]

    def MovePick(self):
        self.pos_Tool = Robot.POSITIONS["Pick"]

    def MovePlace(self):
        self.pos_Tool = Robot.POSITIONS["Place"]

    def RaiseDefault(self):
        self.state_OK = False
        self.nb_alarme += 1

    def ClearDefault(self):
        self.state_OK = True

    def GetStatus(self):
        x, y, z = self.pos_Tool
        print("marque\tstate_OK\tnb_alarme\tX\tY\tZ")
        print(f"{Robot.marque}\t{self.state_OK}\t{self.nb_alarme}\t\t{x}\t{y}\t{z}")
        print(
            f"{Robot.marque} Status "
            f"{'OK' if self.state_OK else 'DEFAULT'} "
            f"({self.nb_alarme}) "
            f"Position X={x} Y={y} Z={z}"
        )
        print("-" * 60)


# =====================================================
# Jeu de test
# =====================================================

if __name__ == "__main__":#structure conditionnelle de test

    print(Robot.marque)  # utilisation attribut de classe sans instanciation

    rob1 = Robot()  # première instance
    rob2 = Robot()  # deuxième instance

    # Ordres sur robot 1
    rob1.GetStatus()
    rob1.MoveHome()
    rob1.RaiseDefault()
    rob1.GetStatus()
    rob1.ClearDefault()
    rob1.GetStatus()

    # Ordres sur robot 2
    rob2.GetStatus()
    rob2.RaiseDefault()
    rob2.GetStatus()
