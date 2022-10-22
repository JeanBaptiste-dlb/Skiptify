import React from "react";
import { Profile } from "./Profile";
import { Config } from "./Config";
import styled from "styled-components";
import { OnOneLine } from "./StyledComponents";
import { CurrentSong } from "./CurrentSong";
import { CurrentPlaylistname } from "./CurrentPlaylistname";

export const Footer = () => {
  return (
    <OnOneLine>
      <CurrentSong
        songTitle="Blabla"
        artist="Iron Maiden"
        albumCover="https://upload.wikimedia.org/wikipedia/en/7/7c/Iron_Maiden_%28album%29_cover.jpg"
      />
      <CurrentPlaylistname playlistname="Heavy Metal & Rock" />
    </OnOneLine>
  );
};
