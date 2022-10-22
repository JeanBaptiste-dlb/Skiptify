import "./App.css";
import { Headerbar } from "./components/Headbar";
import styled from "styled-components";
import { Songlists } from "./components/SongLists";
import { Footer } from "./components/Footer";
import React, { useState } from "react";
import { exampleSongs } from "./dummyData/songs";
import { exampleCurrentSong } from "./dummyData/currentSong";

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

  return (
    <Wrapper>
      <Container>
        <Headerbar threshold={threshold} setThreshold={setThreshold} />
        <Songlists
          threshold={threshold}
          queueSongs={exampleSongs}
          skippedSongs={exampleSongs}
        />
        <Footer
          currentSong={exampleCurrentSong}
          currentPlaylist="Heavy Metal & Rock"
        />
      </Container>
    </Wrapper>
  );
}

export default App;
