import React, { useState } from 'react';
import backendApi from '../api';

function DonorRegistration({userInfo}) {
  const [formData, setFormData] = useState({
    name: '',
    gender: '',
    age: '',
    bloodGroup: '',
    contactNumber: '',
    donationDate: '',
    lastDonated: '',
    adminName: 'admin',
    adminPassword: 'adminPassword',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here

    fetch(backendApi + '/donor_registration', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      // You can add code here to handle a successful registration
    })
    .catch((error) => {
      console.error('Error:', error);
      // You can add code here to handle errors
    });
  };

  return (
    <div className="donor-registration">
      <h2>Donor Registration</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
        <label htmlFor="gender">Gender</label>
        <select
          name="gender"
          value={formData.gender}
          onChange={handleChange}
          >
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
        </select>
        </div>
        <div className="form-group">
          <label htmlFor="age">Age:</label>
          <input
            type="number"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
        <label htmlFor="blood_group">Blood Group</label>
        <select
          name="blood_group"
          value={formData.blood_group}
          onChange={handleChange}
          >
            <option value="">Select Blood Group</option>
            <option value="O+">O+</option>
            <option value="O-">O-</option>
            <option value="A+">A+</option>
            <option value="A-">A-</option>
            <option value="B+">B+</option>
            <option value="B-">B-</option>
            <option value="AB+">AB+</option>
            <option value="AB-">AB-</option>
        </select>
        </div>
        <div className="form-group">
          <label htmlFor="contactNumber">Contact Number:</label>
          <input type="tel" name="contactNumber" value={formData.contact} onChange={handleChange} pattern="[0-9]{10}" title="Please enter a 10-digit phone number" required />
        </div>
        <div className="form-group">
          <label htmlFor="donationDate">Donation Date:</label>
          <input
            type="date"
            id="donationDate"
            name="donationDate"
            value={formData.donationDate}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="lastDonated">Last Donated:</label>
          <input
            type="date"
            id="lastDonated"
            name="lastDonated"
            value={formData.lastDonated}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default DonorRegistration;
