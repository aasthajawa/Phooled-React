// src/components/Login.js
import { useNavigate } from 'react-router-dom';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';
import '../../css/cirrus-core.min.css';
import '../../css/cirrus.min.css';
import '../../css/layout.css';
import '../../css/phishducation.css';
import './Login.css';


const Login = ({history}) => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
  
    const handleLogin = async () => {
      console.log(username, password);
        try {
            const response = await fetch('http://localhost:8000/api/login', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ username, password }),
            });
            console.log("response",response)
            if (response.ok) {
              const data = await response.json();
              
              // Signup successful, you might want to redirect to login or do other actions
              console.log('Login successful');
              console.log("data",data.user);
              navigate('/game/dashboard');
            } else {
              // Signup failed, check the response for specific error message
              const data = await response.json();
              //console.log("i am data", data)
              //console.log("i am data", data.detail)
              setError(data.detail); // Assuming the server sends a message field in the response
              if (data.detail === 'Invalid credentials') {
                // User already exists, navigate to the login page
                navigate('/signup');
              }
            }
          } catch (error) {
            console.error('Error during signup:', error);
          }
    };

    return (
        <div>
          <Header />
          <div id="main" className="contentOFF" role="main">
            <div className="container">
	            <div className="row">
		            <div className="col-sm-12 col-lg-4 my-auto" data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-easing="ease-in-sine">
    		          <div className="main-login-content">
        	          <h4 className="login-header"><i className="fas fa-sign-in-alt" style={{paddingRight: "5px"}}></i>Login </h4>
                    <div>
                      <label>Email Address:</label>
                      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                    </div>
                    <div>
                      <label>Password:</label>
                      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} /> 
                    </div>
                    <br />
                    <div className="button-container">
                      <button onClick = {handleLogin} className= "create-account-buttonOFF loginBtn" type="button">Sign In</button>
			                <button  onClick={() => navigate('/signup')} className="create-account-buttonOFF loginBtn" type="button">Create Account</button>
                    </div>
		              </div>
	              </div>
	

	              <div className="col-sm-12 col-lg-8 my-auto">
		              <img src= 'assets/images/login.png' alt="login" style={{maxHeight: "700px", padding: "50px"}} />
	              </div>
              </div>
            </div>  
         </div>
         <Footer />
        </div>
    );
};

export default Login;
