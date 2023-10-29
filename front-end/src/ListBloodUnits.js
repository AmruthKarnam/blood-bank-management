// BloodUnitList.js

import React, { useState, useEffect } from 'react';
import backendApi from './App'

function BloodUnitList() {
    const [bloodUnits, setBloodUnits] = useState([]);

    useEffect(() => {
        fetch(backendApi + '/get_available_blood_units')
            .then(response => response.json())
            .then(data => setBloodUnits(data.blood_units))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h2>Available Blood Units</h2>
            <ul>
                {bloodUnits.map(unit => (
                    <li key={unit.Blood_Unit_ID}>{`Blood Unit ID: ${unit.Blood_Unit_ID}, Status: ${unit.Status}`}</li>
                ))}
            </ul>
        </div>
    );
}

export default BloodUnitList;
