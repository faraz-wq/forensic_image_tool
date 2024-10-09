import React from "react";

function Results({ results }) {
  if (!results) return null;

  return (
    <div>
      <h3>Metadata:</h3>
      <pre>{JSON.stringify(results.metadata, null, 2)}</pre>

      <h3>Tampering Analysis:</h3>
      <p>Noise Level: {results.tampering_analysis.noise_level}</p>
      <img
        src={`http://localhost:5000/${results.tampering_analysis.ela_image_path}`}
        alt="ELA Result"
      />
    </div>
  );
}

export default Results;
