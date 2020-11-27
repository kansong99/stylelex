import React, {useState, useEffect} from 'react';
import './App.css';
import {SolutionPage} from './Pages/SolutionPage';

function App() {
  const [sol, setSol] = useState([])
  useEffect(()=> {
    fetch('/').then(
      response => {
        if(response.ok){
          return response.json()
        }
      }).then(data => console.log(data))
  }, []);

  return (
    <div className="App">
      <SolutionPage/>
    </div>
  );
}

export default App;
