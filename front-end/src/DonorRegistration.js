import React, { useState } from 'react';

function DonorRegistration() {
  const [formData, setFormData] = useState({
    name: '',
    gender: '',
    age: '',
    bloodGroup: '',
    contactNumber: '',
    donationDate: '',
    lastDonated: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
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
          <label htmlFor="gender">Gender:</label>
          <input
            type="text"
            id="gender"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="age">Age:</label>
          <input
            type="text"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="bloodGroup">Blood Group:</label>
          <input
            type="text"
            id="bloodGroup"
            name="bloodGroup"
            value={formData.bloodGroup}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="contactNumber">Contact Number:</label>
          <input
            type="text"
            id="contactNumber"
            name="contactNumber"
            value={formData.contactNumber}
            onChange={handleChange}
          />
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
