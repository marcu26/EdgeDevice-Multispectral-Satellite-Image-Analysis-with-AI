import React, { useState } from 'react';
import MenuIcon from '@mui/icons-material/Menu';
import { Typography, Button, IconButton, Drawer, List, ListItem, Box } from '@mui/material';
import { useNavigate } from "react-router-dom";

function SideMenu() {
    const [drawerOpen, setDrawerOpen] = useState(false);

    const navigate = useNavigate();

    const handleLogOutClick = () => {
        localStorage.removeItem('user');
        navigate("/");
    };

    const toggleDrawer = () => {
        setDrawerOpen(!drawerOpen);
    };

    const userData = localStorage.getItem('user');
    const userObject = JSON.parse(userData);


    return (
        <>
            <Drawer
                anchor="left"
                open={drawerOpen}
                onClose={toggleDrawer}
            >
                <List style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
                    <ListItem>
                        <Typography variant="body1" align="center">Current User:</Typography>
                    </ListItem>
                    <ListItem>
                        <Typography variant="body1" align="center">{userObject.userName}</Typography>
                    </ListItem>
                    <Box flexGrow={1} />
                    <ListItem>
                        <Button variant="outlined" style={{ margin: 'auto' }} onClick={handleLogOutClick}>Logout</Button>
                    </ListItem>
                </List>
            </Drawer>
            <IconButton onClick={toggleDrawer} style={{ position: 'absolute', left: 0, top: 0 }}>
                <MenuIcon />
            </IconButton>
        </>
    );
}

export default SideMenu;
