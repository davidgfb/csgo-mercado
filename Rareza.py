from enum import Enum

class Rareza(Enum):
    Consumidor=0
    Industrial=1
    Militar=2
    Restringido=3
    Clasificado=4
    Encubierto=5
    Contrabando=6

"""PROBADOR
print(Rareza.Consumidor.value, "debe ser 0")
"""

class Rarity(Enum):
    Consumer=0
    Industrial=1
    MilSpec=2
    Restricted=3
    Classified=4
    Covert=5
    Contraband=6

"""PROBADOR
print(Rarity.Consumer.value, "debe ser 0")
"""
