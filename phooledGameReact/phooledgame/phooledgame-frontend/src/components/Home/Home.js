import './Home.css';
import React from 'react';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';

const Home = () => {
  return (
    <div className="">
    <Header />
    <div id="main" className="contentOFF" role="main">
      <div className="container" style={{backgroundColor: "#FAFBFD", padding: "50px 100px 20px 100px"}}>
        <div className="row">
          <div className="col-sm-12 col-lg-5 my-auto" data-aos="fade-right" data-aos-duration="1000" data-aos-once="true">
            <h2 style={{color: "#374054", fontSize: "2.5rem", fontFamily: "Montserrat,sans-serif", fontWeight: "700", lineHeight: "1.2", margin: "0 0 0.5rem 0"}}>Welcome to <br /><span style={{fontSize: "40px", textTransform: "uppercase", color: "#7C66AC"}}>Phishducation!</span></h2>
            <p style={{margin: "1rem 0", color: "#546172", fontSize: "24px", lineHeight: "110%"}}>Welcome to the Phishducation application! Our goal is to make you better at finding phishing emails, and to make that process easy!</p>
            <div>
            <p style={{display: "inline", margin: "1rem 0", color: "#546172", fontSize: "26px", lineHeight: "110%"}}>Start by <a style={{textDecoration: "none"}} href="/login">logging in</a> or <a style={{textDecoration: "none"}} href="/signup">registering!</a></p>
            </div>
            
          </div>
          <div className="col-sm-12 col-lg-7">
            <img src= '/assets/images/hero.png' alt="hero" style={{maxHeight: "700px"}} />
          </div>
        </div>
      </div>

      <br />

      <div className="" ></div>
        <center>
          <hr style={{width: "80%"}}></hr>
          <br />
          <br />
        <div className="col-sm-12 text-center" data-aos="fade-up" data-aos-duration="1000" data-aos-once="true" style={{width: "70%", padding:"0 15px"}}>
          <h4 className="heading">What is Phishing?</h4>
          <p className="phishing-def">A phishing attack aims to compromise data, resulting in losses and damage to both companies and individuals. The project aims to make users aware of the ten most common phishing attributes and provide a fun way to test and improve their phishing email classNameification abilities.</p>
        </div> 
        <div className="col-sm-12 boat" data-aos="fade-in" data-aos-duration="3000" data-aos-once="true">
            <img src= '/assets/images/boat.png' alt="boat" style={{maxHeight: "700px"}} />
        </div>
   </center>
      </div>
      <Footer />
  </div>
  );
};

export default Home;
