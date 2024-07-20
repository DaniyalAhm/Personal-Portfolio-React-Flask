import './App.css';
import Header from './components/header';
import Projects from './components/Projects';
import Footer from './components/Footer';
import React from 'react';

function App() {
  return (
    <div className="App">
      <div className="star-container">
        {Array.from({ length: 45 }).map((_, index) => (
          <div key={index} className="star"></div>
        ))}
      </div>
      <Header />
      <Projects className="Projects" />
      <Footer className="Footer" />
    </div>
  );
}

export default App;
