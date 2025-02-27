def andComparar(a, b):
    if (a and b):
        return "Ambos son verdaderos"
    else:
        return "Al menos uno es falso"
    
def orComparar(a, b):
    if (a or b):
        return "Al menos uno es verdadero"
    else:
        return "Ambos son falsos"
    
def notComparar(a):
    if (a==True):
        return "Es falso"
    else:
        return "Es verdadero"