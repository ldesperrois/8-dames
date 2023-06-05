"""
AUTHOR : LEVACHER Ethan
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import os
from fpdf import FPDF

"""
Fonction permettant de créé une image 
"""
def create_damier(n):
    # Définir la taille de l'image et le nombre de carrés par côté
    size = n
    squares_per_side = 4

    # Créer un tableau de la taille de l'image, initialisé à 0.5 (gris moyen)
    image = np.ones((size, size)) * 0.5

    # Parcourir les carrés et changer la couleur en noir ou blanc
    for i in range(squares_per_side):
        for j in range(squares_per_side):
            if (i + j) % 2 == 0:
                image[i::squares_per_side, j::squares_per_side] = 0

    return image

def show_damier(image, liste_dame, num, dir):
    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)
    # Afficher l'image
    plt.imshow(image, cmap='gray')
    for i in range(len(liste_dame)):
        plt.plot(i, liste_dame[i], 'ro', markersize=15)
    plt.savefig(dir+"/damier"+str(num)+".png")
    plt.close()

"""
Fonction boolean renvoyant True si il est possible de jouer la reine sans qu'elle sois en danger et false dans le cas contraire.
Paramètres: 
    s: le tableau contenant les reines actuellement placé/
    ligne: un entier qui correspond à la ligne où l'on souhaite jouer notre reine.
    colonne: un entier qui correspond à la colonne où l'on souhaite jouer notre reine.
"""
def possible(s, ligne, colonne):
    jouable = True
    l = 0
    # On verifie pour chaque reine tant qu'il reste des reines et que c'est toujours jouable.
    while (l < ligne and jouable):
        # on récupère la colonne de la reine l
        c = s[l]
        # Verification le l est sur la même diagonale que la reine que l'on souhaite joué.
        # Et également si leurs colonne est différentes.
        jouable = (abs(ligne-l) != abs(colonne-c) and colonne != c)
        l = l + 1
    return jouable

"""
Fonction récursive qui ajoute chaque combinaison d'échéquier possible dans une liste qui lui ai passé en paramètre.
Paramètres:
    n: un entier correspondant à la taille de l'échequier.
    solutions: une liste qui contiendra l'ensemble des solutions.
    sol: une liste représentant un échéquier (utile pour l'appel récursif).
    col: un entier correspondant la colonne dans laquelle on cherche à placer une reine (utile pour l'appel récursif).
"""
def placerReine(n, solutions, sol=[], col=0):
    if (sol == []):
        sol = [-1 for i in range(n)]
    # Cas de base : Si nous avons n reines de placés : On ajoute le tableau au solution.
    if col == n:
        solutions.append(sol.copy())
    else:
        ligne = 0
        # Boucle permettant de parcours chaque colonne
        while (ligne < n):
            # Verification si il est possible de jouer dans cette ligne
            if possible(sol, col, ligne):
                # On place la reine 
                sol[col] = ligne
                # On recommence l'étape avec la reine que l'on à passé précédemment
                placerReine(n, solutions, sol, col+1)
                # On retourne en arrière en enelevant la reine
                sol[col] = 0
            ligne = ligne + 1

"""
Fonction qui permet de gérer l'appel de la fonction placerReine
Utile pour calculer le temps d'execution
Paramètres:
    n: un entier correspondant à la taille de l'échecquier
"""
def n_reines(n):
    liste_solutions = []
    placerReine(n, liste_solutions)
    return liste_solutions

def create_images(n, l, dir):
    #Vide le dossier img
    if os.path.exists(dir):
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    for i in range(len(l)):
        dam = create_damier(n)
        show_damier(dam, l[i], i, dir)

def create_pdf(dir, name, n):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    imagelist = os.listdir(dir) # listes des images
    pdf = FPDF('P','mm','A4') # Création du PDF
    WIDTH = 210 # Largeur
    HEIGHT = 287 # Hauteur
    # Page d'introduction
    pdf.add_page()
    font_size = 16
    line = ["Ensemble des solutions pour le problème des n-reines avec " + str(n) + " dames", str(len(imagelist)) + " solutions"]
    pdf.set_font("Arial", size=font_size)
    # Centrage du texte
    text_width = pdf.get_string_width(line[0])
    y = (HEIGHT - font_size * 2) / 2
    x = (WIDTH - text_width) / 2
    pdf.text(x, y, line[0])
    # Centrage du texte
    text_width = pdf.get_string_width(line[1])
    x = (WIDTH - text_width) / 2
    pdf.text(x, y+font_size, line[1]) 
    x,y,w,h = 0,0,216,144
    # Centre de la page pour y placer l'image
    y = (HEIGHT - 144) / 2
    for i in range(len(imagelist)):
        pdf.add_page()
        pdf.set_font("Arial", size=24)
        pdf.cell(200, 10, txt="Solutions n°" + str(i), align="C")
        pdf.image(dir+imagelist[i],x,y,w,h)
    pdf.output(dir_path+"\\"+name,"F")

# Calcul du temps d'execution :
n = -1
try:
   n = int(input("Nombre de reines que vous souhaitez placé ?"))
except:
    n = 8
    print("Le nombre de reines que vous souhaitez placé doit être un eniter !")
    print("Nombre de reines par défaut : 8")

while (n <= 0):
    try:
        n = int(input("Nombre de reines que vous souhaitez placé ?"))
    except:
        n = 8
        print("Le nombre de reines que vous souhaitez placé doit être un eniter !")
        print("Nombre de reines par défaut : 8")

t1 = time.time()
l = n_reines(n)
t2 = time.time()-t1
print(l)
print(str(len(l)) + " solutions on été trouvé.")
print(f'Temps d\'execution de la fonction n_reines : {t2}')

rep = input("Souhaitez-vous conserver les résultats sous formes d'images ? (y/n)")
if rep == "y":
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/img/"
    print("Création des images en cours...")
    create_images(n, l, dir_path)
    print("Images crééent avec succès ! (Dossier img)")
    rep = input("Souhaitez-vous créé un PDF récapitulatif à partir de ces images ? (y/n)")
    if rep == "y":
        print("Création du PDF en cours...")
        create_pdf(dir_path, "solution_"+str(n)+"_dame.pdf", n)