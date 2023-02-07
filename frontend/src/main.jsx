import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './index.css'
import Nav from "./Nav.jsx";

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <Router>
          <Routes>
              <Route path='/' element={<App name='main'/>} />
              <Route path='/change' element={<Nav name='kuku'/>} />
          </Routes>
      </Router>

  </React.StrictMode>,
)
