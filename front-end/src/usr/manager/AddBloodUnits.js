// AddBloodUnit.js

import React, { useState } from 'react';
import backendApi from '../../App'

const AddBloodUnit = () => {
  const [formData, setFormData] = useState({
    DonorID: '',
    AnalystID:'',
    status: '',
    NumberOfUnits: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send the form data to the backend
    fetch(backendApi + '/add_blood_unit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="DonorID">Donor ID:</label>
        <input
          type="text"
          id="DonorID"
          name="DonorID"
          value={formData.DonorID}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="AnalystID">Analyst ID:</label>
        <input
          type="text"
          id="AnalystID"
          name="AnalystID"
          value={formData.AnalystID}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="NumberOfUnits">Number Of Units:</label>
        <input
          type="number"
          id="NumberOfUnits"
          name="NumberOfUnits"
          value={formData.DonorID}
          onChange={handleInputChange}
        />
      </div>
      <div>
      <label htmlFor="status">Status</label>
      <select
        name="status"
        value={formData.status}
        onChange={handleInputChange}
        >
        <option value="">Blood Unit Status</option>
        <option value="InStock">InStock</option>
        <option value="Utilised">Utilised</option>
        <option value="Expired">Expired</option>
        <option value="Reserved">Reserved</option>
        </select>
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default AddBloodUnit;
