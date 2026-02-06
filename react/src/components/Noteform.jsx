import {useState} from "react";
import { createNote } from "../services/api";

function Noteform(){
    const[title,setTitle]= useState("");
    const[content,setContent]=useState("");

    const handleSumbit= async(e)=>{
        e.preventDefault();

        const result= await createNote({title,content});
        alert("Note created with:"+ result.id);

        setTitle("");
        setContent("");
    };

    return(
        <form onSubmit={handleSumbit}>
            <input placeholder="Title" value={title} onChange={(e)=>setTitle(e.target.value)}/>
            <br/>
            <textarea placeholder="Content" value={content} onChange={(e)=>setContent(e.target.value)}/>
            <br/>
            <button type="sumbit">ADD</button>
        </form>
    )
}
export default Noteform;