import React from 'react';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const HelpMenu = ({ open, handleClose }) => {
  return (
    <Dialog open={open} onClose={handleClose}>
      <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginTop: '5px' }}>
        <DialogTitle>Help Menu</DialogTitle>
      </Box>

      <DialogContent>
        <Typography paragraph>
          - The provided images are of Sentinel2 type.
        </Typography>
        <Typography paragraph>
          - Their size is 512 x 512 pixels, with 13 channels each.
        </Typography>
        <Typography paragraph>
          - After selecting the images, you can download one of the 4 image formats, by clicking the download buttons.
        </Typography>
        <Typography paragraph>
           - Sentinel2 = Image with all 13 channels. <br/>
           - RGB = Image with the 3 channels (red, green, blue).<br/>
           - Masks = Cloud mask resulted in analysis.<br/>
           - Overlay = An overlay between the mask (every type of cloud is a color) and the rgb image.
        </Typography>
        <Typography paragraph>
          - The RGB image can be opened in the gallery, for the satellite image you will need a specialized application, e.g., SNAP.
        </Typography>
        <Typography paragraph>
          - Blue = Clear, Yellow = Thick Cloud, Green = Thin Cloud, Red = Shadow.
        </Typography>
      </DialogContent>
      <DialogActions>
        <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginTop: '50px' }}>
          <Button onClick={handleClose} color="primary">
            OK
          </Button>
        </Box>
      </DialogActions>
    </Dialog>
  );
};

export default HelpMenu;
