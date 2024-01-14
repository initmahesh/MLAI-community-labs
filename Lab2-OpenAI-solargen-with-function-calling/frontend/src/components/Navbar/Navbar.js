// src/components/Navbar.js

import React from 'react';
import logo from '../../Assets/logo.png'; // Import your company logo
import './Navbar.css'; // Import your custom CSS for styling
import email from '../../Assets/mail.png';

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="left-section">
      <img src={logo} alt="Company Logo" className="logo" />
        <span className='company-name'>
          {/* Enter Company name here */}
        </span>
      </div>
      {/* <div className="right-section">
      <span className='mail-section'>
        <img src={email} alt="email logo" className="email" />
      </span>
        <span>Email: example@example.com</span>
      </div> */}
    </div>
  );
};

export default Navbar;
