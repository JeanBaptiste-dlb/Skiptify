import React from "react";
import { Profile } from "./Profile";
import { Config } from "./Config";
import styled from "styled-components";
import { OnOneLine } from "./StyledComponents";
import { CurrentSong } from "./CurrentSong";
import { CurrentPlaylistname } from "./CurrentPlaylistname";

export const Footer = ({ currentSong, currentPlaylist }) => {
  return (
    <OnOneLine>
      <CurrentSong
        songTitle={currentSong?.song}
        artist={currentSong?.artist}
        albumCover={currentSong?.albumcover}
      />
      <CurrentPlaylistname playlistname={currentPlaylist} />
    </OnOneLine>
  );
};
