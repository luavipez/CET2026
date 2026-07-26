import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Cambia esta URL por la de tu backend en Render cuando compiles para producción
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/users';

function App() {
  const [usuarios, setUsuarios] = useState([]);
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    cargarUsuarios();
  }, []);

  const cargarUsuarios = async () => {
    const res = await axios.get(API_URL);
    setUsuarios(res.data);
  };

  const guardarUsuario = async (e) => {
    e.preventDefault();
    if (!nombre || !email) return;
    await axios.post(API_URL, { nombre, email });
    setNombre('');
    setEmail('');
    cargarUsuarios();
  };

  const eliminarUsuario = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
    cargarUsuarios();
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Administración de Usuarios</h1>
      
      <form onSubmit={guardarUsuario} style={{ marginBottom: '20px' }}>
        <input type="text" placeholder="Nombre" value={nombre} onChange={e => setNombre(e.target.value)} />
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        <button type="submit">Agregar</button>
      </form>

      <ul>
        {usuarios.map(u => (
          <li key={u._id} style={{ margin: '10px 0' }}>
            {u.nombre} ({u.email}){' '}
            <button onClick={() => eliminarUsuario(u._id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
