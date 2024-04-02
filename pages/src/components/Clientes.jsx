import NavbarComp from '../App'
import React, { useState } from 'react';
import axios from 'axios';


export function Clientes(){

    const [formData, setFormData] = useState({
       Cedula:"",
       Nombre:"",
       Direccion:"",
       Telefono:"",
      });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
          const response = await axios.post('http://localhost:3000/servidor', formData);
          console.log(response.data);
          // Manejar la respuesta del servidor, si es necesario
        } catch (error) {
          console.error('Error al enviar datos:', error);
        }
    }

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
      };
    

return(
    <div class="container h-100">
        <NavbarComp></NavbarComp>
        <div class="row h-100 justify-content-center align-items-center">
            <div class="col-md-5">
                <div class="card card-body">
                <form method="post" onSubmit={handleSubmit}>
                    <div class="mb-3">
                        <label for="Cedula" class="form-label">Cedula</label>
                        <input type="text" name="Cedula" id="Cedula" class="form-control" value={formData.Cedula}onChange={handleChange} placeholder="Cedula"></input>
                    </div>
                    <div class="mb-3">
                        <label for="Nombre" class="form-label">Nombre</label>
                        <input type="text" name="Nombre" id="Nombre" class="form-control" value={formData.Nombre} onChange={handleChange} placeholder="Nombre"></input>
                    </div>
                    <div class="mb-3">
                        <label for="Direccion" class="form-label">Direccion</label>
                        <input type="text" name="Direccion" id="Direccion" class="form-control"value={formData.Direccion}onChange={handleChange} placeholder="Direccion"></input>
                    </div>
                    <div class="mb-3">
                        <label for="Telefono" class="form-label">Telefono</label>
                        <input type="text" name="Telefono" id="Telefono" class="form-control"value={formData.Telefono}onChange={handleChange} placeholder="Telefono"></input>
                    </div>
                    <button type="submit" class="btn btn-primary">AGREGAR</button>
                </form>
                </div>
            </div>
        </div>
    </div>
)
}