import React from "react";
import "./Header.css";

function Header() {


    return (
        <header className="Header">



            <h1
            style={{fontSize: "500%"}}
            >Daniyal  Ahmed
            </h1>
            <p classname='Aboutme'>I am Daniyal Ahmed, a software developer and data science enthusiast with a keen interest in building cutting-edge applications and exploring complex data insights. 
                My educational and professional journey has equipped me with a robust knowledge base in machine learning and backend development, utilizing technologies like Node.js, Flask, and C++. 
                My portfolio reflects a variety of projects, from developing machine learning models from scratch to engineering full-stack solutions that address real-world challenges.
                 I am continuously seeking opportunities to collaborate on projects that push the limits of technology, while advancing my skills through hands-on experience and ongoing education. 
                 Feel free to explore my LinkedIn and GitHub profiles to see more about my work and what I'm currently tackling.

</p>


            <a href="/resume.pdf">Download My Resume</a>


            <hr></hr>






        </header>
    );
}

export default Header;