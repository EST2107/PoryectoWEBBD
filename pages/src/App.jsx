import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

export function NavbarComp() {
    return (
      <>
        <Navbar bg="light" expand="lg" className="justify-content-center">
          <Container>
            <Navbar.Brand href="http://localhost:3000/">Delicias Dilcia</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Nav className="me-auto">
              <Nav.Link href=''>Clientes</Nav.Link>
              <Nav.Link href=''>platillos</Nav.Link>
              <Nav.Link href=''>Productos</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
      </>
    );
  
}

export default NavbarComp
