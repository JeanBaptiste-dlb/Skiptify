import React from "react";
import styled from "styled-components";
import { OnOneLine } from "./StyledComponents";

const Username = styled.p`
  line-height: 1;
  font-weight: 700;
  font-size: 1.2rem;
`;

const Avatar = styled.img`
  width: ${(props) => (props.size ? props.size + "px" : "30px")};
  height: ${(props) => (props.size ? props.size + "px" : "30px")};
  margin: 1rem;
  border-radius: 50%;
`;

const OnOneLineExtended = styled(OnOneLine)`
  justify-content: right;
`;

export const Profile = ({ name, profilePicture }) => {
  return (
    <OnOneLineExtended>
      <Username>{name}</Username>
      <Avatar src={profilePicture} size={50} />
    </OnOneLineExtended>
  );
};
