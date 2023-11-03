// RemoveAnalyst.js
import React, { useState } from 'react';
import backendApi from '../api';

function RemoveAnalyst() {
  const [username, setUsername] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send a request to your backend API to remove the analyst
    try {
      const response = await fetch(backendApi + '/remove_analyst', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
      });

      if (response.ok) {
        alert('Analyst removed successfully!');
        setUsername('');
      } else {
        alert('Error removing analyst. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Remove Analyst</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>ID:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <button type="submit">Remove Analyst</button>
      </form>
    </div>
  );
}

export default RemoveAnalyst;
