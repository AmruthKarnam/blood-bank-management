// src/AdminDashboard.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function AdminDashboard() {
  const navigate = useNavigate();

  const handleClick = (path) => {
    navigate(path);
  };
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <button onClick={() => handleClick('/admin/donorRegistration')}>Donor Registration</button>
      <button onClick={() => handleClick('/admin/patientRegistration')}>Patient Registration</button>
    </div>
  );
}

export default AdminDashboard;
