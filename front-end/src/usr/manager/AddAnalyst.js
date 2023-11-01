// AddAnalysts.js
import React, { useState } from 'react';
import backendApi from '../../App'

function AddAnalysts() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send a request to your backend API to update the analyst table
    try {
      const response = await fetch(backendApi + '/add_analyst', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        alert('Analyst added successfully!');
        setUsername('');
        setPassword('');
      } else {
        alert('Error adding analyst. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Add Analysts</h1>
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
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add Analyst</button>
      </form>
    </div>
  );
}

export default AddAnalysts;
