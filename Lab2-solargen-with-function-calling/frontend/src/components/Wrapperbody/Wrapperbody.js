// src/components/Navbar.js

import React from 'react';
import './Wrapperbody.css';

const Wrapperbody = () => {
  return (
    <div className='body-wrapper'>
        <div className='body-container'>
            <div className='body-header'>
                <h2>Your Personal Solar Potential Assistant</h2>
            </div>
            <div className='body-desc'>
                <p>Ask you Solar panel related query to this our Solar Assistant.<br/> <br/><span className='bulletted-content'>Always active and ready to go.</span></p>
            </div>
        </div>
    </div>
  );
};

export default Wrapperbody;