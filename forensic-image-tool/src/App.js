import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import Results from "./components/Results";

function App() {
  const [results, setResults] = useState(null);

  return (
    <div className="App">
      <h1>Digital Forensic Tool for Images</h1>
      <UploadForm setResults={setResults} />
      <Results results={results} />
    </div>
  );
}

export default App;
