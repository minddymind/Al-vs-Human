import React, { useState } from "react";

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
    <div>
      <h1 >AI vs Human Text Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}  // Handle text input
          placeholder="พิมพ์ข้อความที่นี่"
          rows={5}
          cols={50}
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? "กำลังทำนาย..." : "ทำนาย"}
        </button>
      </form>

      {/* Conditional rendering based on result */}
      {isLoading && !result && <div>กำลังทำนาย...</div>}  {/* Loading message */}
      
      {result && !isLoading && (
        <div>
          <h2>ผลลัพธ์:</h2>
          <p>มนุษย์: {result.Human ? result.Human.toFixed(2) : 0}%</p>  {/* Display Human percentage */}
          <p>AI: {result.AI ? result.AI.toFixed(2) : 0}%</p>  {/* Display AI percentage */}
        </div>
      )}

      {/* Optional error message */}
      {result === null && !isLoading && <p>เกิดข้อผิดพลาดบางประการ</p>}  {/* Error message */}
    </div>
  );
}

export default App;
