import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useNavigate } from "react-router-dom";
import axios from 'axios';

const defaultTheme = createTheme();

export default function SignIn() {
  const navigate = useNavigate();
  const [errors, setErrors] = React.useState({});
  const [errorMessage, setErrorMessage] = React.useState('');
  const [formData, setFormData] = React.useState({
    email: '',
    password: ''
  });

  const handleDontHaveAccountClick = () => {
    navigate('/sign-up');
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value
    });
    setErrors((prevErrors) => ({
      ...prevErrors,
      [name]: ''
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const { email, password } = formData;

    const errors = {};

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
      errors.email = 'Please enter a valid email address';
    }

    if (!password) {
      errors.password = 'Password is required';
    }

    if (Object.keys(errors).length === 0) {
      axios.post('https://localhost:50001/api/users/log-in', { email, password })
        .then(response => {
          console.log('Login successful:', response.data);
          localStorage.setItem('user', JSON.stringify(response.data));
          navigate('/main');
        })
        .catch(error => {
          if (error.response) {
            console.error('Error response:', error.response.data);
            setErrorMessage(error.response.data.exceptionMessage); 
          } else {
            console.error('Error:', error.message);
          }
        });
    } else {
      setErrors(errors);
    }
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="md">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 5,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5" marginBottom={4}>
            Sign in
          </Typography>
          <Paper elevation={3}>
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1, p: 4 }}>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    required
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    autoFocus
                    placeholder="Enter your email address"
                    value={formData.email}
                    onChange={handleChange}
                    error={!!errors.email}
                    helperText={errors.email}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    required
                    id="password"
                    label="Password"
                    type="password"
                    name="password"
                    autoComplete="current-password"
                    placeholder="Enter your password"
                    value={formData.password}
                    onChange={handleChange}
                    error={!!errors.password}
                    helperText={errors.password}
                  />
                </Grid>
              </Grid>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Sign In
              </Button>
              {errorMessage && (
                <Typography variant="body2" color="error" align="center" sx={{ mt: 1 }}>
                  {errorMessage}
                </Typography>
              )}
            </Box>
            <Grid container justifyContent="center" sx={{ mb: 4 }}>
              <Grid item>
                <span
                  style={{ cursor: 'pointer', color: 'blue', textDecoration: 'underline' }}
                  onClick={handleDontHaveAccountClick}
                >
                  {"Don't have an account? Sign Up"}
                </span>
              </Grid>
            </Grid>
          </Paper>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
