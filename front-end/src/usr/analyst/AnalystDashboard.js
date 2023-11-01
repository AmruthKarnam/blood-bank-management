// src/AnalystDashboard.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function AnalystDashboard() {
    const navigate = useNavigate();

    const handleClick = (path) => {
      navigate(path);
    };
  return (
    <div>
      <h1>Analyst Dashboard</h1>
      <button onClick={() => handleClick('/analyst/AddDonorAnalysis')}>Add Donor's Analysis</button>
      <button onClick={() => handleClick('/analyst/ListDonorAnalysis')}>List Donor's Analysis</button>
      <button onClick={() => handleClick('/analyst/ListDonorsToAnalyse')}>List Donor To Analyse</button>
    </div>
  );
}

export default AnalystDashboard;
