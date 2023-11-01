import React, { useState } from 'react';
import backendApi from '../../App'

function BloodRequest() {
  const [formData, setFormData] = useState({
    patientID: '',
    bloodGroup: '', // Updated from bloodType to bloodGroup
    quantity: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send a POST request to the backend to handle the blood request
    fetch(backendApi + '/make_blood_request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      // You can add code here to handle a successful request
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  return (
    <div>
      <h2>Make a Blood Request</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Patient ID:
          <input
            type="text"
            name="patientID"
            value={formData.patientID}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <label>
          Blood Group:
          <select
            name="bloodGroup"
            value={formData.bloodGroup}
            onChange={handleChange}
            required
          >
            <option value="">Select Blood Group</option>
            <option value="A+">A+</option>
            <option value="A-">A-</option>
            <option value="B+">B+</option>
            <option value="B-">B-</option>
            <option value="AB+">AB+</option>
            <option value="AB-">AB-</option>
            <option value="O+">O+</option>
            <option value="O-">O-</option>
          </select>
        </label>
        <br />
        <label>
          Quantity:
          <input
            type="number"
            name="quantity"
            value={formData.quantity}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <button type="submit">Submit Request</button>
      </form>
    </div>
  );
}

export default BloodRequest;
