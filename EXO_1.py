class PositionTool: #declaration du tableau des positions
    position = ["X", "Y", "Z"] #attribut des coordonnées
    init = [0.0, 0.0, 0.0] #attribut des coordonnées initiales
    Home = [10.0, 10.0, 500.0] #attribut des coordonnées Home
    Pick = [100.0, 30.0, 120.0] #attribut des coordonnées Pick
    Place = [100.0, 150.0, 230.0] #attribut des coordonnées Place

def GetStatus(): #methode
    "Retourne le status de la position"
    return f"Position Tool : {str(PositionTool.position)}\n"