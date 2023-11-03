// UpdateAdmin.js
import React, { useState } from 'react';
import backendApi from '../api';

function UpdateAdmin() {
  const [username, setUsername] = useState('');
  const [newPassword, setNewPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send a request to your backend API to update the admin
    try {
      const response = await fetch(backendApi + '/update_admin', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, newPassword }),
      });

      if (response.ok) {
        alert('Admin updated successfully!');
        setUsername('');
        setNewPassword('');
      } else {
        alert('Error updating admin. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Update Admin</h1>
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
        <button type="submit">Update Admin</button>
      </form>
    </div>
  );
}

export default UpdateAdmin;
