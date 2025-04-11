// src/components/AddUser.js
import React, { useState } from 'react';

function AddUser() {
  // Состояния для данных формы
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [fio, setFio] = useState('');
  const [phone, setPhone] = useState('');
  const [message, setMessage] = useState('');

  // Функция для обработки отправки формы
  const handleSubmit = (event) => {
    event.preventDefault(); // Предотвращаем стандартное поведение формы

    // Создаем объект данных пользователя для отправки
    const userData = {
      username,
      password,
      fio,
      phone,
    };

    // Отправляем POST запрос к серверу с данными
    fetch('http://127.0.0.1:5000/api/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
      .then((response) => response.json()) // Парсим JSON ответ
      .then((data) => {
        setMessage(data.message); // Устанавливаем сообщение от сервера
      })
      .catch((error) => {
        setMessage('Error connecting to the server');
      });
  };

  return (
    <div>
      <h2>Create New User</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div>
          <label>FIO:</label>
          <input
            type="text"
            value={fio}
            onChange={(e) => setFio(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Phone:</label>
          <input
            type="text"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            required
          />
        </div>
        <button type="submit">Create User</button>
      </form>

      {message && <div>{message}</div>} {/* Выводим сообщение о результате */}
    </div>
  );
}

export default AddUser;