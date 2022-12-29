import logo from './logo.svg';
import './App.css';
import HelloWorld from './componentes/HelloWorld';
import BoaNoite from './componentes/BoaNoite';

const totalCount = document.getElementById("total-count");
var count = 0;
totalCount.innerHTML = count;
const increment = document.getElementById("button");
increment.addEventListener("click", handleIncrement);

const handleIncrement = () => {
  count++;
  totalCount.innerHTML = count;
  console.log(count);
}

function App() {
  return (
    <div className="App">
      <h1>Bom dia</h1>
      <HelloWorld/>
      <BoaNoite nome="Pedro"/>
      <BoaNoite nome="Joao"/>
      <BoaNoite nome="Gabriel"/>
      <script src="app.js" defer></script>
      <button>Aumentar</button>
    </div>
  );
}

export default App;
