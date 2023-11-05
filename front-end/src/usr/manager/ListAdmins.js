// ListAdmins.js
import React, { useState, useEffect } from 'react';
import backendApi from '../api';

function ListAdmins() {
  const [admins, setAdmins] = useState([]);

  useEffect(() => {
    // Fetch the list of admins from your backend API
    const fetchAdmins = async () => {
      try {
        const response = await fetch(backendApi + '/list_admins');
        if (response.ok) {
          const data = await response.json();
          setAdmins(data.admins);
        } else {
          console.error('Error fetching admins.');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchAdmins();
  }, []);

  return (
    <div>
      <h1>List Admins</h1>
      <ul>
        {admins.map((admin) => (
          <li key={admin.ADMIN_ID}>{admin.ADMIN_NAME}</li>
        ))}
      </ul>
    </div>
  );
}

export default ListAdmins;
