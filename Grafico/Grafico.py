from matplotlib.pyplot import plot,show,xlabel,ylabel,hlines

def pintaGrafico(x,y,etiquetaX,etiquetaY):   
    maxY=max(y)
    minX=min(x)
    maxX=max(x)

    print("maxY:",maxY,", minX:",minX,", maxX",maxX)

    xlabel(etiquetaX)
    ylabel(etiquetaY)
    
    hlines(y=maxY,xmin=minX,xmax=maxX)
    hlines(y=0,xmin=minX,xmax=maxX)

    plot(x,y,'bo')
    plot(x,y)

    show()







