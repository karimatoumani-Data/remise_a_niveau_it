ventes = [
    {"produit": "Ordinateur", "prix": 900, "quantite": 2},
    {"produit": "Ecran", "prix": 250, "quantite": 4},
    {"produit": "Clavier", "prix": 80, "quantite": 5},
    {"produit": "Souris", "prix": 40, "quantite": 8},
]
def calculer_ca_total(ventes):
    ca_total = 0
    meilleure_vente = ventes[0]

    for vente in ventes:
        montant = vente["prix"] * vente["quantite"]
        ca_total += montant

        meilleur_montant = (
            meilleure_vente["prix"] * meilleure_vente["quantite"]
        )

        if montant > meilleur_montant:
            meilleure_vente = vente

    montant_meilleure_vente = (
        meilleure_vente["prix"] * meilleure_vente["quantite"]
    )

    return montant_meilleure_vente, ca_total


meilleure_vente, ca_total = calculer_ca_total(ventes)

print(f"Chiffre d'affaires total : {ca_total}")
print(f"Montant de la meilleure vente : {meilleure_vente}")
        
        
        
