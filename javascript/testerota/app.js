const express =  require('express')

const app = express();

app.get('/',(req, res) =>{
    res.send('<h1>Nosso primeiro servidor<h1>')
})

app.get('/json', (req,res)=>{
    res.json({Tittle:"Nosso primeiro server", online: true})
})

app.listen(3000, () => {
    console.log("Servidor iniciado!")
})
