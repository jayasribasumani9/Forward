import {useState,useEffect} from "react";
import { getAllNotes } from "../services/api";


function NotesList(){
    const[notes,setNotes]= useState([]);
    
    useEffect(() => {
        const fetchNotes = async () => {
            const data = await getAllNotes();
            setNotes(data);
        };
        fetchNotes();
    }, []);

    return(
        <div>
            <h2>All notes</h2>
            {notes.length===0 && <p>No notes yet!</p>}
            {notes.map((note)=>(
                <div 
                key={note._id}
                style={{
                    border:"1px solid #f4c2c2",
                    margin:"10px 0",
                    padding:"10px",
                }}
                >
                    <h3>{note.title}</h3>
                    <p>{note.content}</p>
                    <small>{new Date(note.created_at).toLocaleString()}</small>
                </div>
            ))}
        </div>
    );
}

export default NotesList;