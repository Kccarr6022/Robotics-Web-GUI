import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Login from './views/Login'
import RoboticsDisplay from './views/RoboticsDisplay'
import Permissions from './views/Permissions'
import RobotControl from './views/RobotControl'

import './index.scss'

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login />} />
      <Route exact path='/selection' element={<RoboticsDisplay />} />
      <Route exact path='/permissions' element={<Permissions />} />
      <Route exact path='/operator' element={<RobotControl />} />
    </Routes>
  </BrowserRouter>
)
