var decisao = prompt("Voce quer rodar o primeiro ou segundo programa? Digite 1 ou 2")
if (decisao == '1'){
    const nota1 = parseInt(prompt("Digite sua primeira nota"));
    const nota2 = parseInt(prompt("Digite sua segunda nota"));
    const nota3 = parseInt(prompt("Digite sua terceira nota"));
    
    function teste(n1, n2, n3){
        resultado = (n1+n2+n3)/3;
        if (resultado < 7){
            console.log("Reprovado");
        }
        else{
            console.log("Aprovado");
        }
    }
    teste(nota1,nota2,nota3)

}

else{
    function minima(n1,n2){
        falta = 21 - (n1 + n2);
        console.log("Voce devera tirar", falta,"na proxima prova")
    }
    
    n1 = parseInt(prompt("Digite a primeira nota"));
    n2 = parseInt(prompt("Digite a segunda nota"));
    
    minima(n1,n2)
}
