import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [options, setOptions] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOptions = async () => {
      try {
        const response = await axios.get('http://localhost:5000/options'); // "proxy" : "http://localhost:5000", didnt work idk
        setOptions(response.data);  
        console.log(response.data)
      } catch (err) {
        setError('Error fetching options');
        console.error('Error:', err);
      }
    };

    fetchOptions();
  }, []);  // Run only once when the component mounts


  const [inputChoice, setChoice] = useState("");

  return (
    <>
      <input 
      value={inputChoice}
      onChange={e => setChoice(e.target.value)}
      placeholder='Action'
      disabled={true}>
      </input>
      <br></br>
      <br></br>

      <div>
      {options.map((opt, i) => (
        <button key={i} onClick={() => setChoice(opt)}>
          {opt}
        </button>
      ))}
      </div>
      <br></br>

      <button>Confirm</button>

      
      </>
  )
}

export default App
