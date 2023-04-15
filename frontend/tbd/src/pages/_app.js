import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
//import from components
import { MovieCardComponent } from '../components/movieCard';


export default function App() {
  return (
    <div className="container">
      {/* Title */}
      <h1 className="title">TBD</h1>

      {/* Image Cards */}
      <div className="MoviePosterComponent">
        <div className="image-card">
          {/* Image 1 */}
          <MovieCardComponent imagePath="path/to/image1.jpg" altText="Image 1" text="Image 1 Text" />
        </div>
        <div className="image-card">
          {/* Image 2 */}
          <MovieCardComponent imagePath="path/to/image2.jpg" altText="Image 2" text="Image 2 Text" />
        </div>
      </div>

      {/* Buttons */}
      <div className="button-container">
        <button className="button">
          <FontAwesomeIcon icon={['fas', 'thumbs-up']} /> {/* Use proper syntax for FontAwesomeIcon */}
        </button>
        <button className="button">
          <FontAwesomeIcon icon={['fas', 'question']} /> {/* Use proper syntax for FontAwesomeIcon */}
        </button>
        <button className="button">
          <FontAwesomeIcon icon={['fas', 'thumbs-down']} /> {/* Use proper syntax for FontAwesomeIcon */}
        </button>
      </div>
    </div>
  );
}
