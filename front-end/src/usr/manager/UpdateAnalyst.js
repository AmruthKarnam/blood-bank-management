// UpdateAnalyst.js
import React, { useState } from 'react';
import backendApi from '../../App'

function UpdateAnalyst() {
  const [username, setUsername] = useState('');
  const [newPassword, setNewPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send a request to your backend API to update the analyst
    try {
      const response = await fetch(backendApi + '/update_analyst', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, newPassword }),
      });

      if (response.ok) {
        alert('Analyst updated successfully!');
        setUsername('');
        setNewPassword('');
      } else {
        alert('Error updating analyst. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Update Analyst</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>New Password:</label>
          <input
            type="password"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Update Analyst</button>
      </form>
    </div>
  );
}

export default UpdateAnalyst;
