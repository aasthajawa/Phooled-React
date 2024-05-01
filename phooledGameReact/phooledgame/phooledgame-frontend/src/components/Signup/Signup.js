// src/components/Signup.js
import { useNavigate } from 'react-router-dom';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';
import React, { useState } from 'react';
import axios from 'axios';
import '../../css/cirrus-core.min.css';
import '../../css/cirrus.min.css';
import '../../css/layout.css';
import '../../css/phishducation.css';
import './Signup.css';


const Signup = ({ history }) => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [error, setError] = useState('');

    const handleSignup = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/signup', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ username, password, email }),
            });
            console.log(response)
            if (response.ok) {
              // Signup successful, you might want to redirect to login or do other actions
              console.log('Signup successful');
              navigate('/login');
            } else {
              // Signup failed, check the response for specific error message
              const data = await response.json();
              console.log("i am data", data)
              console.log("i am data", data.detail)
              setError(data.detail); // Assuming the server sends a message field in the response
              if (data.detail === 'Username already exists') {
                // User already exists, navigate to the login page
                navigate('/login');
              }
            }
          } catch (error) {
            console.error('Error during signup:', error);
          }
    };

    return (
        <div>
          <Header />
          <div className="container">
	          <div className="row">
		          <div className="col-sm-12 col-lg-4 my-auto" data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-easing="ease-in-sine">
			          <div className="main-login-content">
				          <h4> Register </h4>
				          <div>
                    <label>Username:</label>
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                    <span>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>
                  </div>
                  <div>
                    <label>Email address:</label>
                    <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
                  </div>
					        <div>
                    <label>Password:</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    <span>
                      <ul className="signup-ul">
                        <li>Your password can’t be too similar to your other personal information.</li>
                        <li>Your password must contain at least 8 characters.</li>
                        <li>Your password can’t be a commonly used password.</li>
                        <li>Your password can’t be entirely numeric.</li>
                      </ul>
                    </span>
                  </div>
                  <div>
                    <label>Password Confirmation:</label>
                    <input type="password" />
                    <span>Enter the same password as before, for verification.</span>
                  </div>
                  <div>
                    <input type="checkbox" id="terms_and_conditions" value="1" />
                    <label htmlFor="terms_and_conditions"  style={{display: "inline"}}>I agree to the Phishducation</label><a id="myBtn" style={{display: "inline", color: "#5793CF", display: "inline"}}>Terms and Conditions.</a>
                  </div>
						
					        <center><button onClick = {handleSignup} className= "create-account-buttonOFF loginBtn" type="button">Register</button></center>
			          </div>
	            </div>
	

	            <div className="col-sm-12 col-lg-8">
		            <img src= 'assets/images/login.png' alt="hero" style={{maxHeight: "700px", padding: "50px"}} />
	            </div>
            </div>
          </div>
          <Footer />
        </div>
   );
};

export default Signup;
