import React from 'react'
import './index.scss'

const Header = () => {
  let logo = '/images/logo.png'
  const Logout = () => {
    sessionStorage.clear()
  }
  return (
    <nav>
      <div className='nav-left'>
        <ul>
          <li>
            <img src={logo} alt='logo' />
          </li>
          <li>
            <a href='/selection'>Robotics Selection</a>
          </li>
          <li>
            <a href='/permissions'>Permissions</a>
          </li>
          <li>View</li>
        </ul>
      </div>
      <div className='nav-right'>
        <ul>Logout</ul>
      </div>
    </nav>
  )
}

export default Header
