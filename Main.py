from Tipo import Tipo
from Rareza import Rareza
from Coleccion import Coleccion
#from Estado import Estado
from Arma import Arma

armas=[]
a=Arma(Tipo.AUG,"Sweeper",Rareza.Consumidor,
       Coleccion.Inferno2018,0.1,0.02)
print(a.tipo.name,a.nombre,a.rareza.name,a.coleccion.name,
      a.estado.name,"(",a.Float,")",a.precio,"€")
#print(a.tipo,a.nombre,a.rareza,a.estado.value,"debe ser 0.0...")
#a=Arma(Tipo.MP7)

