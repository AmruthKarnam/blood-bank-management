// UpdateBloodUnitStatus.js

import React, { useState } from 'react';
import backendApi from '../api';

const UpdateBloodUnitStatus = () => {
  const [bloodUnitID, setBloodUnitID] = useState('');
  const [newStatus, setNewStatus] = useState('');

  const handleChange = (e) => {
    console.log('Selected value:', e.target.value);
    setNewStatus(e.target.value);
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("status=", newStatus);
    const requestData = {
      blood_unit_id: bloodUnitID,
      new_status: newStatus,
    };

    fetch(backendApi + '/update_blood_unit_status', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      alert(data.message);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>
          Blood Unit ID:
          <input
            type="number"
            value={bloodUnitID}
            onChange={(e) => setBloodUnitID(e.target.value)}
            required
          />
        </label>
      </div>
      <div>
        <label>
          New Status:
          <select
            value={newStatus}
            onChange={handleChange}
            required
          >
            <option value="InStock">In Stock</option>
            <option value="PendingAnalysis">Pending Analysis</option>
            <option value="Expired">Expired</option>
            <option value="Damaged">Damaged</option>
            <option value="Reserved">Reserved</option>
            <option value="Used">Used</option>
          </select>
        </label>
      </div>
      <button type="submit">Update Status</button>
    </form>
  );
};

export default UpdateBloodUnitStatus;
