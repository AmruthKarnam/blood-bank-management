// AdminModifications.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import backendApi from '../api';

function AdminModifications() {
    const navigate = useNavigate();

    const handleClick = (path) => {
        navigate(path);
    };
  return (
    <div>
      <h1>Admin Modifications</h1>
      <button onClick={() => handleClick('/manager/AdminModifications/AddAdmins')}>Add Admins</button>
      <button onClick={() => handleClick('/manager/AdminModifications/RemoveAdmins')}>Remove Admins</button>
      <button onClick={() => handleClick('/manager/AdminModifications/UpdateAdmins')}>UpdateAdmins </button>
      <button onClick={() => handleClick('/manager/AdminModifications/ListAdmins')}>List Admins </button>
    </div>
  );
}

export default AdminModifications;
