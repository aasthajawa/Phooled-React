import React, { Component } from "react";
import { Route, Routes } from 'react-router-dom';
import Login from './components/Login/Login';
import Signup from './components/Signup/Signup';
import Dashboard from './components/Dashboard/Dashboard';
import Home from './components/Home/Home';
import Game from './components/Game/Game';
import Play from './components/Play/Play';
import Rules from './components/Rules/Rules';
import ActualGame from "./components/ActualGame/ActualGame";

class App extends Component {
  render() {
    return (  
        <div>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element ={<Login/>} />
            <Route path="/signup" element={<Signup/>} />
            <Route path="/game/dashboard" element={<Dashboard/>} />
            <Route path="/game/phish-game" element ={<Game />}></Route>
            <Route path="/game/phish-game/room/:roomId" element={<Play />} />
            <Route path="/game/phish-game/room/:roomId/quickfire" element={<ActualGame />} />
            <Route path="/rules" element={<Rules />}></Route>
          </Routes>
        </div>
    );
  }
}

export default App;