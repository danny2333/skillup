import React, { useState } from 'react';
import axios from 'axios';

const DrillForm = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [videoUrl, setVideoUrl] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/drills/', { name, description, video_url: videoUrl })
      .then(response => {
        alert('Drill created successfully!');
        setName('');
        setDescription('');
        setVideoUrl('');
      })
      .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Description:</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Video URL:</label>
        <input
          type="url"
          value={videoUrl}
          onChange={(e) => setVideoUrl(e.target.value)}
          required
        />
      </div>
      <button type="submit">Create Drill</button>
    </form>
  );
};

export default DrillForm;