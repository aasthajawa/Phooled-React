import React, {Component } from 'react';
import './Rules.css';
import { useNavigate } from 'react-router-dom';

const Rules = () => {
    return(
        <div>
          <div className="header">
            <img className="header-img" src='assets/images/logo-white.png'></img>
          </div>
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
                    max="2"
                    className="range"
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
                <button className="btn btn-primary my-4">
                    Save
                </button>
              </div>
            </div>
            </div>
          </div>
      
        
    );
};

export default Rules;