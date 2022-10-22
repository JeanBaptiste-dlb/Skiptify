import React from "react";
import styled from "styled-components";

const LogoImage = styled.img`
  width: ${(props) => (props.size ? props.size * 1.57 + "px" : "30px")};
  height: ${(props) => (props.size ? props.size + "px" : "30px")};
  margin: ${(props) => (props.m ? props.m : "1rem")};
`;

export const Logo = () => (
  <LogoImage size={50} src="https://m.exodia.ch/skiptify-logo.png" />
);
