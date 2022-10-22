import React from "react";
import styled from "styled-components";
import { Album } from "./StyledComponents";

const SongContainer = styled.div`
  display: flex;
  flex-wrap: nowrap;
  width: 100%;
`;
const SongInfo = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
`;

const SongTitle = styled.h2`
  font-size: 2rem;
  line-height: 2rem;
  margin: 0;
  padding: 0;
  margin-top: 1rem;
`;

const Artist = styled.p`
  font-size: 1.2rem;
  padding: 0;
  margin: 0;
  margin-top: 0.75rem;
`;

export const CurrentSong = ({ songTitle, artist, albumCover }) => {
  return (
    <SongContainer>
      <Album src={albumCover} size={125} alt="Cover" />
      <SongInfo>
        <SongTitle>{songTitle}</SongTitle>
        <Artist>{artist}</Artist>
      </SongInfo>
    </SongContainer>
  );
};
