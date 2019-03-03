def suma(numero):
    resultado = 0
    for i in range(0 , numero+1):
        resultado += i
    
    return resultado

print(suma(100))

def sumacuadrados(limite, f):
    resultado = 0
    for i in range(limite+1):
        resultado += f(i)
    return resultado

print(sumacuadrados(3))
 
def portres(i):
    return i*i
    