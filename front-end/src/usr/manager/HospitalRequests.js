// HospitalRequest.js

import React, { useState } from 'react';
import backendApi from '../api';

const HospitalRequest = () => {
  const [hospitalID, setHospitalID] = useState('');
  const [bloodGroup, setBloodGroup] = useState('');
  const [quantity, setQuantity] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
  
    const requestData = {
      hospital_id: hospitalID,
      blood_group: bloodGroup,
      quantity: quantity,
    };
  
    fetch(backendApi + '/hospital_request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Set the content type to JSON
      },
      body: JSON.stringify(requestData), // Stringify the data to JSON
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      alert(data.message);
      // You can add code here to handle a successful response
    })
    .catch(error => {
      console.error('Error:', error);
      // You can add code here to handle errors
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>
          Hospital ID:
          <input
            type="number"
            value={hospitalID}
            onChange={(e) => setHospitalID(e.target.value)}
            required
          />
        </label>
      </div>
      <div>
        <label>
          Blood Group:
          <select
            value={bloodGroup}
            onChange={(e) => setBloodGroup(e.target.value)}
            required
          >
            <option value="">Select Blood Group</option>
            <option value="O+">O+</option>
            <option value="O-">O-</option>
            <option value="A+">A+</option>
            <option value="A-">A-</option>
            <option value="B+">B+</option>
            <option value="B-">B-</option>
            <option value="AB+">AB+</option>
            <option value="AB-">AB-</option>
          </select>
        </label>
      </div>
      <div>
        <label>
          Quantity:
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            required
          />
        </label>
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default HospitalRequest;
