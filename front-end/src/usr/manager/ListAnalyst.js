// ListAnalyst.js
import React, { useState, useEffect } from 'react';
import backendApi from '../../App'

function ListAnalyst() {
  const [analyst, setAnalyst] = useState([]);

  useEffect(() => {
    // Fetch the list of analyst from your backend API
    const fetchAnalyst = async () => {
      try {
        const response = await fetch(backendApi + '/list_analyst');
        if (response.ok) {
          const data = await response.json();
          setAnalyst(data.analyst);
        } else {
          console.error('Error fetching analyst.');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchAnalyst();
  }, []);

  return (
    <div>
      <h1>List Analyst</h1>
      <ul>
        {analyst.map((admin) => (
          <li key={admin.id}>{admin.username}</li>
        ))}
      </ul>
    </div>
  );
}

export default ListAnalyst;
