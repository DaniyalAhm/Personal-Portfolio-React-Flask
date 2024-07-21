import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Projects() {
  const [repos, setRepos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/repos')
      .then(response => {
        setRepos(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching the repositories:', error);
      });
  }, []);

  if (loading) {

    return <p>Loading...</p>;
  }


  return (


    <div>


      <h2 className='Section_Title'>Projects </h2>
    <div className="ProjectsContainor">

      <div className="Projects">
        {repos.map((repo) => (
          <div key={repo.name}>
            <a className='Project_title' href={repo.url} target="_blank" rel="noopener noreferrer">{repo.name}</a>
            <hr></hr>
            <p>{repo.description}</p>
          </div>
          
        ))}
        </div>
        </div>
</div>
  );
}

export default Projects;
