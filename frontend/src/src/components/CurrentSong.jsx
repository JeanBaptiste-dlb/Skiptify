import React from "react";

export const CurrentSong = ({ songTitle, artist, albumCover }) => {
  return (
    <div>
      <img src={albumCover} alt="Cover" />
      {songTitle} from {artist}
    </div>
  );
};
