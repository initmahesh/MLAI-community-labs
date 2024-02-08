import React, { useState, useRef, useEffect } from 'react';
import { Button, FormControl, InputGroup, ListGroup } from 'react-bootstrap';
import axios from 'axios';
import './App.css'; // Import the CSS file
import { Helmet } from 'react-helmet';

import Navbar from './components/Navbar/Navbar';
import backgroundImage from './Assets/body.jpg';
import sun from './Assets/contrast.png';
import chatlogo from './Assets/chat.png';
import Wrapperbody from './components/Wrapperbody/Wrapperbody';
import TextWithLineBreaks from './components/textlinebreak';

// Generate a random integer between min (inclusive) and max (exclusive)
const randomInteger = Math.floor(Math.random() * (10000000 - 1) + 1);
console.log(randomInteger)
const App = () => {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');
  const [loading, setLoading] = useState(false);
  const [showChat, setShowChat] = useState(true);

  const sendMessage = async () => {
    if (inputText.trim() === '') return;

    // Add user message to the chat
    setMessages((prevMessages) => [...prevMessages, { text: inputText, sender: 'user' }]);
    setInputText('');
    setLoading(true);

    // Send user message to the backend for processing
    // https://solar-gen.onrender.com/api/experiments-openai
    try {
      const response = await axios.post('https://solar-gen.onrender.com/api/experiments-openai', {
        "message": inputText,
        "Identifier":randomInteger
      });
      console.log(response)
      const botMessage = response.data["response"];

      // Simulate a delay for loading indication
      await new Promise((resolve) => setTimeout(resolve, 1000));

      // Add bot response to the chat
      setMessages((prevMessages) => [...prevMessages, { text: botMessage, sender: 'bot' }]);
    } catch (error) {
      console.error('Error processing message:', error);
    } finally {
      setLoading(false);
    }
  };
  const backgroundStyle = {
    backgroundImage: `url(${backgroundImage})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100%',
    height: '100%'
  }
  const messageContainerRef = useRef(null);

  useEffect(() => {
    //Scroll to the bottom when messages change
    if (messageContainerRef.current) {
      messageContainerRef.current.scrollTop = messageContainerRef.current.scrollHeight;
    }
  }, [messages]);

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div>
    <Helmet>
          <title>Solar Gen</title>
    </Helmet>
    <div style={backgroundStyle}>
      <Navbar />
      <div className="chat-wrapper">
        <Wrapperbody />
      <div className="message-icon" onClick={() => setShowChat(!showChat)}>
              <span><img src={chatlogo} alt="chat logo" className="chatlogo" /></span>
            </div>
            {showChat &&(
        <div className="chat-container">
          <div className="chat-header">
            <div className="chat-bar">
            <span><img src={sun} alt="sun logo" className="sun-logo" /></span>
            <span><h3>Your Solar Assistant</h3></span>
            </div>
          </div>
          <div>
            <ListGroup className="message-list"
              ref={messageContainerRef}
              // Adjust as needed
            >
              {messages.map((message, index) => (
                <ListGroup.Item
                  key={index}
                  className={`message-item ${message.sender === 'user' ? 'user-item' : 'bot-item'}`}
                >
                  <div className={`${message.sender === 'user' ? 'user' : 'bot'}`} >
                    <TextWithLineBreaks text = {message.text} /></div>
                </ListGroup.Item>
              ))}
              {loading && <div className={`message-item `}><div className='bot'>Loading...</div></div>}
            </ListGroup>

          
          </div>

          <div className="input-group">
          <InputGroup >
            <FormControl
              placeholder="Type your message..."
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={handleKeyPress}
            />
            <Button onClick={sendMessage} variant="primary">
              Send
            </Button>
          </InputGroup>
          </div>
        </div>)}
      </div>
    </div>
    </div>
  );
};

export default App;
