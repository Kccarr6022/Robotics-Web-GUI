import React from 'react'

const Robots = [
  {
    name: 'Spot',
    img: './images/...',
  },
]

const RoboticsDisplay = () => {
  return (
    <div className='robotics-page'>
      <ul>
        {Robots.map(Robot => {
          return (
            <li>
              <h1>{Robot.name}</h1>
            </li>
          )
        })}
      </ul>
    </div>
  )
}

export default RoboticsDisplay