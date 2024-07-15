import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';
import Carousel from 'react-material-ui-carousel';

function ImageWithDescription({ images, description, tiffLinks }) {
  // Split the description string into an array of lines
  const descriptionLines = description.split('\n');

  return (
    <Card>
      <Carousel
        autoPlay={false}
        navButtonsAlwaysVisible
        indicators={false}
      >
        {images.map((image, index) => (
          <div
            key={index}
            style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              height: '300px',
              marginTop: '15px'
            }}
          >
            <img
              src={image.imageUrl}
              alt={`Slide ${index}`}
              style={{ maxHeight: '100%', maxWidth: '100%' }}
            />
          </div>
        ))}
      </Carousel>
      <CardContent>
        {/* Render each line of the description as a separate Typography component */}
        {descriptionLines.map((line, index) => (
          <Typography key={index} variant="body2" color="textSecondary" component="p">
            {line}
          </Typography>
        ))}
      </CardContent>
    </Card>
  );
}

export default ImageWithDescription;
