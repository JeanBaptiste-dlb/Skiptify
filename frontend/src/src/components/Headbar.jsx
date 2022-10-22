import React from "react";
import { Profile } from "./Profile";
import { Config } from "./Config";
import styled from "styled-components";
import { OnOneLine } from "./StyledComponents";

export const Headerbar = () => {
  return (
    <OnOneLine>
      System Online
      <Config />
      <Profile />
    </OnOneLine>
  );
};
