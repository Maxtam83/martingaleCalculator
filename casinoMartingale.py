import os
import random

def affiche(valeur):
    print(valeur)

def martingale(valeurDepot,miseDepart,affichage):

    # déclaration variables
    min = 9999
    max = 0
    compteurDeCoup = 1

    miseCourante = miseDepart
    valeurDepotCourante = valeurDepot

    while (miseCourante < valeurDepotCourante):
        valeurDepotCourante -= miseCourante
        valeurDepotCourante = round(valeurDepotCourante,1)
        resultatRoulette = random.randint(0,36)

        if (resultatRoulette >= 18):

            if (min > valeurDepotCourante):
                            min = valeurDepotCourante

            valeurDepotCourante += miseCourante * 2
            valeurDepotCourante = round(valeurDepotCourante,1)
            miseCourante = miseDepart

        else:
            miseCourante *= 2
            valeurDepotCourante = round(valeurDepotCourante,1)
        
        if (max < valeurDepotCourante):
            max = valeurDepotCourante

        if(affichage == 'o'):
            affiche(valeurDepotCourante)

        compteurDeCoup += 1

    print('\n\nnombre de coup total : ',compteurDeCoup,"\n\nmin :",min,"\nmax : ",max,"\n")

    return compteurDeCoup, min, max

# Main
os.system('cls')
ValeurDepot = float(input("valeur déposé dans la machine :\n\n-> "))
miseDepart = float(input("\nvaleur mise de départ :\n\n-> "))
estAffichage = input("\nvoulez-vous l'affichage des valeurs à chaque tour ? (o/n)\n\n-> ")
nEssais = int(input("\nCombien d'essai ?\n\n-> "))

Pmax = 0
Pmin = 9999
Gmax = 0
Gmin = 9999
minCumul = 0
maxCumul = 0
minMoy = 0
maxMoy = 0
nCoupTemp = 0
nCoupCumule = 0

for i in range(0,nEssais):
    nCoupTemp,Pmin, Pmax = martingale(ValeurDepot,miseDepart,estAffichage)
    if (Pmin < Gmin):
        Gmin = Pmin

    if (Pmax > Gmax):
        Gmax = Pmax

    nCoupCumule += nCoupTemp
    minCumul += Pmin
    maxCumul += Pmax
    
nCoupMoy = nCoupCumule/nEssais
minMoy = minCumul / nEssais
maxMoy = maxCumul / nEssais

print("\n\n====================\n\nNombre d'essai :", nEssais,"\nGain Max : ",Gmax,"\nGain max moyen : ",maxMoy,"\nGain Min",Gmin,"\nGain min moyen : ",minMoy,"\nnombre de coup moyen : ",nCoupMoy)