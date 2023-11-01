import React, { useState } from 'react';

function Login({ setUserType }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [adminInfo, setAdminInfo] = useState(null);


  const handleLogin = (e) => {
    e.preventDefault();

    if (username === "admin" && password === "adminPassword") {
        setUserType('admin');
        setAdminInfo({ adminName: username, adminPassword: password });
    }
    if (username === 'manager' && password === 'managerPassword') {
      setUserType('manager');
      setAdminInfo({ adminName: username, adminPassword: password });
    }
    if (username === 'analyst' && password === 'analystPassword') {
      setUserType('analyst');
      setAdminInfo({ adminName: username, adminPassword: password });
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
