import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './index.css'
import ChartPage from "./ChartPage.jsx";

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <Router>
          <Routes>
              <Route path='/' element={<App name='main'/>} />
              <Route path='/Chart' element={<ChartPage />} />
          </Routes>
      </Router>

  </React.StrictMode>,
)
