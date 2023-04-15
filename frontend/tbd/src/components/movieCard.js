import React from 'react';

//specific media card examples
export const MoviePosterComponent = () => {
    return (
      <div className="movie-poster">
        <img
          src="path/to/movie-poster.jpg"
          alt="Movie Poster"
          style={{ width: '1200px', height: '3000px', maxWidth: '100%', height: 'auto' }}
        />
      </div>
    );
};
