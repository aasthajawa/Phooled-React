import React, { useEffect, useState } from 'react';
import Header from '../Header/Header';
import { useNavigate ,useLocation} from 'react-router-dom';

import './Game.css';
const Game = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [avatars, setAvatars] = useState([]);
  const [selectedAvatar, setSelectedAvatar] = useState(null);
  const [activeGames, setActiveGames] = useState([]);

  
  useEffect(() => {
    const displayGames = async () => {
      try {
          const response = await fetch('http://localhost:8000/api/game/phish-game', {
              method: 'GET',
              headers: {
                  'Content-Type': 'application/json'
              },
              credentials: 'include'
          });
          if (response.ok) {
              const data = await response.json();
              console.log("displaydata", data);
              console.log("displaydata2", data.context.active_games);
              setActiveGames(data.context.active_games);
          } else {
              console.error('Failed to fetch user data');
          }
      } catch (error) {
          console.error('Error fetching user data:', error);
      }
  };

  displayGames();
  // Fetch avatars from the backend when the component mounts
  fetchAvatars();
  }, []);

  useEffect(() => {
    console.log("Updated selectedAvatar:", selectedAvatar);
  }, [selectedAvatar]);

  const fetchAvatars = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/images/');
      if (response.ok) {
        const data = await response.json();
        console.log("images data", data)
        setAvatars(data)
      } else {
        console.error('Failed to fetch avatars');
      }
    } catch (error) {
      console.error('Error fetching avatars:', error);
    }
  };

  const handleAvatarSelection = (avatar) => {
    console.log("i am in function");
    console.log("Avatar", avatar);
    setSelectedAvatar(avatar);
    console.log("selectedAvatar", selectedAvatar);
  };


  const createRoomAPI = async () => {
    try {
    
      console.log("yha tak aya ");
      const response = await fetch('http://localhost:8000/api/phish-game/create', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          // Add any other headers if needed
        },
        credentials: 'include'
        //body: JSON.stringify({
          //roomName: selectedAvatar.name,  // Replace with your desired room name
          //gameStarter: user.User.user_id,
        //}),
      });
      console.log("response",response)
      if (response.ok) {
        const data = await response.json();
        console.log("game data",data);
        // Room created successfully, redirect to the Play page
        navigate("/game/phish-game/room/" + data.context.room_id);
      } else {
        // Handle the case where room creation failed
        console.error('Error creating room:', response.statusText);
      }
    } catch (error) {
      console.error('Error creating room:', error);
    }
  };

  return (
      <div>
       <Header />
       <div id="main" className="contentOFF" role="main">
         <div className="hero-content text-center">
            <div className="max-w-md">
              <div className="card">
                <div className="card-body">
                  <h2 className="card-title">Select Avatar</h2>
                  <div className="avatar-picker">
                    {avatars.map((avatar, index) => (
                      <div key={index} className="avatar-animal" onClick={() => handleAvatarSelection(avatar)}>
                        <img className="avatar-animal-img" src={`http://localhost:8000${avatar.image}`}  alt={avatar.name}></img>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
              <button className="startbutton" onClick={createRoomAPI}>Start new game</button>
            </div>
          </div>
          <div className="container">
            <div className="row row-hero">
              <div className="col col-hero">
                <h1 className="hero-heading">Join an active game lobby</h1>
                <table className='table-hero'>
                  <thead className='table-head'>
                    <tr className='table-row'>
                      <th>#</th>
                      <th>Host Name</th>
                      <th>Room Id</th>
                      <th>Link</th>
                    </tr>
                  </thead>
                  <tbody>
                    {activeGames.map((game, index) => (
                      <tr key={index}>
                        <td>{game.id}</td>
                        <td>{game.host}</td>
                        <td><a href={`/game/phish-game/room/${game.id}`}>Join</a></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        </div>
  );
};

export default Game;