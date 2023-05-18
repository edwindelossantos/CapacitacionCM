

#Raiz cuadrada con metodo de newton
print ("################ - metodo de newton - #######################")


n1 = float (input( "Ingrese la raiz cuadrada = "))
a1 = int (input( "Ingrese un valor entero que la raiz sea aproximado a su raiz cuadrada = ")) 
precision = 0.0001  # Precisión de 4 decimales


raiz = (n1,precision)
a1 = (a1 + n1 / a1) /2


#b1 = (a1*a1)

print ("La raíz cuadrada de",n1,  "es:", a1)




#print (15/5*7+(5+3)-2/5)




