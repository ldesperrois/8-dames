### Author : COLLIN Ethan
### Algorithme d'exploration algorithmique pour résoudre le problème des huits reines
### Time : 31/03/2023

### Mon programme est fait en 2 dimension , en me servant des coordonnées 'x' et 'y' comparée à ceux de mes collègues qui utilise une grille 


def solve_n_queens(n):
    #  Permet d'initialiser la liste des combinaisons possible
    liste_solutions = []
    # Permet initialiser la liste de placements possibles pour chaque reine
    placements = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            # Permet de ajouter toutes les positions possibles pour chaque reine
            placements[i].append((i, j))

    # Permet de Trouver toutes les combinaisons possibles de placements pour chaque reine
    all_combinations = cartesian_product(placements)

    # Permet de Trouver la première combinaison valide de placements de reines
    for combination in all_combinations:
        if is_valid(combination):
            liste_solutions.append(combination)
    print(liste_solutions)
    print(len(liste_solutions))
    
# def is_valid permet de vérifier si une combinaison donnée de placements de reines est valide
def is_valid(combination):
    for i in range(len(combination)):
        for j in range(i+1, len(combination)):
            # Vérifie si 2 reines ont une position en conflit ( se menace )
            if conflict(combination[i], combination[j]):
                return False
    return True

# def conflict Permet de vérifier s'il y a un conflit entre deux reines placées sur les positions (i1, j1) et (i2, j2)
def conflict(pos1, pos2):
    i1, j1 = pos1
    i2, j2 = pos2
    if i1 == i2 or j1 == j2 or abs(i1 - i2) == abs(j1 - j2):
        # vérifie si les positions sont sur la même ligne, la même colonne ou la même diagonale
        return True
    return False

# def cartesian_product Permet de trouver le produit cartésien de plusieurs listes
def cartesian_product(lists):
    if len(lists) == 1:
        return [(item,) for item in lists[0]]
    else:
        result = []
        for item in lists[0]:
            # Gràce à la récursive cela permet de trouver le produit cartésien des listes restantes
            for rest in cartesian_product(lists[1:]):
                result.append((item,) + rest)
        return result

# Appele la fonction pour résoudre le problème
solve_n_queens(8)


### Cet algorithme utilise une approche de recherche complète qui permet de générer toutes les combinaisons possibles de placements et à les vérifier.
### Cependant cet algorithme utilise beaucoup de ressources , ce qui fait qui est très lent comparée à des algorithme de BackTracking.
### Cet algorithme ne permettra pas de résoudre le problème de huits reines si la grille devient trop grande , ceci est la limite de de l'alogrithme.