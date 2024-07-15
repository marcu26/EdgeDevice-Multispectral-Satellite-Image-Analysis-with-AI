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

export default function SignUp() {
  const navigate = useNavigate();
  const [errors, setErrors] = React.useState({});
  const [errorMessage, setErrorMessage] = React.useState('');

  const handleAlreadyHaveAccountClick = () => {
    navigate('/');
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const firstName = data.get('firstName');
    const lastName = data.get('lastName');
    const email = data.get('email');
    const password = data.get('password');
    const repeatPassword = data.get('repeatPassword');
  
    const errors = {};
  
    if (!firstName) {
      errors.firstName = 'First Name is required';
    }
    if (!lastName) {
      errors.lastName = 'Last Name is required';
    }
    if (!email) {
      errors.email = 'Email is required';
    } else {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        errors.email = 'Invalid email format';
      }
    }
    if (!password) {
      errors.password = 'Password is required';
    } else if (password.length < 8) {
      errors.password = 'Password must be at least 8 characters';
    }
    if (!repeatPassword) {
      errors.repeatPassword = 'Repeat Password is required';
    }
    if (password !== repeatPassword) {
      errors.repeatPassword = 'Passwords do not match';
    }
  
    if (Object.keys(errors).length === 0) {
      try {
        const response = await axios.post('https://localhost:50001/api/users/create', {
          email: email,
          password: password,
          firstname: firstName,
          lastname: lastName
        });
        console.log(response.data);
        localStorage.setItem('user', JSON.stringify(response.data));
        navigate('/main');
      } catch (error) {
        console.error('Error creating user:', error);
        setErrorMessage(error.response.data.exceptionMessage); 
      }
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
            Sign up
          </Typography>
          <Paper elevation={3}>
            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 1, p: 4 }}>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    autoComplete="given-name"
                    name="firstName"
                    required
                    id="firstName"
                    label="First Name"
                    placeholder="Enter your first name"
                    error={!!errors.firstName}
                    helperText={errors.firstName}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    required
                    id="lastName"
                    name="lastName"
                    label="Last Name"
                    autoComplete="family-name"
                    placeholder="Enter your last name"
                    error={!!errors.lastName}
                    helperText={errors.lastName}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    required
                    id="email"
                    name="email"
                    label="Email Address"
                    autoComplete="email"
                    placeholder="Enter your email address"
                    error={!!errors.email}
                    helperText={errors.email}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    required
                    name="password"
                    type="password"
                    id="password"
                    label="Password"
                    autoComplete="new-password"
                    placeholder="Enter your password"
                    error={!!errors.password}
                    helperText={errors.password}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    required
                    name="repeatPassword"
                    type="password"
                    id="repeatPassword"
                    label="Repeat Password"
                    autoComplete="new-password"
                    placeholder="Repeat your password"
                    error={!!errors.repeatPassword}
                    helperText={errors.repeatPassword}
                  />
                </Grid>
              </Grid>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Sign Up
              </Button>
              {errorMessage && (
                <Typography variant="body2" color="error" align="center" sx={{ mt: 1 }}>
                  {errorMessage}
                </Typography>
              )}
              <Grid container justifyContent="center" sx={{ mb: 4 }}>
                <Grid item>
                  <span
                    style={{ cursor: 'pointer', color: 'blue', textDecoration: 'underline' }}
                    onClick={handleAlreadyHaveAccountClick}
                  >
                    {"Already have an account? Sign In"}
                  </span>
                </Grid>
              </Grid>
            </Box>
          </Paper>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
