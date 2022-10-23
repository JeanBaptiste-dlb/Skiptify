import "./App.css";
import { Headerbar } from "./components/Headbar";
import styled from "styled-components";
import { Songlists } from "./components/SongLists";
import { Footer } from "./components/Footer";
import React, { useState, useEffect } from "react";
import { exampleSongs } from "./dummyData/songs";
import { exampleCurrentSong } from "./dummyData/currentSong";
import axios from "axios";

const Wrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  background-color: #333;
`;

const Container = styled.div`
  max-width: 1200px;
  width: 100%;
  min-height: 100vh;
  padding: 2rem;
`;

function App() {
  const [threshold, setThreshold] = useState(70);
  const [currentSong, setCurrentSong] = useState(exampleCurrentSong);
  const [currentPlaylist, setCurrentPlaylist] = useState("Loading..."); // Heavy Metal & Rock
  const [queueSongs, setQueueSongs] = useState(exampleSongs);
  const [skippedSongs, setSkippedSongs] = useState(exampleSongs);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    loadData(true);
    let interval = setInterval(async () => {
      loadData();
    }, 2000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  const loadData = async (firstTime) => {
    const URL = `http://localhost:3000/test.json`;
    const URL_real = `http://127.0.0.1:5000/current_info`;
    //const res = await fetch(URL);
    const res = await axios.get(URL_real);
    const data = res?.data;
    console.log(data);
    if (firstTime) {
      setThreshold(data?.threshold);
    }
    setCurrentSong(data?.currentSong);
    setCurrentPlaylist(data?.currentPlaylistName);
    setQueueSongs(data?.queueSongs);
    setSkippedSongs(data?.skippedsongs);
    setLoaded(true);
  };

  return (
    <Wrapper>
      <Container>
        {loaded ? (
          <>
            <Headerbar threshold={threshold} setThreshold={setThreshold} />
            <Songlists
              threshold={threshold}
              queueSongs={queueSongs}
              skippedSongs={skippedSongs}
            />
            <Footer
              currentSong={currentSong}
              currentPlaylist={currentPlaylist}
            />
          </>
        ) : (
          <p>Loading...</p>
        )}
      </Container>
    </Wrapper>
  );
}

export default App;
