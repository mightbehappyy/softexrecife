const mysql = require('mysql');
const connection = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  password: 'sua_senha',
  database: "nome_do_banco_de_dados"
});

connection.connect((error) => {
  if(error){
    console.log('Erro ao conectar');
    return;
  }
  console.log('Conectado');
});
connection.end((error) => {
});
