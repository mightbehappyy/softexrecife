const Banco = function(conta, saldo, tipo, agencia){
    gConta = conta,
    gSaldo = saldo,
    gTipo = tipo,
    gAgencia = agencia

    this.getSaldo = function(){
        return gSaldo;
    }
    this.deposito = function(dinheiro){
        gSaldo += dinheiro;
    }
    this.saque = function(dinheiro){
        gSaldo -= dinheiro;
    }
    this.getNumero = function(){
        return agencia
    }
}

const novoBanco = new Banco("05", 500, "Conta corrente",  "404");
console.log(novoBanco.getSaldo())
console.log(novoBanco.getNumero())
novoBanco.deposito(5)
console.log(novoBanco.getSaldo())
novoBanco.saque(100)
console.log(novoBanco.getSaldo())
