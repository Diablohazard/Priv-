class Robot:
    """
    Classe Robot
    """

    # ========= Attributs de classe =========
    marque = "FANUC"
    state_OK = True
    nb_alarme = 0

    # Positions outil (X, Y, Z)
    POSITIONS = {
        "init":  [0, 0, 0],
        "Home":  [10, 10, 500],
        "Pick":  [100, 30, 120],
        "Place": [100, 150, 230]
    }

    # Position courante outil
    pos_Tool = POSITIONS["init"]

    def Moveinit(self):
        self.pos_Tool = Robot.POSITIONS["init"]

    def MoveHome(self):
        self.pos_Tool = Robot.POSITIONS["Home"]

    def MovePick(self):
        self.pos_Tool = Robot.POSITIONS["Pick"]

    def MovePlace(self):
        self.pos_Tool = Robot.POSITIONS["Place"]

    def RaiseDefault(self):
        Robot.state_OK = False
        Robot.nb_alarme += 1

    def ClearDefault(self):
        Robot.state_OK = True

        # ========= Méthodes =========
    def GetStatus(self):
        x, y, z = self.pos_Tool
        print("marque\tstate_OK\tnb_alarme\tX\tY\tZ")
        print(f"{Robot.marque}\t{Robot.state_OK}\t{Robot.nb_alarme}\t\t{x}\t{y}\t{z}")
        print(
            f"{Robot.marque} Status "
            f"{'OK' if Robot.state_OK else 'DEFAULT'} "
            f"({Robot.nb_alarme}) "
            f"Position X={x} Y={y} Z={z}"
        )
        print("-" * 60)


# =====================================================
# Jeu de test (conforme à l’énoncé)
# =====================================================

if __name__ == "__main__": #structure conditionnelle de test

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
