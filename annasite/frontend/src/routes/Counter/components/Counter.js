import React from 'react'
import {Helmet} from "react-helmet"
import PropTypes from 'prop-types'

export const Counter = ({ counter, increment, doubleAsync }) => (
  <div style={{ margin: '0 auto' }} >
    <Helmet>
      <title>Counter</title>
    </Helmet>
    <h2>Counter: {counter}</h2>
    <button className='btn btn-primary' onClick={increment}>
      Increment
    </button>
    {' '}
    <button className='btn btn-secondary' onClick={doubleAsync}>
      Double (Async)
    </button>
  </div>
)
Counter.propTypes = {
  counter: PropTypes.number.isRequired,
  increment: PropTypes.func.isRequired,
  doubleAsync: PropTypes.func.isRequired,
}

export default Counter
