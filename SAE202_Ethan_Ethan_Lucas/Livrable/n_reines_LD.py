#---------------------------Desperrois_Lucas-------------------------------#
#---------------Algorithme de résolution du Problème des N Dames ----------#
#------------------------n_reines_LD.py-------------------------#    





#---------Fonction affiche_plateau(n,grille)-------------#
# - Type du résultat de la fonction : void
# - Résultat de la fonction : Affichage de l'échiquier pour 1 solution du problème des N dames

# - Param n : entier qui représente la taille de l'echiquier
# - Param grille : Liste de Liste qui représente l'échiquier

# - Fonctionnement : Utilisation d'une double boucle for pour afficher le tabelau à deux dimenssions 

def affiche_plateau(n,grille):
    

    for i in range(n):                                   # double boucle for
        for j in range(n):
            if (grille[i][j]==1):
                print(" | dame" ,end='');
            else:
                print(" | ",grille[i][j]," ",end='');    #Affichage des barres qui séparent les positions de l'echiquier
        print(" |",end='');
        
        
        print("\n");
    print("\n\n\n\n");

#---------Fonction valide_position(grille,col,lig)---------#
# - Type de résultat de la fonction : Booléen
# - Résultat de la fonction : retourne un booléen si la position de la n ème dame en position(lig,col) peut être posé sans être menacé

# - Param grille : Liste de Liste qui représente l'échiquier
# - Param lig : entier qui représente la ligne où on test de poser la n-ème dames
# - Param col : entier qui représente la colonne où on test de poser la n-ème dames

# - Fonctionnement_Fonction : on parcourt toute la grille pour tester si on peut poser la n-ème dames sur la position
# (lig,colonne) sans être menacées par les autres dames.


def valide_position(grille,lig,col):
    i=lig;
    j=col;
    ok=True;                                            # variable résultat;
    n=len(grille);
                                                        # le 1 sur la grille signifie que la case est occupé par une reine 
                                                        #toutes les boucles while cherchent dans les differentes directions par rapport à la reine qu'on veut poser
                                                        #à la position(lig,colonne)

    #vérification est

    while(j+1<n and ok==True):
        j=j+1;
        if(grille[i][j]==1):
            ok=False;
                    
    j=col;
    #verification sud
    while(i+1<n and ok==True):
        i=i+1;
        if(grille[i][j]==1):
            ok=False;
    i=lig;
    #verification  ouest
    while(j-1>=0 and ok==True):
        j=j-1;
        if(grille[i][j]==1):
            ok=False;
    j=col;
    # vérification sud est
    while(j+1<n and i+1<n and ok==True):
        i=i+1;
        j=j+1;
        if(grille[i][j]==1):
            ok=False;
    i=lig;
    j=col;
    # vérification nord ouest
    while(j-1>=0 and i-1>=0 and ok==True):
        i=i-1;
        j=j-1;
        if(grille[i][j]==1):
            ok=False;
    i=lig;
    j=col;
    # verification nord 
    while(i-1>=0 and ok==True):
        i=i-1;
        if(grille[i][j]==1):
            ok=False;
    i=lig;
    # verification nord est
    while(i-1>=0 and j+1<n and ok==True):
        i=i-1;
        j=j+1;
        if(grille[i][j]==1):
            ok=False;
    i=lig;
    j=col;
    # verrification sud ouest
    while(i+1<n and j-1<=0 and ok==True):
        i=i+1;
        j=j+1;
        if(grille[i][j]==1):
            ok=False;
    
    return ok;
                    
                        
                    
#----------- Fonction grille(n)--------------------#
# - Type du résultat de la fonction : list
# - Résultat de la fonction : une grille de liste de listes de zeros

# - param n : entier qui représente la taille de la grille

# - Fonctionement-de-la-Fonction : on créer une grille avec une liste par compréhension


def grille(n):
    l = [[0 for i in range(n)] for i in range(n)]               #création d'une liste en compréhension
    return l;
                                                                #0:case vide,1:la reine

#------------Fonction placer_reine_affichage---------#
# - Type du résultat de la fonction : void
# - Résultat de la fonction : affichage des solutions pour n dames 

# - param lig : entier qui représente la ligne où on commence de placer les reines
# - param echequier : liste de listes qui represente l'échiquier
# - param n :entier qui représente la taille de la liste de listes(échiquier)

# - Fonctionnement-de-la-fonction : c'est la fonction de résolution du problème des dames mais qui affiche les solutions
#  . elle utilise le récursif et le backtracing pour afficher les solutions 



def placer_reine_affichage(lig,echequier,n):
    #boucle qui parcourt toutes les colonnes d'une ligne
    for col in range(n):
        
        echequier[lig][col]=1;
        if(valide_position(echequier,lig,col)):
                                                    #si on a pas atteint la dernière ligne de l'échiquier et que la position de la dernière dame et valide
                                                    #on appelle récursivement la fonction pour la ligne suivante
            if(lig<n-1):
                placer_reine_affichage(lig+1,echequier,n);
            else:
                                                    #si on a traité toutes les lignes où placer les dames pour un cas on affiche l'échiquier mais le récursif ne s'arrête pas puisque
                                                    #on a pas fini d'effectuer la boucle for ci-dessus pour les autres appels récursifs
                affiche_plateau(n,echequier);
        echequier[lig][col]=0;                      #si la position tester n'est pas valide on met un 0 à la position tester

#---------------Fonction placer_reine(lig,echequier,n,l)------------#
# - Type de résultat de la fonction : entier
# - Résultat-de-la-fonction : le nombre de solutions du problème des dames pour n dames

# - param lig : entier qui représente la ligne où on commence de placer les reines
# - param echequier : liste de listes qui represente l'échiquier
# - param n : entier qui représente la taille de la liste de listes(echiquier)
# - param l : liste qui contient à l'indice 0 le nombre de solutions pour n dames

# - Fonctionnement-de-la-fonction : c'est la fonction de résolution du problème des dames mais qui affiche les solutions
#  .Elle utilise le récursif et le backtracing pour afficher les solutions



def placer_reine(lig,echequier,n,l):
                                            #boucle qui parcourt toutes les colonnes d'une ligne
    for col in range(n):
        
        echequier[lig][col]=1;
        if(valide_position(echequier,lig,col)):
                                            #si on a pas atteint la dernière ligne de l'échiquier et que la position de la dernière dame et valide
                                            #on appelle récursivement la fonction pour la ligne suivante
            if(lig<n-1):
                
                placer_reine(lig+1,echequier,n,l);
            else:
                                            # lorsqu'on a fini de traité toutes les lignes pour placer toutes les dames pour un cas on ajoute un
                                            # au compteur du nombre de solutions
                l[0]+=1;
                
                
                
        echequier[lig][col]=0;              #si la position tester n'est pas valide on met un 0 à la position tester
    return l[0];                            # le compteur à l'indice 0 de la liste



#--------------Fonction main()----------------------------#
# - Type de resultat de la fonction : void
# - Resultat-de-la-fonction : affichage des nombres de solutions pour n dames mais aussi de tous les échiquiers possibles pour n dames.
#
#
# - Fonctionnement-de-la-Fonction : elle propose de résoudre le probleme pur n dames et empêche 
# de résoudre le cas pour n<=3 car cela ne marche pas



def main():
    nb=int(input("donnez la taille de l'echiquier"));
    while(nb<=3):
        print("la taille de l'echiquier doit être supérieur à 3 sinon on ne peut pas placer les dames");
        nb=int(input("donnez la taille de l'échiquier"));
    print("le nombre de solutions pour le problème des dames avec un échiquier de",nb,"est de:",placer_reine(0,grille(nb),nb,[0]),"solutions")
    rep=str(input("voulez-vous voir tous les échiquiers possibles pour le nombre de dames demandées précedemment, alors tapez 1 sinon pour quitter saissisez ce que vous souhaitez"));
    if(rep=="1"):
        placer_reine_affichage(0,grille(nb),nb);
    else:
        print("aurevoir");
        
        
 
main();
    
    




    
    
        
            