import React, { useState } from "react";
import axios from "axios";

function UploadForm({ setResults }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "http://localhost:5000/upload",
      formData,
      {
        headers: { "Content-Type": "multipart/form-data" },
      },
    );
    setResults(response.data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileChange} />
      <button type="submit">Upload</button>
    </form>
  );
}

export default UploadForm;
