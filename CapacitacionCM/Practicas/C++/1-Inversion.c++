#include<iostream>
#include<cmath>
using namespace std;

int main () {
    float cantidad, interes_anual, capital;
    int anos;

    cout << "Ingresar la candad a invertir: ";
    cin >> cantidad;

    cout << "Ingresar interes anual en (%): ";
    cin >> interes_anual;

    cout << "Ingresar el numero de anos de la inversion: "
    cin >> anos;

    capital = cantidad * pow(1+ interes_anual / 100, anos);

    cout << "EL capital obtenido en la inversion es: " << round(capital * 100) / 100 << end1;
    
    return 0;
}