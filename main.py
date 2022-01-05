import json
import os
import sys


def create_project(path, d):
    os.chdir(path)  # de fiecare data cand se apeleaza functia se schimba path ul
    for k in d.keys():  # parcurgem pe rand toate cheile
        if isinstance(d[k], dict):  # verificam daca este un dictionar
            new_path = os.path.join(path, k) # cream un path nou unind numele path ului cu numele dictionarului
            os.mkdir(new_path)  # cream directorul
            create_project(new_path, d[k])  # se parcurge recursiv dictionarul gasit
            os.chdir(path)  # dupa ce am parcurs dictionarul respectiv revenim la path ul initial
        else:  # daca nu este un dictionar, vom crea fisierul si vom scrie in el continutul acestuia
            f = open(k, 'w')
            f.write(d[k])

if not os.path.exists(sys.argv[1]):  #daca nu exista directorul root, il cream
    os.mkdir(os.path.abspath(sys.argv[1]))

f = open(os.path.abspath(sys.argv[2]))
dictionary = json.load(f)  # deschidem jsonul si ii facem load

create_project(os.path.abspath(sys.argv[1]), dictionary)