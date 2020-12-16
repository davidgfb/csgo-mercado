class Intercambio(object):    
    def __init__(self,armas):
        def coste(armas):
            c=0.0

            for a in armas:
                c+=a.precio

            return c

        def recibe():
            a=Arma(Tipo.G18,"Candy Apple",Rareza.Militar,
                   Coleccion.Italy,0.069,0.74) 
            #prob y float los calcularemos auto
            armas=a #[]
            return armas

        def beneficio(pRecepcion,coste):
            b=pRecepcion-coste
            porc=100.0*b/coste
            return [b,porc]
        
        if len(armas)==10:
            self.armas=armas
            coste=coste(armas)
            self.coste=coste
            recepcion=recibe()
            self.recepcion=recepcion
            self.beneficio=beneficio(recepcion.precio,coste)
        else:
            print("E: debe haber 10 armas para el intercambio")    

"""PROBADOR
from Arma import Arma
from Rareza import Rareza
from Coleccion import Coleccion
from Tipo import Tipo

a=Arma(Tipo.XM1014,"CaliCamo",Rareza.Industrial,Coleccion.Italy,
       0.2,0.05) #barata 7
a1=Arma(Tipo.G18,"Death Rattle",Rareza.Industrial,Coleccion.Bank,
        0.2,0.05) #cara 3
armas=[a,a,a,a,a,a,a,
       a1,a1,a1]
i=Intercambio(armas)

b,p=i.beneficio
print("Coste:",i.coste,"€\nRecibe:\n",
      i.recepcion.tipo.name,i.recepcion.nombre,
      i.recepcion.rareza.name,i.recepcion.coleccion.name,
      i.recepcion.estado.name,"(",i.recepcion.Float,")",
      i.recepcion.precio,"€",
      "\nBeneficio:", b, "€",
      "\nPorcentaje:", p, "%",)


for a in i.armas:
    
    repetidas=[]

    if not a in repetidas:
        repetidas.append(a)
    
    print(a.tipo.name,a.nombre,a.rareza.name,a.coleccion.name,
          a.estado.name,"(",a.Float,")",a.precio,"€")

"""

def beneficio(precios,probs): #esperanza
    b=0.0

    for i in range(len(precios)):
        prob=probs[i]
        precio=precios[i]
        b+=prob*precio

    return b
           
"""PROBADOR
"""
precios=[0.74,0.54,0.72,
         1.04,0.61,0.62]
"""
probs=[0.2333,0.2333,0.2333,
       0.1,0.1,0.1]
"""
probs=[7/30,7/30,7/30,
       0.1,0.1,0.1]
print("beneficio:",beneficio(precios,probs),"debe ser 0.69")




















