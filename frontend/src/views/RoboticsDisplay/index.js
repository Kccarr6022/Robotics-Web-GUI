import React from 'react'
import Header from '../../components/Header'
import './index.scss'

const RoboticsDisplay = () => {
  let Logo = '/images/operator-logo.png'

  return (
    <>
      <Header />
      <div className='robotics-page'>
        <h2 className='page-title'>Robotics System Selection</h2>
        <div className='button-container'>
          <a className='button' href='/permissions'>
            <h3>Spot Interface</h3>
            <img src={Logo} alt='logo' className='button-logo' />
            <div className='status-container'>
              <div>Online status: ...</div>
              <p className='status-power'>Power status: ...</p>
            </div>
          </a>
          <a className='button' href='/permissions'>
            <h3>FNAL Interface</h3>
            <img src='images/nav-logo.png' alt='logo' className='button-logo' />
            <div className='status-container'>
              <div>Online status: ...</div>
              <p className='status-power'>Power status: ...</p>
            </div>
          </a>
        </div>
        <div className='box'>
          <div className='box-child'></div>
        </div>
      </div>
    </>
  )
}

export default RoboticsDisplay
