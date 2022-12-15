const num1 = prompt("Digite um numero ");
const num2 = prompt("Digite outro numero ");
const operador = prompt("Digite o operador");
if (operador == "+"){
    console.log(num1 + num2);
}
if (operador == "-") {
    console.log(num1 + num2);
}
if (operador == "*"){
    console.log(num1 * num2);
}
else{
    console.log(num1 / num2);
    console.log("A sobra foi: ", num1 % num2);
}
