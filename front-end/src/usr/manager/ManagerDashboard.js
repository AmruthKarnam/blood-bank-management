// src/ManagerDashboard.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import backendApi from '../api';

function ManagerDashboard() {
  const navigate = useNavigate();

  const handleClick = (path) => {
    navigate(path);
  };
  return (
    <div>
    <h1>Manager Dashboard</h1>
    <button onClick={() => handleClick('/manager/BloodUnitModifications')}>Changes to Blood Units</button>
    <button onClick={() => handleClick('/manager/BloodRequests')}>Blood Requests</button>
    <button onClick={() => handleClick('/manager/AdminModifications')}>Changes to Admins</button>
    <button onClick={() => handleClick('/manager/AnalystModifications')}>Changes to Analyst</button>
    <button onClick={() => handleClick('/manager/HospitalRequests')}>Hospital Requests</button>
  </div>
);
}

export default ManagerDashboard;
