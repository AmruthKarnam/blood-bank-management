// ListDonorsToAnalyse.js

import React, { useState, useEffect } from 'react';
import backendApi from '../../App'

function ListDonorsToAnalyse() {
    const [donorsToAnalyse, setDonorsToAnalyse] = useState([]);

    useEffect(() => {
        fetch(backendApi + '/donors_to_analyse')
            .then(response => response.json())
            .then(data => setDonorsToAnalyse(data.blood_units))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h2>Donors To be Analysed</h2>
            <ul>
                {donorsToAnalyse.map(unit => (
                    <li key={unit.Donor_ID}>{`DONOR ID: ${unit.Donor_ID}`}</li>
                ))}
            </ul>
        </div>
    );
}

export default ListDonorsToAnalyse;
