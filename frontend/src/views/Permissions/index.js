import React from 'react'
import Header from '../../components/Header'

const Permissions = () => {
  let OperatorLogo = 'images/nav-logo.png'
  
  return (
    <>
      <Header />
      <div className='permissions-page'>
        <h2 className='page-title'>Robotics System Selection</h2>
        <div className='button-container'>
          <a className='button' href='/gui'>
            <h3>Operator Interface</h3>
            <img src={OperatorLogo} alt='logo' className='button-logo' />
            <div className='status-container'>
              <div>Operator status: ...</div>
            </div>
          </a>
          <a className='button' href='/gui'>
            <h3>Viewer Interface</h3>
            <img src='images/viewer-logo.png' alt='logo' className='button-logo' />
          </a>
        </div>
        <div className='box'>
          <div className='box-child'></div>
        </div>
      </div>
    </>
  )
}

export default Permissions
