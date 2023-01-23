import React, { useContext, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import FermiLabLogo from './images/FermiLabLogo.png'
import './index.scss'

import axios from 'axios'

const Login = () => {
  const [prompt, setPrompt] = useState(null)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleUsernameChange = e => {
    setUsername(e.target.value)
  }

  const handlePasswordChange = e => {
    setPassword(e.target.value)
  }

  const handleLogin = () => {
    try {
      axios
        .post(process.env.REACT_APP_API_ADDRESS + 'api/login', {
          username: username,
          password: password,
        })
        .then(response => {
          response.status === 200 && response.data['msg'] == 'Successful login' ? navigate('/robotics') : setPrompt(response.data['msg'])
        })
        .catch(e => {
          console.log(e)
        })
    } catch (e) {
      console.log(e)
    }
  }

  return (
    <div className='login-page'>
      <img src={FermiLabLogo} className='login-logo' />
      <h1 className='login-title'>Robotic Systems Login</h1>
      <div className='login-username'>
        <label for='username'>Username:</label>
        <input id='username' value={username} onChange={handleUsernameChange} />
      </div>
      <div className='login-password'>
        <label for='password'>Password:</label>
        <input id='password' value={password} onChange={handlePasswordChange} type='password' />
      </div>
      <button className='login-button' onClick={handleLogin}>
        Login
      </button>
      <div className='box-1'>
        <div className='box-2'></div>
      </div>
      {prompt && (
        <div className='login-prompt'>
          <h1>Wrong username or password</h1>
          <button
            onClick={() => {
              setPrompt(null)
            }}
          >
            Continue
          </button>
        </div>
      )}
    </div>
  )
}

export default Login
