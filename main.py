class Piont:
    def __init__(self, famille, couleur, numero):
        self.famille = famille
        self.couleur = couleur
        self.numero = numero

    def coord_piont(self, plateau):
        for i in range(8):
            for j in range(8):
                if plateau.grille[i][j] == self:
                    return (j, i)

pb1 = Piont("piont", "blanc", 1)
pb2 = Piont("piont", "blanc", 2)
pb3 = Piont("piont", "blanc", 3)
pb4 = Piont("piont", "blanc", 4)
pb5 = Piont("piont", "blanc", 5)
pb6 = Piont("piont", "blanc", 6)
pb7 = Piont("piont", "blanc", 7)
pb8 = Piont("piont", "blanc", 8)

pn1 = Piont("piont", "noir", 1)
pn2 = Piont("piont", "noir", 2)
pn3 = Piont("piont", "noir", 3)
pn4 = Piont("piont", "noir", 4)
pn5 = Piont("piont", "noir", 5)
pn6 = Piont("piont", "noir", 6)
pn7 = Piont("piont", "noir", 7)
pn8 = Piont("piont", "noir", 8)

tb1 = Piont("tour", "blanc", 1)
tb2 = Piont("tour", "blanc", 2)

tn1 = Piont("tour", "noir", 1)
tn2 = Piont("tour", "noir", 2)

cb1 = Piont("cavalier", "blanc", 1)
cb2 = Piont("cavalier", "blanc", 2)

cn1 = Piont("cavalier", "noir", 1)
cn2 = Piont("cavalier", "noir", 2)

fb1 = 
fb2 = 

fn1 = 
fn2 = 

class Plateau:
    def __init__(self):
        self.grille = [[tn2, cn2, None, None, None, None, cn1, tn1],
                       [pn8, pn7, pn6, pn5, pn4, pn3, pn2, pn1],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8],
                       [tb1, cb1, None, None, None, None, cb2, tb2]]
        self.coups = 0
        self.joueur = 0 # 0 = blancs, 1 = noirs
        self.blancDehors = []
        self.noirDehors = []
    
    def coups_possibles(self, piont):
        lst = []
        return lst
    
    def changer_piont(self, piont, coord_x, coord_y):
        if (coord_x, coord_y) in self.coups_possible(piont):
            ancienneCoordX, ancienneCoordY = piont.coord_piont(self)
            self.grille[ancienneCoordY][ancienneCoordX] = None
            if self.grille[coord_y][coord_x] != None:
                if self.grille[coord_y][coord_x].couleur == "noir":
                    self.noirDehors.append(self.grille[coord_y][coord_x])
                else:
                    self.blancDehors.append(self.grille[coord_y][coord_x])
            self.grille[coord_y][coord_x] = piont
            self.coups += 1
            return 0 # Pas d'erreur
        print("Coup impossible")
        return 1 # Erreur
    
    def tourner_plateau(self):
        grille_noir = [[self.grille[7-i][7-j] for j in range(8)] for i in range(8)]
        self.grille = grille_noir
    
    def aficher_grille(self):
        for i in self.grille:
            print(i)
        return

