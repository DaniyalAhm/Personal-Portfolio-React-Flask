import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Projects() {
  const [repos, setRepos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/repos')
      .then(response => {
        setRepos(response.data);
      })
      .catch(error => {
        console.error('Error fetching the repositories:', error);
      });
  }, []);

  return (

    <div>
      <h2 className='Section_Title'>Projects </h2>
    <div className="ProjectsContainor">

      <div className="Projects">
        {repos.map((repo) => (
          <div key={repo.name}>
            <a href={repo.url} target="_blank" rel="noopener noreferrer">{repo.name}</a>
            <p>{repo.description}</p>
          </div>
          
        ))}
        </div>
        </div>
</div>
  );
}

export default Projects;
