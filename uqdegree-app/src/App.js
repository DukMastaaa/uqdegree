import './App.css';
//import MyButton from './Components/MyButton.js'
import Table from './Components/Table';
import { Update } from './Components/Update';

function App() {

  const list = [
    { title: '', id: 0 },
    { title: 'COSC3500', id: 1 },
    { title: 'MATH1071', id: 2 },
    { title: 'ECON1010', id: 3 },
  ];

  return (
    <div className="App">
      <Table products = {list}/>
    </div>
  );
}

export default App;
