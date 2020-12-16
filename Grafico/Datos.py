from Grafico import pintaGrafico

def pideDatos():
    xs=[]
    ys=[]
    nPuntos=input("Introduce nPuntos:")

    print(20*"-")

    for i in range(int(nPuntos)):
        x=float(input("Introduce x:"))
        y=float(input("Introduce y:"))

        print(20*"-")
        
        xs.append(x)
        ys.append(y)

    return [xs,ys]

"""
x=[0.2,0.22,0.23,0.26,0.29] #float promedio
y=[23.9,-0.9,23.9,11,11] #porcentaje beneficio
print("xs:",xs,
      "\nys:",ys)

xs,ys=pideDatos()



pintaGrafico(xs,ys,"Float promedio (0.0-1.0)",
           "Porcentaje beneficio (%)")

from statistics import mean
xs=[]
print("float medio:",mean(xs))
"""


