import React from 'react';
import './Footer.css';

const Footer = () => {
  return(
    <div>
	  <footer className="footer">
		<div className="" style={{padding: "0px 65px"}}>
		  <div className="row" style={{flexDirection: "column", alignItems: "flex-start"}}>
			<div className="col-md-12 col-lg-12" style={{width: "100%"}}>
			  <div className="logo-group" style={{padding: "0px"}}>
			    <img src='/assets/images/logo-white.png'></img>
			  </div>
			  <p className="footer-text">Our goal is to make you better at finding phishing emails, and to make that process easy!</p>
			  <hr className="footer-hr" />
			</div>
            <div style={{width:"100%", display: "flex", justifyContent: "space-between"}}>
            <div className="col-md-2" style={{color: "white"}}>
			  <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/n" target="_blank"><img src='/assets/images/logo_cc.png' style={{marginTop: "5px"}} /></a>
			</div>
			<div className="col-md-8">
			  <p style={{marginBottom: "0px", color: "white", padding: "2px", lineHeight: "2", textAlign: "center"}}>Design and Production by: 
			  <a className="footer-link" href="https://tlss.uottawa.ca/site/en/home" target="_blank">University of Ottawa, TLSS</a>
			  <br />
			  <a className="footer-link" href="https://www.freepik.com/vectors/web" target="_blank">Web vector created by stories - www.freepik.com</a>
			  <br />
			  Copyright ©<span id="year" style={{color: "white"}}></span> All rights reserved</p>
			</div>
			<div className="col-md-2">
			  <a href="https://www.uottawa.ca/en" target="_blank"><img src="assets/images/logo_uottawa.png" style={{marginTop: "5px"}} /></a>
			</div>
            </div>
          </div>
		</div>
	  </footer>
	</div>
  );
};

export default Footer;