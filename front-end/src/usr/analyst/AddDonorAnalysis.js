import React, { useState } from 'react';
import backendApi from '../api';

const AddDonorAnalysis = () => {
  const [formData, setFormData] = useState({
    donorId: '',
    diseases: [],
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleMultiSelectChange = (e) => {
    const options = e.target.options;
    const selectedDiseases = [];
    for (let i = 0; i < options.length; i++) {
      if (options[i].selected) {
        selectedDiseases.push(options[i].value);
      }
    }
    setFormData({
      ...formData,
      diseases: selectedDiseases,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);

    // Send the form data to your backend here
    fetch(backendApi + '/add_donor_analysis', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Success:', data);
        // Handle success response from the backend
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle error from the backend
      });
  };

  return (
    <div>
      <h2>Add Donor Analysis</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="donorId">Donor ID:</label>
          <input
            type="text"
            id="donorId"
            name="donorId"
            value={formData.donorId}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="diseases">Diseases:</label>
          <select
            id="diseases"
            name="diseases"
            multiple
            value={formData.diseases}
            onChange={handleMultiSelectChange}
            required
          >
            <option value="Hepatitis B">Hepatitis B</option>
            <option value="Hepatitis C">Hepatitis C</option>
            <option value="HIV">HIV</option>
            <option value="Syphilis">Syphilis</option>
            <option value="Malaria">Malaria</option>
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddDonorAnalysis;
