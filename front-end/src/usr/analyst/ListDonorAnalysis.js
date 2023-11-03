import React, { useState } from 'react';
import backendApi from '../api';

const DiseaseList = () => {
  const [donorId, setDonorId] = useState(''); // State to hold the donor ID
  const [diseases, setDiseases] = useState([]); // State to hold the list of diseases

  // Function to fetch diseases for a specific donor
  const fetchDiseases = async () => {
    try {
      const response = await fetch(backendApi + '/list_donor_diseases', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ donor_id: donorId })
      });

      const data = await response.json();
      setDiseases(data.diseases); // Assuming the response format is { diseases: [] }
    } catch (error) {
      console.error('Error fetching diseases:', error);
    }
  };

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    fetchDiseases();
  };

  return (
    <div>
      <h2>List of Diseases for a Donor</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="donorId">Enter Donor ID:</label>
        <input
          type="text"
          id="donorId"
          value={donorId}
          onChange={(e) => setDonorId(e.target.value)}
          required
        />
        <button type="submit">Submit</button>
      </form>

      <h3>Diseases:</h3>
      <ul>
        {diseases.map((disease, index) => (
          <li key={index}>{disease}</li>
        ))}
      </ul>
    </div>
  );
};

export default DiseaseList;
