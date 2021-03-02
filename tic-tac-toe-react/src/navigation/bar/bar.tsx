import React, { useState } from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Button from 'react-bootstrap/Button'
import Toast from 'react-bootstrap/Toast'

interface Navigation {
  navigation: (path: string) => void;
}

export const NavBar: React.FC<Navigation> = props => {
  const [showToast, setShowToast] = useState(false);
  return (
    <div>
      <Navbar bg="dark" expand="lg">
        <Navbar.Brand onClick={() => { props.navigation('/home') }}>React-Bootstrap</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link onClick={() => { props.navigation('/game') }}>Game</Nav.Link>
            <Nav.Link onClick={() => { props.navigation('/ranking') }}>Chuck Norris</Nav.Link>
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
            </NavDropdown>
          </Nav>
          <Form inline>
            <FormControl type="text" placeholder="Search" className="mr-sm-2" onClick={() => { setShowToast(true) }} />
            <Button variant="outline-success">Search</Button>
          </Form>
        </Navbar.Collapse>
      </Navbar>
      <Toast show={showToast} onClose={() => { setShowToast(false) }} style={{ width: '30%', position: 'absolute', right: 30 }}>
        <Toast.Header>
          <img src={window.location.origin + "/favicon.ico"} className="rounded mr-2" alt="" width='50' height='50' />
          <strong className="mr-auto">Search</strong>
        </Toast.Header>
        <Toast.Body>Search results...</Toast.Body>
      </Toast>
    </div >
  );
}