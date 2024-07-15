import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";

import SignIn from './screens/SignIn/SignIn';
import SignUp from './screens/SignUp/SignUp';
import MainPage from './screens/Main/Main';



function App() {
  return (
    <div>
    <div className='wrapper'>
      <div className='contentApp'>
        <Router>
          <Routes>
          <Route path='/' element={<SignIn />} />
          <Route path='/sign-up' element={<SignUp />} />
          <Route path='/main' element={<MainPage />} />
          </Routes>
        </Router>
      </div>
    </div>
    </div>
  );
}

export default App;
