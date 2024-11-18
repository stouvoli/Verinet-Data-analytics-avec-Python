# -*- coding: utf-8 -*-
"""Formation data analytics chapitre 1 et 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TNWKAhrxMEeh9bht8ao5RqoA3h6HKX22
"""

try:
  print(0/0)
except ZeroDivisionError:
  print("Cannot divide by zero")
else:
  print("Division successful")
finally:
  print("This will always execute")

"""# Liste"""

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)  # égale 3
list_sum = sum(integer_list)  # égale 6

x = list(range(10))  # est la liste [0, 1, ..., 9]
zero = x[0]  # égale 0, les listes sont indexées à partir de 0
one = x[1]  # égale 1
nine = x[-1]  # égale 9, version 'pythonique' pour le dernier élément
eight = x[-2]  # égale 8, version 'pythonique' pour l’avant-dernier élément
x[0] = -1  # maintenant x vaut [-1, 1, 2, 3, ..., 9]

first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]

x = [1, 2, 3]
x.extend([4, 5, 6])  # x vaut maintenant [1,2,3,4,5,6]

x = [1, 2, 3]
y = x + [4, 5, 6]  # y vaut [1, 2, 3, 4, 5, 6]; x est inchangé

x = [1, 2, 3]
x.append(0)  # x vaut maintenant [1, 2, 3, 0]
y = x[-1]  # égale 0
z = len(x)  # égale 4

x, y = [1, 2]  # maintenant x vaut 1, y vaut 2
_, y = [1, 2]  # maintenant y == 2, peu importe le premier élément

# Création de tuples
my_tuple = (1, 2)
other_tuple = 3, 4

# Assignations multiples
x, y = 1, 2
print(x, y)  # Output: 1 2

# Échange de valeurs
x, y = y, x
print(x, y)  # Output: 2 1

# Fonction retournant un tuple
def sum_and_product(x, y):
    return (x + y), (x * y)

s, p = sum_and_product(2, 3)
print(s, p)  # Output: 5 6

# Création d'un dictionnaire
grades = {"Joel": 80, "Tim": 95}

# Accès à une valeur
joels_grade = grades["Joel"]
print(joels_grade)  # Output: 80

# Vérification d'existence
joel_has_grade = "Joel" in grades
print(joel_has_grade)  # Output: True

# Valeur par défaut
kates_grade = grades.get("Kate", 0)
print(kates_grade)  # Output: 0

# Modification
grades["Tim"] = 99
print(grades)  # Output: {'Joel': 80, 'Tim': 99}

# Itération
for key, value in grades.items():
    print(key, value)

from collections import defaultdict

word_counts = defaultdict(int)
for word in document:
   word_counts[word] += 1

from collections import Counter
# Compter les mots dans un document
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)

# Afficher les 3 mots les plus fréquents
for word, count in word_counts.most_common(3):
    print(word, count)

s = set()
s.add(1)
s.add(2)
# Vérification d'appartenance
print(2 in s)  # Output: True
# Suppression des doublons
item_list = [1, 2, 3, 1, 2, 3]
item_set = set(item_list)
distinct_item_list = list(item_set)
print(distinct_item_list)  # Output: [1, 2, 3]

all([True, 1, { 3 }]) # Vrai
all([True, 1, {}]) # Faux, {} est plutôt faux
any([True, 1, {}]) # Vrai, True est plutôt vrai
all([]) # Vrai, pas d’éléments plutôt faux dans la liste
any([]) # Faux, pas d’éléments plutôt vrais dans la liste

10/5

10//5

1 == 2

sorted([-4,1,-2,3], key=abs, reverse=True)

pairs = [(x, y)
    for x in range(10)
    for y in range(10)] # 100 paires (0,0) (0,1) ... (9,9)

pairs

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for i in my_range(10):
    print(i)

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # TODO Implement your generator function here
    for element in iterable:
        yield start, element
        start += 1


for i, lesson in my_enumerate(lessons, 5):
    print("Lesson {}: {}".format(i, lesson))

def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]



for chunk in chunker(range(25), 4):
    print(list(chunk))

import random

# Générer un nombre aléatoire entre 0 et 1
nombre_aleatoire = random.random()
print(nombre_aleatoire)

# Générer un entier aléatoire entre 1 et 10 (inclus)
entier_aleatoire = random.randint(1, 10)
print(entier_aleatoire)

# Mélanger une liste
liste = [1, 2, 3, 4, 5]
random.shuffle(liste)
print(liste)

# Choisir un élément aléatoirement dans une liste
liste = [1, 2, 3, 4, 5]
element_choisi = random.choice(liste)
print(element_choisi)

import re

# Vérification 1: 'cat' ne commence pas par 'a'
check1 = not re.match("a", "cat")

# Vérification 2: 'cat' possède un 'a'
check2 = re.search("a", "cat")

# Vérification 3: 'dog' ne contient pas de 'c'
check3 = not re.search("c", "dog")

# Vérification 4: 'carbs' se coupe en 'a' ou 'b' en ['c', 'r', 's']
check4 = 3 == len(re.split("[ab]", "carbs"))

# Vérification 5: remplace les chiffres par des tirets dans "R2D2"
check5 = "R-D-" == re.sub("[0-9]", "-", "R2D2")

# Afficher si toutes les vérifications sont vraies
print(check1 and check2 and check3 and check4 and check5)

re.split("[ab]", "carbs")

# Calculer le carré de chaque nombre dans une liste
carres = map(lambda x: x**2, [1, 2, 3, 4, 5])

# Filtrer les nombres pairs d'une liste
pairs = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])

# Créer une liste des nombres impairs inférieurs à 10
impairs = [x for x in range(10) if x % 2 != 0]

pairs

list(pairs)

for i in pairs:
  print(i)

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']

for x, y in zip(liste1, liste2):
    print(x, y)

def somme(x, y, z):
    return x + y + z

liste = [1, 2, 3]
resultat = somme(*liste)  # Équivalent à somme(1, 2, 3)
print(resultat)  # Affiche 6

paires = [(1, 'a'), (2, 'b'), (3, 'c')]
liste1, liste2 = zip(*paires)
print(liste1)  # Affiche (1, 2, 3)
print(liste2)  # Affiche ('a', 'b', 'c')

def magic(*args, **kwargs):
    print("args sans nom :", args)
    print("args mots-clés :", kwargs)

magic(1, 2, key="word", key2="word2")
# affiche
# args sans nom : (1, 2)
# args mots-clés : {'key2': 'word2', 'key': 'word'}

# Calculer le carré de chaque nombre dans une liste
carres = map(lambda x: x**2, [1, 2, 3, 4, 5])

# Filtrer les nombres pairs d'une liste
pairs = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])

for i in pairs:
  print(i)

for j in carres:
  print(j)