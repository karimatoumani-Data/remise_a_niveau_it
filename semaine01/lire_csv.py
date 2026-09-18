import csv

with open("ventes.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    total = 0
    for ligne in lecteur:
        produit = ligne["produit"]
        prix = float(ligne["prix"])
        quantite = int(ligne["quantite"])

        chiffre_affaires = prix * quantite
        total+=chiffre_affaires
        print(produit, ":", chiffre_affaires, "€")
        if chiffre_affaires > 500 :
            print("  → Vente importante")
    print("le chiffre d'affaire total est : " ,total)