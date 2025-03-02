import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DrillList = () => {
  const [drills, setDrills] = useState([]);

  useEffect(() => {
    axios.get('/api/drills/')
      .then(response => setDrills(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Drills</h2>
      <ul>
        {drills.map(drill => (
          <li key={drill.id}>
            <h3>{drill.name}</h3>
            <p>{drill.description}</p>
            <a href={drill.video_url} target="_blank" rel="noopener noreferrer">Watch Video</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DrillList;