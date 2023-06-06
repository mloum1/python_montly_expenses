import datetime

devises = ['dollar', 'euro', 'yen', 'pound', 'franc CFA']
print("Les devises disponibles sont :")
for devise in devises:
    print("-", devise)

choice = input("Entrez le nom de votre devise : ")
if choice not in devises:
    print("Devise invalide, veuillez réessayer")
    nb_essais = 0
    while choice not in devises:
        choice = input("Entrez le nom de votre devise : ")
        nb_essais += 1
        if nb_essais > 3:
            print("Vous avez dépassé le nombre de tentatives autorisées")
            exit()

else:
    print("Vous avez choisi la devise", choice)

      ####** saisie du mois **####
###**================================**###
salary = float(input("Entrez votre salaire : "))
now = datetime.datetime.now()
date_salaire = now.strftime("%d-%m-%Y")
      ####** Fin de ce variable **####
###**================================**###


amount = float(input("Entrez un montant : "))

if amount <= 0:
    print("Le montant doit être supérieur à 0")
    exit()


# Afficher le montant et la date de saisie du montant et la devise choisie
if amount > 1:
    print("Vous avez saisi un montant de", amount, choice + "s", "le", date_salaire)
else:
    print("Vous avez saisi un montant de", amount, choice, "le", date_salaire)

# Créer un fichier pour sauvegarder le montant et la date de saisie du montant et la devise choisie
fichier = "saisie_montant_{:%Y-%m}.csv".format(now)

# Vérifier si un montant a déjà été saisi pour le mois en cours
try :
        with open(fichier, "r") as f:
            #verifier un montant a déjà été saisi pour le mois en cours
            lines = f.readlines()
            if len(lines) > 1:
                print("Vous avez déjà saisi un montant pour le mois en cours")
                print("Veuillez consulter le fichier", fichier, "la saisie d'un nouvau montant n'est pas autorisée")
                f.close()
                print ("Voulez-vous ajouter des dépenses réalisés dans la journée ?")
                print("1. Oui")
                print("2. Non")
                choix = int(input("Entrez votre choix: "))
                
        if choix == 1:
                    depenses_jour = float(input("Entrez le montant de vos dépenses de la journée: "))
                    ## verifier si le montant est supérieur à 0
                    if depenses_jour > 0:
                      #soustraire le montant de vos dépenses de la journée au montant de votre salaire
                      amountv = amount - depenses_jour
                      # Ouverture du fichier en mode lecture qui a été dans le mois   
                      with open(fichier, "r") as f:
                        # Lecture du contenu du fichier dans une variable
                         contenu = f.read()
                         if(contenu != ""):
                              # Ouverture du fichier en mode écriture
                          with open(fichier, "a") as fi:
                                  # Mise à jour du montant dans la variable
                                nouveau_montant = amountv
                                date = "{:%Y-%m-%d }".format(now)
                                devise = choice
                                montant_restant = amountv - depenses_jour
                                nouvelle_ligne = "{}, {}, {},{}\n".format(nouveau_montant, date, devise, depenses_jour, montant_restant)
                                contenu_mis_a_jour = contenu + nouvelle_ligne
                                fi.write(contenu_mis_a_jour)
                                print("Montant enregistré avec succès !")
        if choix == 2:
            print("Merci d'avoir utilisé notre application")
            exit()
except FileNotFoundError: 
    # Ouverture du fichier en mode écriture
      with open(fichier, "w") as fichier:
        # Écriture des en-têtes de colonnes
        fichier.write("montant,date,devise,motif, montant_restant\n")
    
        # Écriture des données de saisie de montant
  
        montant = amount
        date = "{:%Y-%m-%d }".format(now)
        devise = choice
        motif = input("Entrez le motif: ")
        montant_restant = amount - depenses_jour

        ligne = "{},{},{}, {}\n".format(montant, date, devise, motif, montant_restant)
        fichier.write(ligne)
        print("Fichier créé avec succès !")
        
   
  
    
     

            
             





