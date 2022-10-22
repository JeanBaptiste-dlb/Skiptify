import React from "react";
import styled from "styled-components";
import { Songlist } from "./SongList";
import { OnOneLine } from "./StyledComponents";

export const Songlists = () => {
  return (
    <OnOneLine>
      <Songlist title="Skipped Songs" list={null} color="#E8115B" />
      <Songlist title="Queue" list={null} color="#608108" />
    </OnOneLine>
  );
};
