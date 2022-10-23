import React from "react";
import styled from "styled-components";
import { Album } from "./StyledComponents";

const Title = styled.h1`
  size: 3rem;
  line-height: 1;
  padding: 0;
  margin: 0;
  margin-top: 0.5rem;
  margin-bottom: 1rem;
`;

const Container = styled.div`
  width: 100%;
  margin: 2rem;
  padding: 1rem;
  background: ${(props) => (props.color ? props.color : "#eee")};
  border-radius: 2%;
`;

export const Songlist = ({
  title,
  color,
  songs,
  markProbability = false,
  threshold,
}) => {
  console.log(title);
  let willBeSkipped = false;
  if (songs) {
    willBeSkipped = songs.filter(
      (song) => song?.probability > threshold
    ).length;
  }
  return (
    <Container color={color}>
      <Title>{title}</Title>
      {markProbability ? (
        <p>{willBeSkipped} songs will be skipped by Skiptify.</p>
      ) : (
        <p>{songs && songs.length} songs were skipped by Skiptify.</p>
      )}
      <List>
        {songs &&
          songs.map((song) => (
            <Song
              markProbability={markProbability}
              threshold={threshold}
              title={song?.name}
              artist={song?.artist}
              probability={song?.probability}
              cover={song?.albumcover}
            />
          ))}
      </List>
    </Container>
  );
};

const Song = ({
  title,
  artist,
  probability,
  cover,
  threshold,
  markProbability,
}) => {
  const willBeSkipped = markProbability && threshold < probability;
  return (
    <SongContainer skip={willBeSkipped}>
      <Album m="0.5rem 0.25rem" src={cover} size={35} /> {title} | {artist}
      {willBeSkipped && <> | {probability} | will be skipped</>}
    </SongContainer>
  );
};

const SongContainer = styled.div`
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  background: ${(props) =>
    props.skip ? "rgba(232, 17, 91, 0.5)" : "transparent"};
  margin: 0.25rem 0;
`;

const List = styled.div`
  width: 100%;
  max-height: 250px;
  overflow: scroll;
  padding: 0.25rem;
  background: rgba(255, 255, 255, 0.07);
`;
