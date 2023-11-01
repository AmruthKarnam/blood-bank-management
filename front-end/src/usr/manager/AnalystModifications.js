// AnalystModifications.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function AdminModifications() {
    const navigate = useNavigate();

    const handleClick = (path) => {
        navigate(path);
    };
  return (
    <div>
      <h1>Admin Modifications</h1>
      <button onClick={() => handleClick('/manager/AnalystModifications/AddAnalyst')}>Add Analyst</button>
      <button onClick={() => handleClick('/manager/AnalystModifications/RemoveAnalyst')}>Remove Analyst</button>
      <button onClick={() => handleClick('/manager/AnalystModifications/UpdateAnalyst')}>UpdateAnalyst </button>
      <button onClick={() => handleClick('/manager/AnalystModifications/ListAnalyst')}>List Analyst </button>
    </div>
  );
}

export default AdminModifications;
