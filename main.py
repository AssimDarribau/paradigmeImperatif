# Partie 1
def donnees():
    noms = []
    notes = []

    nb_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))

    for i in range(nb_etudiants):
        nom = input(f"Nom de l’étudiant {i + 1} : ")
        note = float(input(f"Note de {nom} (sur 20) : "))
        noms.append(nom)
        notes.append(note)

    return noms, notes



# Partie 2
def calculer_moyenne(notes):
    total = sum(notes)  
    moyenne = total / len(notes)
    return moyenne



# Partie 3
def afficher_repartition(noms, notes):
    print("\nÉtudiants ayant réussi (note >= 10) :")
    for i in range(len(notes)):
        if notes[i] >= 10:
            print(noms[i])

    print("\nÉtudiants en échec (note < 10) :")
    for i in range(len(notes)):
        if notes[i] < 10:
            print(noms[i])



# Partie 4
def meilleure_note(noms, notes):
    meilleure = max(notes)  
    indice = notes.index(meilleure)  
    print(f"\nL’étudiant ayant la meilleure note est {noms[indice]} avec {meilleure}.")



# Main
def main():
    noms, notes = donnees()

    # Calcul de la moyenne
    moyenne = calculer_moyenne(notes)
    print(f"\nLa moyenne de la classe est de {moyenne}.")

    afficher_repartition(noms, notes)

    meilleure_note(noms, notes)


if __name__ == "__main__":
    main()
