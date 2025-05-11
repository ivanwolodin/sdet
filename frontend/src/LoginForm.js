import React, { useState } from 'react';

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/api/v1/login";

function LoginForm() {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const [messageColor, setMessageColor] = useState('');

  const handleLogin = async (event) => {
    event.preventDefault();
  
    try {
      const res = await fetch(`${API_URL}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ login, password }),
      });
  
      if (res.status === 401) {
        setMessage('Ошибка при входе');
        setMessageColor('red');
        return;
      }
  
      const data = await res.json();
      setMessage(data.message || 'Успешный вход');
      setMessageColor('green');
    } catch (err) {
      setMessage('Ошибка при входе');
      setMessageColor('red');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <div>
        <label>Username:</label><br />
        <input value={login} onChange={(e) => setLogin(e.target.value)} required />
      </div>
      <div>
        <label>Password:</label><br />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </div>
      <button type="submit">Login</button>
      {message && <p style={{ color: messageColor }}>{message}</p>}
    </form>
  );
}

export default LoginForm;
