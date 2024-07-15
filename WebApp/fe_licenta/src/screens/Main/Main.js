import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
    Container, Grid, Typography, TextField, Button, IconButton, Box, Checkbox, FormControlLabel,
    Pagination, Snackbar, Alert
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import CloudDownloadIcon from '@mui/icons-material/CloudDownload';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import SideMenu from '../../components/SideMenu';
import HelpMenu from '../../components/HelpMenu';
import ImageWithDescription from '../../components/Image';
import './MainPage.css'; // Import CSS file

function MainPage() {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [open, setOpen] = useState(false);
    const [page, setPage] = useState(1);
    const [images, setImages] = useState([]);
    const [selectedImages, setSelectedImages] = useState([]);
    const [selectAll, setSelectAll] = useState(false);
    const [numPages, setNumPages] = useState(1);
    const [locationSearch, setLocationSearch] = useState('');
    const [sortField, setSortField] = useState('');
    const [isDescending, setIsDescending] = useState(true);
    const [snackbarOpen, setSnackbarOpen] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState('');

    useEffect(() => {
        fetchImages();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [page, sortField, isDescending]);

    const downloadImagesRgb = async () => {
        if (!selectedImages.includes(true)) {
            setSnackbarMessage('No image selected');
            setSnackbarOpen(true);
            return;
        }
        const userData = localStorage.getItem('user');
        const userObject = JSON.parse(userData);
        const token = userObject.token;

        for (const [index, isSelected] of selectedImages.entries()) {
            if (isSelected) {
                const imageUrl = images[index].rgbImage;
                const imageName = imageUrl.split('/').pop();
                const downloadUrl = `https://localhost:50000/api/analize-results/download-image-png/${imageName}`;

                try {
                    const response = await axios.get(downloadUrl, {
                        method: "GET",
                        responseType: 'blob',
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    });

                    const url = window.URL.createObjectURL(new Blob([response.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', imageName);
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);

                    console.log(`Image ${imageName} downloaded successfully`);
                } catch (error) {
                    console.error(`Error downloading the image ${imageName}:`, error);
                }
            }
        }
    };

    const downloadImagesOverlay = async () => {
        if (!selectedImages.includes(true)) {
            setSnackbarMessage('No image selected');
            setSnackbarOpen(true);
            return;
        }
        const userData = localStorage.getItem('user');
        const userObject = JSON.parse(userData);
        const token = userObject.token;

        for (const [index, isSelected] of selectedImages.entries()) {
            if (isSelected) {
                const imageUrl = images[index].overlay;
                const imageName = imageUrl.split('/').pop();
                const downloadUrl = `https://localhost:50000/api/analize-results/download-image-png/${imageName}`;

                try {
                    const response = await axios.get(downloadUrl, {
                        method: "GET",
                        responseType: 'blob',
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    });

                    const url = window.URL.createObjectURL(new Blob([response.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', imageName);
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);

                    console.log(`Image ${imageName} downloaded successfully`);
                } catch (error) {
                    console.error(`Error downloading the image ${imageName}:`, error);
                }
            }
        }
    };

    const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    const triggerDownload = async (url) => {
        const link = document.createElement('a');
        link.href = url;
        link.download = url.substring(url.lastIndexOf('/') + 1);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };
    
    const downloadSentinel2Images = async () => {
        if (!selectedImages.includes(true)) {
            setSnackbarMessage('No image selected');
            setSnackbarOpen(true);
            return;
        }
        for (const [index, isSelected] of selectedImages.entries()) {
            if (isSelected) {
                const imageUrl = images[index].sentinel2Image;
                await triggerDownload(imageUrl);
                await delay(100);  
            }
        }
    };
    
    const downloadMasks = async () => {
        if (!selectedImages.includes(true)) {
            setSnackbarMessage('No image selected');
            setSnackbarOpen(true);
            return;
        }
        for (const [index, isSelected] of selectedImages.entries()) {
            if (isSelected) {
                const imageUrl = images[index].mask;
                await triggerDownload(imageUrl);
                await delay(100);  
            }
        }
    };

    const downloadAll = async () => {
        if (!selectedImages.includes(true)) {
            setSnackbarMessage('No image selected');
            setSnackbarOpen(true);
            return;
        }
        await downloadSentinel2Images();
        await downloadImagesRgb();
        await downloadMasks();
        await downloadImagesOverlay();
    };

    const fetchImages = async () => {
        try {
            const userData = localStorage.getItem('user');
            const userObject = JSON.parse(userData);
            const token = userObject.token;

            const response = await axios.post(
                'https://localhost:50000/api/analize-results/get-analize-results-pageable',
                {
                    draw: 9,
                    start: (page - 1) * 9,
                    length: 9,
                    sortField: sortField ? sortField : null,
                    isDescending: isDescending,
                    location: locationSearch ? locationSearch : null,
                    startDate: startDate ? startDate : null,
                    endDate: endDate ? endDate : null,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            setImages(response.data.data);
            setNumPages(Math.ceil(response.data.recordFiltered / 9));
            setSelectedImages(new Array(response.data.data.length).fill(false));
            setSelectAll(false);
        } catch (error) {
            console.error('Error fetching images:', error);
        }
    };

    const handleStartDateChange = (event) => {
        setStartDate(event.target.value);
    };

    const handleEndDateChange = (event) => {
        setEndDate(event.target.value);
    };

    const handleOpen = () => {
        setOpen(true);
    };
    
    const handleClose = () => {
        setOpen(false);
    };

    const handlePageChange = (event, value) => {
        setPage(value);
    };

    const handleSelectAll = (event) => {
        const checked = event.target.checked;
        const newSelectedImages = selectedImages.map(() => checked);
        setSelectedImages(newSelectedImages);
        setSelectAll(checked);
    };

    const handleImageSelect = (index) => (event) => {
        const checked = event.target.checked;
        const newSelectedImages = [...selectedImages];
        newSelectedImages[index] = checked;
        setSelectedImages(newSelectedImages);

        if (!checked) {
            setSelectAll(false);
        } else if (newSelectedImages.every(Boolean)) {
            setSelectAll(true);
        }
    };

    const handleSortUp = (field) => {
        setSortField(field);
        setIsDescending(true);
    };

    const handleSortDown = (field) => {
        setSortField(field);
        setIsDescending(false);
    };

    return (
        <>
            <SideMenu />
            <div className="help-button-wrapper">
                <IconButton size="large" onClick={handleOpen}>
                    <HelpOutlineIcon />
                </IconButton>
            </div>
            <Container maxWidth="lg">
                <Grid container spacing={2} alignItems="center">
                    <Grid item xs={12} marginTop={3} marginBottom={1}>
                        <Grid container justifyContent="space-between" alignItems="center">
                            <Grid item>
                                <TextField label="Search" size="small" style={{ marginBottom: '8px', width: '500px', backgroundColor: 'white'}} value={locationSearch} onChange={(event) => setLocationSearch(event.target.value)} />
                            </Grid>
                            <Grid item>
                                <TextField
                                    type="date"
                                    label="Start Date"
                                    value={startDate.split('T')[0]}
                                    onChange={handleStartDateChange}
                                    InputLabelProps={{
                                        shrink: true,
                                    }}
                                    size="small"
                                    style={{ marginBottom: '8px', backgroundColor: 'white' }}
                                />
                            </Grid>
                            <Grid item>
                                <TextField
                                    type="date"
                                    label="End Date"
                                    value={endDate.split('T')[0]}
                                    onChange={handleEndDateChange}
                                    InputLabelProps={{
                                        shrink: true,
                                    }}
                                    size="small"
                                    style={{ marginBottom: '8px', backgroundColor: 'white'  }}
                                />
                            </Grid>
                            <Grid item>
                                <Button variant="contained" startIcon={<SearchIcon />} size="large" style={{ marginLeft: '8px', marginBottom: '0px' }} onClick={fetchImages}>
                                    Search
                                </Button>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
                <Grid container justifyContent="space-between" alignItems="center" marginBottom={'10px'}>
                    <Grid item>
                        <Button startIcon={<CloudDownloadIcon />} variant="outlined" size="large" onClick={downloadSentinel2Images}  style={{ backgroundColor: 'white' }}>
                            Sentinel-2 Images
                        </Button>
                    </Grid>
                    <Grid item>
                        <Button startIcon={<CloudDownloadIcon />} variant="outlined" size="large" onClick={downloadImagesRgb} style={{ backgroundColor: 'white' }}>
                            RGB Images
                        </Button>
                    </Grid>
                    <Grid item>
                        <Button startIcon={<CloudDownloadIcon />} variant="outlined" size="large" onClick={downloadMasks} style={{ backgroundColor: 'white' }}>
                            Masks
                        </Button>
                    </Grid>
                    <Grid item>
                        <Button startIcon={<CloudDownloadIcon />} variant="outlined" size="large" onClick={downloadImagesOverlay} style={{ backgroundColor: 'white' }}>
                            Overlays
                        </Button>
                    </Grid>
                    <Grid item>
                        <Button startIcon={<CloudDownloadIcon />} variant="outlined" size="large" onClick={downloadAll} style={{ backgroundColor: 'white' }}>
                            All
                        </Button>
                    </Grid>
                </Grid>
                <Box border={1} borderRadius={'5px'} paddingLeft="20px" paddingRight="20px" backgroundColor="white">
                    <Grid container alignItems="center" style={{ justifyContent: "space-between" }}>
                        <Grid item>
                            <Typography variant="body1" display="inline">Date</Typography>
                            <IconButton size="small" onClick={() => handleSortUp('CreatedAt')}><ArrowUpwardIcon /></IconButton>
                            <IconButton size="small" onClick={() => handleSortDown('CreatedAt')}><ArrowDownwardIcon /></IconButton>
                        </Grid>

                        <Grid item>
                            <Typography variant="body1" display="inline">Unusable Percentage</Typography>
                            <IconButton size="small" onClick={() => handleSortUp('UnusablePercentage')}><ArrowUpwardIcon /></IconButton>
                            <IconButton size="small" onClick={() => handleSortDown('UnusablePercentage')}><ArrowDownwardIcon /></IconButton>
                        </Grid>

                        <Grid item>
                            <Typography variant="body1" display="inline">Location Alphabetically</Typography>
                            <IconButton size="small" onClick={() => handleSortUp('Location')}><ArrowUpwardIcon /></IconButton>
                            <IconButton size="small" onClick={() => handleSortDown('Location')}><ArrowDownwardIcon /></IconButton>
                        </Grid>
                    </Grid>
                </Box>
                <Grid item xs={12} marginBottom={'15px'}>
                    <FormControlLabel
                        label="Select All Images"
                        control={<Checkbox checked={selectAll} onChange={handleSelectAll} />}
                    />
                </Grid>

                <Grid container spacing={2}>
                    {images.map((image, index) => (
                        <Grid item xs={12} sm={4} key={image.id}>
                            <Box padding="10px">
                                <FormControlLabel
                                    control={
                                        <Checkbox
                                            checked={selectedImages[index]}
                                            onChange={handleImageSelect(index)}
                                        />
                                    }
                                    label="Select"
                                />
                                <ImageWithDescription
                                    images={[
                                        { imageUrl: image.rgbImage },
                                        { imageUrl: image.overlay }
                                    ]}
                                    description={`Location: ${image.location}\nLatitude: ${image.latitude}\nLongitude: ${image.longitude}\nUnusable Percentage: ${image.unusablePercentage}%\nAquisition Date: ${image.createdAt}`}
                                />

                            </Box>
                        </Grid>
                    ))}
                </Grid>
                <Box display="flex" justifyContent="center" marginTop={2} marginBottom={2}>
                    <Pagination
                        count={numPages}
                        page={page}
                        onChange={handlePageChange}
                        color="primary"
                    />
                </Box>
            </Container>
            <HelpMenu open={open} handleClose={handleClose} />
            <Snackbar open={snackbarOpen} autoHideDuration={6000} onClose={() => setSnackbarOpen(false)}>
                <Alert onClose={() => setSnackbarOpen(false)} severity="error" sx={{ width: '100%' }}>
                    {snackbarMessage}
                </Alert>
            </Snackbar>
        </>
    );
}

export default MainPage;
