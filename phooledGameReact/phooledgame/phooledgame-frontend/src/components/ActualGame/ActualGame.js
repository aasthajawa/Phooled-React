import React, { useState} from 'react';
import './ActualGame.css';
const ActualGame = () => {

  const [selectedImage, setSelectedImage] = useState('/assets/images/sample1.png');
  const [classification, setClassification] = useState('True');

  const showImage = (imageSrc) => {
    setSelectedImage(imageSrc);
  };

  const handleClassificationChange = (event) => {
    setClassification(!classification);
  };

    return (
      <div>
        <div className="sticky">
        <div className="header">
            <img className="header-img" src="/assets/images/logo-white.png" alt = "Phooled header logo"></img>
        </div>
        <div className="container-rules">
            <div className="stat">
            <img  className="heart" src='assets/images/heart.png'></img>
            </div>
        </div>
        </div>
        <div>
            <div className="image-container">
                <img src={selectedImage} alt="Selected Image" />
            </div>
        </div>
        <div className="button-container-hero">
        
            <button className="phishing button-hero" onClick={handleClassificationChange}>Phishing</button>
           
            <button className="non-phishing button-hero" onClick={handleClassificationChange}>Non-Phishing</button>
        
        </div>
        <div className="class-image-container">
            <div className="image" onClick={() => showImage('/assets/images/sample1.png')}>
                <img src="/assets/images/default.png" alt="Image 1" />
            </div>
            <div className="image" onClick={() => showImage('/assets/images/sample2.png')}>
                <img src="/assets/images/default.png" alt="Image 2" />
            </div>
            <div className="image" onClick={() => showImage('/assets/images/sample3.png')}>
                <img src="/assets/images/default.png" alt="Image 3" />
            </div>
        </div>
    </div>
    );
}

export default ActualGame;