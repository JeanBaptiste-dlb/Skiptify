import "./App.css";
import { Headerbar } from "./components/Headbar";
import styled from "styled-components";
import { Songlists } from "./components/SongLists";
import { Footer } from "./components/Footer";

const Wrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  background-color: #333;
`;

const Container = styled.div`
  max-width: 1200px;
  width: 100%;
  height: 100vh;
  padding: 2rem;
`;

function App() {
  return (
    <Wrapper>
      <Container>
        <Headerbar />
        <Songlists />
        <Footer />
      </Container>
    </Wrapper>
  );
}

export default App;
