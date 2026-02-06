import Noteform from "./components/Noteform";
import NotesList from "./components/Notelist";

function App(){
  return(
    <div style={{padding:"20px"}}>
      <h1>Notes App</h1>
      <p> FAstApi + MongoDB +React</p>
      <Noteform/>
      <NotesList/>
    </div>
  );
}

export default App;