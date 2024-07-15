import './App.css';
import Header from './components/header';
import Projects from './components/Projects';
import Footer from './components/Footer';
import React from 'react';

function App() {
  return (
    <div className="App">
      <Header  />

      <Projects className='Projects' />
      

      <Footer className='Footer' />
    </div>
  );
}

export default App;
