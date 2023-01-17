import React, { useContext, useState } from 'react'
import FermiLabLogo from './images/FermiLabLogo.png'
import './index.scss'

const Login = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleUsernameChange = e => {
    setUsername(e.target.value)
  }

  const handlePasswordChange = e => {
    setPassword(e.target.value)
  }

  const handleLogin = () => {}

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
    </div>
  )
}

export default Login
