// RemoveAdmin.js
import React, { useState } from 'react';
import backendApi from '../../App'

function RemoveAdmin() {
  const [username, setUsername] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send a request to your backend API to remove the admin
    try {
      const response = await fetch(backendApi + '/remove_admin', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
      });

      if (response.ok) {
        alert('Admin removed successfully!');
        setUsername('');
      } else {
        alert('Error removing admin. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Remove Admin</h1>
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
        <button type="submit">Remove Admin</button>
      </form>
    </div>
  );
}

export default RemoveAdmin;
