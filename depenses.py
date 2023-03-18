import datetime

devises = ['dollar', 'euro', 'yen', 'pound', 'franc CFA']

# Afficher la liste des devises disponibles
print("Les devises disponibles sont :")
for devise in devises:
    print("-", devise)

# Demander à l'utilisateur de choisir une devise
choice = input("Entrez le nom de votre devise : ")

# Vérifier si le choix de l'utilisateur est valide
if choice not in devises:
    print("Devise invalide, veuillez réessayer")

    # Tant que le choix de l'utilisateur n'est pas valide, demander à l'utilisateur de choisir une devise
    # Nombre d'essais
    nb_essais = 0
    while choice not in devises:
        choice = input("Entrez le nom de votre devise : ")
        # Incrémenter le nombre d'essais
        nb_essais += 1
        # Vérifier si le nombre d'essais est supérieur à 3
        if nb_essais > 3:
            print("Vous avez dépassé le nombre de tentatives autorisées")
            exit()

else:
    print("Vous avez choisi la devise", choice)

# Demander à l'utilisateur de saisir un montant
amount = float(input("Entrez un montant : "))

# Vérifier si le montant est supérieur à 0
if amount <= 0:
    print("Le montant doit être supérieur à 0")
    exit()

# Obtenir la date du jour
now = datetime.datetime.now()

# Créer une variable pour la date de saisie du montant de votre salaire
date_salaire = now.strftime("%d-%m-%Y")

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
                                nouvelle_ligne = "{}, {}, {}\n".format(nouveau_montant, date, devise)
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
        fichier.write("montant,date,devise,motif\n")
    
        # Écriture des données de saisie de montant
  
        montant = amount
        date = "{:%Y-%m-%d }".format(now)
        devise = choice
        motif = input("Entrez le motif: ")

        ligne = "{},{},{}\n".format(montant, date, devise, motif)
        fichier.write(ligne)
        print("Fichier créé avec succès !")
        
   
  
    
     

            
             




