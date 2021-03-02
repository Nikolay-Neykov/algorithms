import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import { decode } from 'he';

export default function Game() {
  const [joke, setJoke] = useState('');

  const fetchJoke = async (signal: AbortSignal) => {
    const response = await fetch('https://api.icndb.com/jokes/random', { signal });
    const { value } = await response.json();

    setJoke(decode(value.joke));
  };

  useEffect(() => {
    if (!joke) {
      const controller = new AbortController();
      fetchJoke(controller.signal);

      return () => controller.abort();
    }
  }, [joke]);

  return (
    <div>
      <p>{joke || '...'}</p>
      <Button className="App-link" onClick={() => setJoke('')}>Get a new joke</Button>
    </div >
  );

}