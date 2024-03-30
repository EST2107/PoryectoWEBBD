import React from 'react'
import ReactDOM from 'react-dom/client'
import NavbarComp from './App.jsx'
import { Clientes } from './components/Clientes.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Clientes></Clientes>
  </React.StrictMode>,
)
