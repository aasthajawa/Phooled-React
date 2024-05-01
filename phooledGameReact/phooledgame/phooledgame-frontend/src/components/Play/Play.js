import React from 'react';
import './Play.css';
import { useNavigate, useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ActualGame from '../ActualGame/ActualGame';

const Play = () => {
  const navigate = useNavigate();
  
  const [currentUrl, setCurrentUrl] = useState('');
  const [showRules, setShowRules] = useState(false);
  const [numCards, setNumCards] = useState(0);
  useEffect(() => {
    // Update the currentUrl state with the current window URL
    setCurrentUrl(window.location.href);
  }, []);
  // Function to handle slider value change
  // Function to handle slider value change
  const handleSliderChange = (event, setStateFunction) => {
    setStateFunction(Number(event.target.value));
  };
  const handleCopy = () => {
    navigator.clipboard.writeText(currentUrl);
  };
  
  const handleStartGame = () => {
    setShowRules(true);
  }; 
  const handleSave = () => {
    navigate('/game/phish-game/room/:roomId/quickfire',{ state: { numCards: 4 } })
    
  };
      return (
        <div>
          <div className="header">
            <img className="header-img" src="/assets/images/logo-white.png" alt = "Phooled header logo"></img>
          </div>
          {showRules ? (
            <div>
              <div className="container-rules">
              <div className="stat">
                <img  className="heart" src='assets/images/heart.png'></img>
              </div>
            </div>
            <div className="hero-content text-center">
              <div className="max-w-md">
                <h1 className="text-5xl font-bold">Game Settings</h1>
                <div className="card">
                  <div className="card-body">
                    <h2 className="card-title">Select Avatar</h2>
                    <div className="avatar-picker"></div>
                  </div>
                </div>
                <div className="container-flex" x-show="isOwner === 1">
                  <p className="py-6">Cards Per Hand</p>
                  <input
                      x-model="num_cards"
                      type="range"
                      min="0"
                      max="5"
                      className="range"
                      value={numCards}
                      onChange={(event) => handleSliderChange(event, setNumCards)}
                      step="1" />
                  <div className="w-full flex justify-between text-xs px-2">
                      <span>2 cards</span>
                      <span>3 cards</span>
                      <span>5 cards</span>
                  </div>
                  <p className="py-6">Quick Fire Time</p>
                  <input
                      x-model="limit_qf"
                      type="range"
                      min="0"
                      max="2"
                      className="range"
                      step="1" />
                  <div className="w-full flex justify-between text-xs px-2">
                      <span>30 sec</span>
                      <span>60 sec</span>
                      <span>120 sec</span>
                  </div>
                  <p className="py-6">Arsenal Time</p>
                  <input
                      x-model="limit_ar"
                      type="range"
                      min="0"
                      max="2"
                      className="range"
                      step="1" />
                  <div className="w-full flex justify-between text-xs px-2">
                      <span>30 sec</span>
                      <span>60 sec</span>
                      <span>120 sec</span>
                  </div>
                  <p className="py-6">The Fight Time</p>
                  <input
                      x-model="limit_fr"
                      type="range"
                      min="0"
                      max="2"
                      className="range"
                      step="1" />
                  <div className="w-full flex justify-between text-xs px-2">
                      <span>30 sec</span>
                     
                      <span>60 sec</span>
                      
                      <span>120 sec</span>
                  </div>
                  <button className="btn btn-primary my-4" onClick={handleSave}>
                      Save
                  </button>
                </div>
              </div>
              </div>
              </div>
          ):(
            
          <div className="hero-content-container text-center">
            <div className="hero-content">
            
                <h1 className="hero-text"> Game Lobby</h1>
                <div className="hero-subcontainer">
                  <div className="card-body">
                    <h2 className='card-title'>Connected players</h2>
                    <div>
                      <p className="invite-text"></p>
                    </div>
                    <h2 className='card-title'>
                      Invite players
                    </h2>
                    <p className="invite-text">Share the invite link below to let other players join this game!</p>
                    <label>
                      <input className="hero-input" type="text" value={currentUrl} readOnly></input>
                    </label>
                    <div className="hero-copy-container">
                      <button className="hero-copy" onClick={handleCopy}>Copy</button>
                    </div>
                  </div>
                </div>
                <button
                      className="hero-button"
                      onClick={handleStartGame}
                    >
                      Ready to play the game!
                </button>
              </div>
              
        </div>
          )}
          
      </div>
      );
    }
  
export default Play;

