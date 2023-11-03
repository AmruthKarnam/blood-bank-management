import React, { useEffect, useState } from 'react';
import backendApi from '../api';

function ListDonorsToAnalyse({ userInfo }) {
    const [donors, setDonors] = useState([]);

    useEffect(() => {
        const requestOptions = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        };

        const url = `${backendApi}/donors_to_analyse?analystName=${userInfo.userName}&analystPassword=${userInfo.userPassword}`;

        fetch(url, requestOptions)
            .then(response => response.json())
            .then(data => setDonors(data.donors))  // Store the donors in state
            .catch(error => console.error('Error:', error));
    }, [userInfo]);

    return (
        <div>
            <h2>Donors to Analyse</h2>
            <ul>
                {donors.map(donor => (
                    <li key={donor.Donor_ID}>
                        Donor ID: {donor.Donor_ID}, Blood Unit ID: {donor.Blood_Unit_ID}, Status: {donor.Status}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ListDonorsToAnalyse;
