import React from 'react'
import logo from './images/logo.png'
import './index.scss'

const Header = () => {
  const Logout = () => {
    sessionStorage.clear()
  }
  return (
    <nav className='header'>
      <img className='header-logo' src={logo} />
      <ul className='header-items'>
        <li></li>
        <li>
          <a href='/robotics'>Robotic Selection</a>
        </li>
        <li>
          <a href='/permissions'>Permissions</a>
        </li>
        <li>
          <a href='/view'>View</a>
        </li>
        <li className='Logout'>
          <a onClick={Logout}>Logout</a>
        </li>
      </ul>
    </nav>
  )
}

export default Header
