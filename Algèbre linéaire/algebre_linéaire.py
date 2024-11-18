# -*- coding: utf-8 -*-
"""Algebre linéaire

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16P65V5153rVO2QesxoR6nOXQF8XI6eHs
"""

from typing import List
Vector = List[float]
height_weight_age = [70,  # pouces
                     170, # livres
                     40]  # années

def add(v: Vector, w: Vector) -> Vector:
    """Additionne les éléments correspondants."""
    assert len(v) == len(w), "Les vecteurs doivent être de même longueur"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    """Soustrait les éléments correspondants."""
    assert len(v) == len(w), "Les vecteurs doivent être de même longueur"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Fait la somme de tous les éléments correspondants."""
    # Vérifier que les vecteurs ne sont pas vides.
    assert vectors, "Aucun vecteur fourni!"

    # Vérifier que les vecteurs sont tous de la même taille.
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Tailles différentes!"

    # L'élément i du résultat est la somme des éléments i de chaque vecteur.
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplie chaque élément par c."""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Calcule la moyenne élément par élément."""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    """Calcule v_1 * w_1 + ... + v_n * w_n."""
    assert len(v) == len(w), "Les vecteurs doivent être de même longueur"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

def sum_of_squares(v: Vector) -> float:
    """Retourne v_1 * v_1 + ... + v_n * v_n."""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3

import math
def magnitude(v: Vector) -> float:
    """Retourne la magnitude de v."""
    return math.sqrt(sum_of_squares(v))  # math.sqrt = racine carrée

assert magnitude([3, 4]) == 5

# def squared_distance(v: Vector, w: Vector) -> float:
#     """Calcule (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2."""
#     return sum_of_squares(subtract(v, w))

# def distance(v: Vector, w: Vector) -> float:
#     """Calcule la distance entre v et w."""
#     return math.sqrt(squared_distance(v, w))


# Ou, de manière plus concise :

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))

from typing import List

# Alias de type pour une matrice
Matrix = List[List[float]]

# Exemple de matrice 2x3 (2 lignes, 3 colonnes)
A = [[1, 2, 3],
     [4, 5, 6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """Retourne (nombre de lignes de A, nombre de colonnes de A)."""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # Nombre d'éléments dans la première ligne
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 lignes, 3 colonnes

def get_column(A: Matrix, j: int) -> Vector:
    """Retourne la colonne j de la matrice A (en tant que vecteur)."""
    return [A_i[j]  # Élément j de la ligne A_i
            for A_i in A]  # Pour chaque ligne A_i

def get_row(A: Matrix, i: int) -> Vector:
    """Retourne la ligne i de la matrice A (en tant que vecteur)."""
    return A[i]

from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Retourne une matrice num_rows x num_cols
    dont l'élément (i,j) est entry_fn(i, j).
    """
    return [[entry_fn(i, j)  # Étant donné i, créer une liste
             for j in range(num_cols)]  # [entry_fn(i, 0), ...]
            for i in range(num_rows)]  # Créer une liste pour chaque i

def identity_matrix(n: int) -> Matrix:
    """Retourne la matrice identité n x n."""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 1]]