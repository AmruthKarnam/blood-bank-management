// src/AnalystDashboard.js
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function AnalystDashboard({userInfo}) {
  console.log("here userInfo =", userInfo);
  const [localUserInfo, setLocalUserInfo] = useState(userInfo);
  useEffect(() => {
      setLocalUserInfo(userInfo);
    }, [userInfo]);
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
