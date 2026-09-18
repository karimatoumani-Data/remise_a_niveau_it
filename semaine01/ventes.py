ventes = [
    {"produit": "Ordinateur", "prix": 900, "quantite": 2},
    {"produit": "Ecran", "prix": 250, "quantite": 4},
    {"produit": "Clavier", "prix": 80, "quantite": 5},
    {"produit": "Souris", "prix": 40, "quantite": 8},
]

def trouver_meilleure_vente(ventes):
    meilleurevente = ventes[0]
    for vente in ventes : 
        montant=vente["prix"] * vente["quantite"] 
        MV=meilleurevente["prix"] * meilleurevente["quantite"]
        if montant>MV :
            meilleurevente=vente
    return meilleurevente
resultat=trouver_meilleure_vente(ventes)
print("meilleure vente :",resultat)
print("meilleur prix :", resultat["prix"])

        
        
        
