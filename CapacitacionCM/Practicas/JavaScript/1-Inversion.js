let cantidad = parseFloat(prompt("Ingresar la candad a invertir: "));
let interes_anual = parseFloat(prompt("Ingresar interes anual en %: "));
let anos = parseFloat(prompt("Ingresar el numero de anos de la inversion: "));

let capital = cantidad * Math.pow (1 + interes_anual / 100, anos);

console.log ("EL capital obtenido en la inversion es: " + capital.toFixed(2));