"""
Module d'encodage de chaînes de caractères (RLE).

Ce module propose deux implémentations (itérative et récursive)
de l'algorithme Run-Length Encoding pour compresser des chaînes
en une liste de tuples (caractère, nombre d'occurrences).
"""

#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s: str) -> list[tuple[str, int]]:
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list[tuple[str, int]]: la liste des tuples (caractère, nombre d'occurences)
    """
    # Cas de base : chaîne vide
    if not s:
        return []

    resultat = []
    caractere_courant = s[0]
    compteur = 1

    for c in s[1:]:
        if c == caractere_courant:
            compteur += 1
        else:
            resultat.append((caractere_courant, compteur))
            caractere_courant = c
            compteur = 1

    resultat.append((caractere_courant, compteur))

    return resultat


def artcode_r(s: str) -> list[tuple[str, int]]:
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list[tuple[str, int]]: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base : chaîne vide
    if not s:
        return []

    # recherche nombre de caractères identiques au premier
    caractere = s[0]
    n = 1
    # On compte tant que le caractère suivant est identique et qu'on ne dépasse pas la longueur
    while n < len(s) and s[n] == caractere:
        n += 1

    # appel récursif
    # On retourne le tuple courant + le résultat de l'appel sur le reste de la chaîne
    return [(caractere, n)] + artcode_r(s[n:])


#### Fonction principale


def main() -> None:
    """
    Fonction principale de test.
    Affiche le résultat de l'encodage itératif et récursif.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


if __name__ == "__main__":
    main()
