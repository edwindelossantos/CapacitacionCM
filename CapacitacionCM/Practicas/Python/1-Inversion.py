


cantidad = float(input("Ingresar la candad a invertir: "))
interes_anual = float(input("Ingresar interes anual en %: "))
anos = float(input("Ingresar el numero de anos de la inversion: "))

capital = cantidad *(1 + interes_anual / 100) ** anos

print("EL capital obtenido en la inversion es: ",round(capital,2))