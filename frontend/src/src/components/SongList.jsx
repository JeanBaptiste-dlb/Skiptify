import React from "react";
import styled from "styled-components";

const Title = styled.h1`
  size: 3rem;
`;

const Container = styled.div`
  width: 100%;
  margin: 2rem;
  padding: 1rem;
  background: ${(props) => (props.color ? props.color : "#eee")};
`;

export const Songlist = ({ title, color }) => {
  console.log(title);
  return (
    <Container color={color}>
      <Title>{title}</Title>
    </Container>
  );
};
