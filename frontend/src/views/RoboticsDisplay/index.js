import React from 'react'
import Header from '../../components/Header'

const Robots = [
  {
    name: 'Spot Interface',
    img: './images/...',
  },
]

const RoboticsDisplay = () => {
  return (
    <>
      <Header />
      <div className='robotics-page'>
        <ul>
          {Robots.map(Robot => {
            return (
              <li>
                <h1>{Robot.name}</h1>
                <img src={Robot.img} alt={Robot.name} />
              </li>
            )
          })}
        </ul>
      </div>
    </>
  )
}

export default RoboticsDisplay
