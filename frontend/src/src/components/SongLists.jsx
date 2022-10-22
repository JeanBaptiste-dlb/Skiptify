import React from "react";
import { Songlist } from "./SongList";
import { OnOneLine } from "./StyledComponents";
import styled from "styled-components";

const OnOneLineAligned = styled(OnOneLine)`
  align-items: strech;
`;

export const Songlists = ({ threshold, queueSongs, skippedSongs }) => {
  return (
    <OnOneLineAligned>
      <Songlist
        title="Skipped Songs"
        list={null}
        color="#E8115B"
        songs={skippedSongs}
      />
      <Songlist
        title="Queue"
        list={null}
        color="#608108"
        markProbability={true}
        threshold={threshold}
        songs={queueSongs}
      />
    </OnOneLineAligned>
  );
};
