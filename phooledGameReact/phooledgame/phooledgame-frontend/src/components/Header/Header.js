import React from 'react';
import './Header.css';
import { useNavigate } from 'react-router-dom';
const Header = () => {
    const navigate = useNavigate();
    
    const handleClick = () => {
        // Navigate to /your-link
        navigate('/login');
      };
  return (
    <div>
      <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>
      <nav className="navbar navbar-expand-xl navbar-dark bg-lightOFF">
        <a href='/'>
		      <div className="logo-group">
			      <img src="/assets/images/logo_main.png" alt="Phishducation logo"></img>
		      </div>
	      </a>
        <div className="collapse navbar-collapse" id="navbarNav" style={{paddingTop: "55px"}}>
          <ul className="navbar-nav ml-auto" style={{margin: "0px"}}>
            <li className="nav-item">
              <a href = '/signup'><i className="fa fa-edit" style={{paddingRight: "5px"}}></i>Register</a>
            </li>
            <li className="nav-item">
              <button className="logBtn" onClick={handleClick} ><i className="fa fa-sign-in-alt" style={{paddingRight: "5px"}}></i>LOGIN</button>
            </li>
          </ul>
        </div>
      </nav>
 	  </div>
  );
};

export default Header;
