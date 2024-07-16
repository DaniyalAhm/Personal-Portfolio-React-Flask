import React from "react";
import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa'; // Import the icons

function Footer() {
    return (
        <footer className="Footer">
            <a href="https://github.com/DaniyalAhm">
                <FaGithub size={24} /> {/* GitHub icon */}
            </a>
            <a className="inverted-icon" href="https://www.linkedin.com/in/daniyal-ahmed-435a36280/">
                <FaLinkedin className="inverted-icon" size={24} /> {/* LinkedIn icon */}
            </a>
            <a className="inverted-icon" href="mailto:daniyala@bu.edu">
                <FaEnvelope className="inverted-icon" size={24} /> {/* Email icon */}
            </a>
        </footer>
    );
}

export default Footer;
