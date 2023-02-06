import React from 'react'
import axios from 'axios'
import './index.scss'

const RobotControl = () => {
  const handleMove = key => {
    axios.post(process.env.REACT_APP_API_ADDRESS + '/api/spot/move', {
      direction: key,
    })
  }

  document.addEventListener('keydown', function (event) {
    console.log(`Key: ${event.key} with keycode ${event.keyCode} has been pressed`)
    handleMove(event.key)
  })

  return (
    <div className='robot-control-page'>
      <div class='controls-container'>
        <div class='controls-left'>
          <h2>Current Permissions:</h2>
          <button>Request Operator Permissions</button>
        </div>
        <div class='controls-right'>
          <button>Record video</button>
          <button>Screenshot</button>
          <button>Listen to SPOT</button>
          <button>Talk to SPOT</button>
        </div>
      </div>
      <div class='video-border'>
        <h3 style='font-size:18px'>Camera Selection</h3>
      </div>

      <div class='video-container'>
        <div class='video-compass'></div>
        <video class='video-360-view' src=''></video>
        <video class='video-main' controls>
          <source src='movie.mp4' type='video/mp4' />
          <source src='movie.ogg' type='video/ogg' />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  )
}

export default RobotControl
