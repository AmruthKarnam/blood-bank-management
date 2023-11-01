import React, { useState } from 'react';

const UpdateBloodUnitStatus = () => {
  const [bloodUnitID, setBloodUnitID] = useState('');
  const [newStatus, setNewStatus] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add code to send data to the backend
    fetch('/update_blood_unit_status', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `blood_unit_id=${bloodUnitID}&new_status=${newStatus}`,
    })
    .then(response => response.json())
    .then(data => {
    console.log('Success:', data);
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
        onChange={(e) => setNewStatus(e.target.value)}
        required
        >
        <option value="InStock">In Stock</option>
        <option value="PendingAnalysis">Pending Analysis</option>
        <option value="Expired">Expired</option>
        <option value="Damaged">Damaged</option>
        </select>
      </label>
      </div>
      <button type="submit">Update Status</button>
    </form>
  );
};

export default UpdateBloodUnitStatus;
