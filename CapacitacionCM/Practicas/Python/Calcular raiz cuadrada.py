

#TITULO - Raiz cuadrada con metodo de newton
print ("################ - metodo de newton - #######################")


#VARIABLE PARA CALCULAR LA RAIZ CUADRADA A ELECCION
n1 = float (input( "Ingrese la raiz cuadrada = "))
#VARIABLE QUE MULTIPLICADO POR 2 SE APROXIME A LA RAIZ SELECCIONADA
a1 = int (input( "Ingrese un valor entero que la raiz sea aproximado a su raiz cuadrada = ")) 

#FORMULA PARA EL CALCULO QUE REALIZARA LA OPERACION
a1 = (a1 + n1 / a1) /2

#IMPRIME POR PANTALLA EL RESULTADO
print ("La raíz cuadrada de",n1,  "es:", a1)




#print (15/5*7+(5+3)-2/5)




