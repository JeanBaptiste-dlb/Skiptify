import React from "react";
import { Profile } from "./Profile";
import { Config } from "./Config";
import styled from "styled-components";
import { Circle, OnOneLine } from "./StyledComponents";
import { Logo } from "./Logo";

export const Headerbar = ({ setThreshold, threshold }) => {
  const systemStatus = 1; // 1 = online
  return (
    <OnOneLine>
      <Logo />
      {/*
      <SystemText>
        <Circle size={15} bg={systemStatus ? "#1ED760" : "#E8115B"} /> System{" "}
        {systemStatus ? "online" : "offline"}
      </SystemText>
      */}
      <Config setThreshold={setThreshold} threshold={threshold} />
      <Profile
        name="Headbanger"
        profilePicture="https://m.exodia.ch/profile.jpg"
      />
    </OnOneLine>
  );
};

const SystemText = styled.p`
  line-height: 1;
  font-size: 1rem;
`;
