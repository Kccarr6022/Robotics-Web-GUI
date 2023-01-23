import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Login from './views/Login'
import RoboticsDisplay from './views/RoboticsDisplay'

import './index.scss'

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login />} />
      <Route exact path='/robotics' element={<RoboticsDisplay />} />
    </Routes>
  </BrowserRouter>
)
