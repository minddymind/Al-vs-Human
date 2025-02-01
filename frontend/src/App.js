import React, { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState(""); // Store user input text
  const [result, setResult] = useState(null); // Store the response data
  const [isLoading, setIsLoading] = useState(false);  // Loading state

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);  // Start loading

    try {
      // Send POST request to Flask server
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: text }),  // Send text data to server
      });

      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }

      const data = await response.json();  // Parse JSON response from server
      setResult(data);  // Set the result with data received from Flask server
    } catch (error) {
      console.error("Error fetching data: ", error);
      setResult(null);  // Optionally reset result on error
    } finally {
      setIsLoading(false);  // Stop loading
    }
  };

  return (
    <div className="App">
      <h1 style={{marginTop: "8rem"}}>Review Detector</h1>
      <div className="box">
        <p>The purpose of this website is to detect reviews of products in the <b className="text">Health and Personal care category</b>, which include skincare, 
          vitamins, and other products that may be harmful to the human body if they do not meet the standard or 
          are too over-reviewed on an e-commerce website.
        </p>
      </div>
      <div className="pbox" style={{marginTop: "2rem"}}>
        <form onSubmit={handleSubmit}>
          <textarea
            id="predict-text"
            value={text}
            onChange={(e) => setText(e.target.value)}  // Handle text input
            placeholder="input your text here"
            rows={5}
          />
          <button className="button" style={{marginTop: "1rem"}} type="submit" disabled={isLoading}>
            {isLoading ? "Predicting..." : "Predict"}
          </button>
        </form>
      </div>

      {result && !isLoading && (
        <div>
          <h2>Result:</h2>
          <p><b 
            style={{
              color: result.Human > result.AI ? "green" : "black", 
              backgroundColor: result.Human > result.AI ? "lightgreen" : "transparent",
              padding: "5px",
              borderRadius: "5px"
            }}
          >
            Human: {result.Human ? result.Human.toFixed(2) : 0}%
          </b></p>
          
          <p><b 
            style={{
              color: result.AI > result.Human ? "red" : "black", 
              backgroundColor: result.AI > result.Human ? "pink" : "transparent",
              padding: "5px",
              borderRadius: "5px"
            }}
          >
            AI: {result.AI ? result.AI.toFixed(2) : 0}%
          </b></p>
        </div>
      )} 
    </div>
  );
}

export default App;
