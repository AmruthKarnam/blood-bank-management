import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
function Login({ setUserInfo }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    try {
      if (username === "admin" && password === "adminPassword") {
        setUserInfo({ userName: username, userPassword: password, userType:"admin" });
      }
      if (username === 'manager' && password === 'managerPassword') {
        setUserInfo({ userName: username, userPassword: password, userType:"manager" });
      }
      if (username === 'analyst' && password === 'analystPassword') {
        setUserInfo({ userName: username, userPassword: password, userType:"analyst" });
      }
    } catch (error) {
      console.error(error);
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
