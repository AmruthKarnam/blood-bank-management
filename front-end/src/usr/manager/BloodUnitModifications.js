// BloodUnitModifications.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import backendApi from '../api';

function BloodUnitModifications() {
  const navigate = useNavigate();

    const handleClick = (path) => {
        navigate(path);
    };
  return (
    <div>
      <h1>Blood Modifications</h1>
      <button onClick={() => handleClick('/manager/BloodUnitModifications/ListBloodUnits')}>List Blood Units</button>
      <button onClick={() => handleClick('/manager/BloodUnitModifications/UpdateBloodUnitStatus')}>Update Blood Units</button>
      <button onClick={() => handleClick('/manager/BloodUnitModifications/AddBloodUnits')}>Add Blood Units </button>
    </div>
  );
}

export default BloodUnitModifications;
