import React, { useState } from 'react';

const ChatApp = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    const newMessage = { id: Date.now(), text: input, sender: 'user' };
    setMessages([...messages, newMessage]);
    setInput('');

    // Here you would add the logic to send the input to your backend and get the response
  };

  return (
    <div className="chat-container">
      <ul className="message-list">
        {messages.map((message) => (
          <li key={message.id} className={`message-item ${message.sender}`}>
            {message.text}
          </li>
        ))}
      </ul>
      <form onSubmit={sendMessage} className="message-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="message-input"
          placeholder="Type your message here..."
        />
        <button type="submit" className="send-button">Send</button>
      </form>
    </div>
  );
};

export default ChatApp;
