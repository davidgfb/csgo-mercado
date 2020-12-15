from enum import Enum

class Estado(Enum):
    RecienFabricado = 0.0
    CasiNuevo = 0.07
    AlgoDesgastado = 0.15
    BastanteDesgastado = 0.38
    Deplorable = 0.45

"""PROBADOR
print(Estado.RecienFabricado.value,"debe ser 0.0")
"""

class Status(Enum):
    FactoryNew = 0.0
    MinimalWear = 0.07
    FieldTested = 0.15
    WellWorn = 0.38
    BattleScarred = 0.45

"""PROBADOR
print(Status.FactoryNew.value,"debe ser 0.0")
"""


