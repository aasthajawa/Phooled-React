import React, { useEffect, useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';
import './Dashboard.css';
import '../../css/cirrus-core.min.css';
import '../../css/cirrus.min.css';
import '../../css/layout.css';
import '../../css/phishducation.css';

const Dashboard = () => {
    const navigate = useNavigate();
    const [userData, setUserData] = useState('');
    useEffect(() => {
      const fetchUserData = async () => {
          try {
              const response = await fetch('http://localhost:8000/api/game/dashboard', {
                  method: 'GET',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  credentials: 'include'
              });
              if (response.ok) {
                  const data = await response.json();
                  setUserData(data.user);
                  console.log("user_dashboard data", data);
              } else {
                  console.error('Failed to fetch user data');
              }
          } catch (error) {
              console.error('Error fetching user data:', error);
          }
      };

      fetchUserData();
  },[]);

    const handle = async () => {
        navigate('/game/phish-game');
    };

    return (
      <div>
        <Header />
        <div id="content" className="content">
          <div className="containerOFF" style={{backgroundColor: "#FAFBFD"}}>
            <div className="row">
              <div className="dashboard-side-panelOFF col-md-4 col-lg-4" data-aos="fade-right" data-aos-duration="1000" data-aos-once="true">
                <h2 style={{color: "#385B64"}}>{userData.curUserName}</h2>
                <h4> Level: 1</h4>
                <hr />
                <h6>Start a session:</h6>
                <button type="button" className="dashBtnB" onClick = {handle} style={{marginBottom: "1rem", width: "180px"}} data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-delay="320">Play Phooled</button>
                <button type="button" className="dashBtnB" style={{marginBottom: "1rem", width: "180px"}} data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-delay="320">Play BetaPhish</button>
                <button type="button" className="dashBtnB"style={{marginBottom: "1rem", width: "180px"}} data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-delay="320"><i className="fas fa-pencil-alt" style={{paddingRight: "5px"}}></i>Start a Quiz</button>

                <h6>Learn:</h6>
                <button type="button" className="dashBtnB" data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-delay="320" style={{marginBottom: "1rem", width: "150px"}}><i className="fas fa-video" style={{paddingRight: "5px"}}></i>View Courses</button>

                <h6>Give Feedback:</h6>
                <button type="button" className="dashBtnB" data-aos="fade-right" data-aos-duration="1000" data-aos-once="true" data-aos-delay="320" style={{marginBottom: "1rem", width: "150px"}} ><i className="fas fa-comment-alt" style={{paddingRight: "5px"}}></i>Feedback</button>
              </div>
              <div className="col-md-8 col-lg-8 my-auto">
                <img src="/assets/images/dashboard.png" alt="dashboard" style={{maxHeight: "700px"}} />
              </div>
            </div>
          </div>
          <div className="dashboard-summary-containerOFF col-md-12" data-aos="fade-up" data-aos-duration="1000" data-aos-once="true" data-aos-delay="300">
            <hr />
            <div style={{display:"flex", flexDirection: "row", alignItems: "center"}}>
              <h4 style={{marginRight: "0.5rem"}}>Current Level: </h4> <h4> Beginner 1 </h4>
            </div>
            <div className="progress">
              <div className="progress-bar" role="progressbar" style={{ backgroundColor: "#FF4F5A"}}></div>
            </div>
            <h6>XP Needed: 50 </h6>
            <div className="row">
              <div className="col-md-6 my-auto">
                <img src="/assets/images/progress.png" alt="dashboard" style={{maxHeight: "700px"}} />
              </div>
              <div className="col-md-6 my-auto">
                <div>
                  <h4 style={{marginRight: "0.5rem"}}>Your Performance: Review the videos </h4>
                </div>
                <div className="flex-containerOFF" data-aos="fade-left" data-aos-duration="1000" data-aos-once="true" data-aos-delay="320">
                  <div className="performance">
                    <h3>  Quizzes Completed: <span className ='performance-numberOFF'>0 </span> </h3>
                  </div>
                  <div className = "performance">
                    <h3>Correct Answers: <span className ='performance-numberOFF'>0</span></h3>
                  </div>
                  <div className="performance">
                    <h3>Avg Quiz Mark: <span className ='performance-numberOFF'>0%</span> </h3>
                  </div>
                  <div className ="performance">
                    <h3>Avg Question Time: <span className ='performance-numberOFF'>  sec</span> </h3>
                  </div>
                  <div className="performance">
                    <h3>Avg Quiz Time: <span className='performance-numberOFF'>0 sec</span> </h3>
                  </div>
                </div>
              </div>
            </div>
          </div>    
        </div>
        <Footer />
      </div>
    );
};

export default Dashboard;