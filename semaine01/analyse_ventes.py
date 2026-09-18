ventes = [
    {"produit": "Ordinateur", "prix": 800, "quantite": 2},
    {"produit": "Souris", "prix": 25, "quantite": 10},
    {"produit": "Clavier", "prix": 50, "quantite": 5},
    {"produit": "Écran", "prix": 300, "quantite": 3},
]

print("Analyse des ventes")
print("------------------")

total = 0
meilleure_vente = None
meilleur_produit = None

for vente in ventes:
    chiffre_affaires = vente["prix"] * vente["quantite"]
    total+=chiffre_affaires
    if meilleure_vente is None or chiffre_affaires > meilleure_vente:
        meilleure_vente = chiffre_affaires
        meilleur_produit = vente["produit"]
    print(vente["produit"], ":", chiffre_affaires, "€")

print("------------------")
print("Chiffre d'affaires total :", total, "€")
print("Meilleure vente :",meilleur_produit,"--", meilleure_vente, "€")

    