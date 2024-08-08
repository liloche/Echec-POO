class Piont:
    def __init__(self, famille, couleur, numero):
        self.famille = famille
        self.couleur = couleur
        self.numero = numero

class Plateau:
    def __init__(self):
        self.grille = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
        self.coups = 0
        self.joueur = 0 # 0 = blancs, 1 = noirs
        self.blancDehors = []
        self.noirDehors = []
    
    def coups_possibles(self, piont):
        lst = []
        return lst
    
    def changer_piont(self, piont, coord_x, coord_y):
        return
    
    def tourner_plateau(self):
        grille_remplacement = [[self.grille[7-i][7-j] for j in range(8)] for i in range(8)]
        self.grille = grille_remplacement