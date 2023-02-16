from random import randint

#Liste des choix possibles
jeu  = ["pierre", "papier", "ciseaux"]

#L'ordinateur va venir prendre un choix aléatoires entre les 3
ordinateur = jeu[randint(0,2)]

#On initialise le compteur
Pointsjoueur = 0
Pointsordinateur = 0

continuer = True

#tant que le joueur n'a pas écris 'Fin' alors le jeu continue
while(continuer):
    #Demander le choix de l'ordinateur<br>
    joueur = input("pierre, papier, ciseaux? ou tapez Fin pour arrêter le jeu!\n")

    #On vient créer nos scénarios possibles
    if(joueur == 'Fin'):
        continuer = False
    elif(joueur == ordinateur):
        print("Egalité!")
    elif(joueur == "pierre"):
        if(ordinateur == "papier"):
            print("Perdu!", ordinateur, "recouvre", joueur)
            Pointsordinateur = Pointsordinateur + 1 
        else:
            print("Gagné!", joueur, "écrase", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    elif(joueur == "papier"):
        if(ordinateur == "ciseaux"):
            print("Perdu!", ordinateur, "coupe", joueur)
            Pointsordinateur = Pointsordinateur + 1
        else:
            print("Gagné!", joueur, "recouvre", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    elif(joueur == "ciseaux"):
        if(ordinateur == "Pierre"):
            print("Perdu...", ordinateur, "écrase", joueur)
            Pointsordinateur = Pointsordinateur + 1
        else:
            print("Gagné!", joueur, "coupe", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    else:
        print("Votre choix n'est pas correct, vérifiez l'orthographe!")
    #L'ordinateur ici va choisir son prochain choix
    ordinateur = jeu[randint(0,2)]
    print('********Tour suivant********')

#Fin de la partie on attribue les points à chacun
print("********Points********")
print("joueur: ", Pointsjoueur)
print("ordinateur: ", Pointsordinateur)