from Tipo import Tipo
from Rareza import Rareza
from Coleccion import Coleccion
from Estado import Estado

class Arma(object):
    def __init__(self, tipo, nombre, rareza, coleccion, Float, precio,
                 estado=Estado.RecienFabricado):
        self.tipo = tipo
        self.nombre = nombre
        self.rareza = rareza
        self.coleccion = coleccion
        self.precio = precio

        if precio<0.0:
            print("E: el precio debe ser mayor que 0.0")

        if 0.0<Float<=1.0:
            self.Float = Float

            if 0.0<Float<0.07:
                estado=Estado.RecienFabricado
            elif 0.07<=Float<0.15:
                estado=Estado.CasiNuevo
            elif 0.15<=Float<0.38:
                estado=Estado.AlgoDesgastado
            elif 0.38<=Float<0.45:
                estado=Estado.BastanteDesgastado
            elif 0.45<=Float<=1:
                estado=Estado.Deplorable

            self.estado=estado   
            
        else:
            print("E: el float debe ser mayor que 0.0 y menor o igual a 1.0")

#"""PROBADOR
armas=[]
a=Arma(Tipo.AUG,"Sweeper",Rareza.Consumidor,
            Coleccion.Inferno2018,0.1,0.02)
print(a.tipo.name,a.nombre,a.rareza.name,a.coleccion.name,
      a.estado.name,"(",a.Float,")",a.precio,"€")
#print(a.tipo,a.nombre,a.rareza,a.estado.value,"debe ser 0.0...")
#a=Arma(Tipo.MP7)
#"""
