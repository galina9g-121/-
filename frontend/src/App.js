// src/App.js
import React from 'react';
import AddUser from './components/AddUser';  // Импортируем компонент

function App() {
  return (
    <div>
      <h1>User Management</h1>
      <AddUser />  {/* Используем компонент AddUser */}
    </div>
  );
}

export default App;