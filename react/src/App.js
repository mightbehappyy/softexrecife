import logo from './logo.svg';
import './App.css';
import HelloWorld from './componentes/HelloWorld';
import BoaNoite from './componentes/BoaNoite';

function App() {
  return (
    <div className="App">
      <h1>Bom dia</h1>
      <HelloWorld/>
      <BoaNoite nome="Pedro"/>
      <BoaNoite nome="Joao"/>
      <BoaNoite nome="Gabriel"/>
    </div>
  );
}

export default App;
