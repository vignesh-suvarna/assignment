import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [fizzBuzzList, setFizzBuzzList] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/fizzbuzz') // fetching the API 
      .then(response => response.json())
      .then(data => {
        console.log(data); // Optional line of code to check for outputs in the console
        setFizzBuzzList(data);
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div className="App">
      <h1>FizzBuzz</h1>
      <ul>
        {fizzBuzzList.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
