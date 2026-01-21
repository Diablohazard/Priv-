from syntaxe import Cellule as Cellule
from EXO_1 import Robot
from EXO_Multirobot import MultiRobot as mr

#===========================================

if __name__ == "__main__":
    cell = Class01_Cellule()
    rob = Robot()
    rob1 = mr.MultiRobot()

    print("Mode courant =", cell.GetMode())
    rob.GetStatus()
    print(rob.GetStatus())
    print(rob1)

    rob1.MoveHome()
    rob1.RaiseDefault()
    print(rob1)
    rob1.ClearDefault()
    rob1.MovePick()
    print(rob1)

    rob1.nb_alarme = 0
    rob1.pos_Tool[2] = -100
    print(rob1)