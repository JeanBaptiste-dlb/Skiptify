import React from "react";
import styled from "styled-components";

const Container = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  text-align: right;
`;

const Text = styled.p`
  font-size: 1.2rem;
  padding: 0;
  margin: 0;
  display: block;
  width: 100%;
`;

const PlayListName = styled.p`
  font-size: 1.2rem;
  padding: 0;
  margin: 0;
  font-weight: 700;
  display: block;
  width: 100%;
`;

export const CurrentPlaylistname = ({ playlistname }) => {
  return (
    <Container>
      <Text>Listening to playlist</Text>
      <PlayListName>{playlistname}</PlayListName>
    </Container>
  );
};
