#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict ()
moscow = sites ['Moscow']
london = sites ['London']
paris = sites ['Paris']
moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) **2) ** .5

moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5

london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1])**2) ** .5


distances ['moscow'] = {}
distances ['moscow'] ['london'] = moscow_london
distances ['moscow'] ['paris'] = moscow_paris

distances ['london'] = {}
distances ['london'] ['moscow'] = moscow_london
distances ['london'] ['paris'] = london_paris

distances ['paris'] = {}
distances ['paris'] ['moscow'] = moscow_paris
distances ['paris'] ['london'] = london_paris

pprint(distances)

# зачет!



