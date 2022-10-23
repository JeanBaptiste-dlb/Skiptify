import React, { useState } from "react";
import styled from "styled-components";
import { OnOneLine } from "./StyledComponents";
import Slider from "@mui/material/Slider";

export const Config = ({ threshold, setThreshold }) => {
  const handleChange = (e, newThreshold) => {
    setThreshold(newThreshold);
  };

  return (
    <OnOneLine>
      <ConfigLabel>Sensitivity</ConfigLabel>
      <SliderContainer>
        <Slider
          min={0}
          max={100}
          value={threshold}
          onChange={handleChange}
          valueLabelDisplay="on"
          width="100%"
        />
      </SliderContainer>
    </OnOneLine>
  );
};

const ConfigLabel = styled.p`
  padding: 0 1rem 0 1rem;
`;

const SliderContainer = styled.div`
  width: 150px;
`;
