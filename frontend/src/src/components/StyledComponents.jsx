import React from "react";
import styled from "styled-components";

export const OnOneLine = styled.div`
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 1;
`;

export const Album = styled.img`
  width: ${(props) => (props.size ? props.size + "px" : "30px")};
  height: ${(props) => (props.size ? props.size + "px" : "30px")};
  margin: ${(props) => (props.m ? props.m : "1rem")};
`;

export const Circle = styled.span`
  width: ${(props) => (props.size ? props.size + "px" : "30px")};
  height: ${(props) => (props.size ? props.size + "px" : "30px")};
  background-color: ${(props) => (props.bg ? props.bg : "#bbb")};
  border-radius: 50%;
  display: inline-block;
`;
