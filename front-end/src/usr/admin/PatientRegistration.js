import React, { useState } from 'react';
import backendApi from '../../App'

function PatientRegistration({adminInfo}) {
  const [formData, setFormData] = useState({
    name: '',
    blood_group: '',
    gender: '',
    contact: '',
    date: '',
    adminName: adminInfo?.adminName || '',
    adminPassword: adminInfo?.adminPassword || '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch(backendApi + '/patient_registration', {
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
    <div>
      <h2>Patient Registration</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input type="text" name="name" value={formData.name} onChange={handleChange} required />
        </div>
        <div>
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
        <div>
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
        <div>
          <label>Contact:</label>
          <input type="tel" name="contact" value={formData.contact} onChange={handleChange} pattern="[0-9]{10}" title="Please enter a 10-digit phone number" required />
        </div>
        <div>
          <label>Date:</label>
          <input type="date" name="date" value={formData.date} onChange={handleChange} required />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default PatientRegistration;
