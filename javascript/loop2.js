const guitarra = {
    cor: "Amarela",
    braco: "Maple",
    marca: "Fender",
    modelo: "Telecaster"
}

const estudantes = ["Gabriel", "Jamu", "Higor"]

function primeira(objeto){
    for(var i in guitarra){
        console.log(objeto[i])
    }

}

function segunda(estu){
    for (var i in estu){
        console.log(estu[i])
    }
    
}

segunda(estudantes)
primeira(guitarra)
