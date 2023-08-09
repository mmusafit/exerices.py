def gestionne_spesa(items, values):
    n = len(items)
    liste_items = {}
    for i in range(n):
        item = items[i].upper()  # Convertir l'élément en majuscules
        if item not in liste_items:
            liste_items[item] = values[i]
        else:
            if n != values[i]:  # Correction de la condition
                liste_items[item] = values[i]
    return liste_items

# Test de la fonction
liste_items = ["pizza", "fagiolini", "pizza con tonno","spinnaci","carbonara","salsicia di bra","camomila"]
values = [1, 2, 3,4,5,6,7]
print(gestionne_spesa(liste_items, values))
