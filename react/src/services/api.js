const API_URL="http://127.0.0.1:8000";

export async function createNote(note){
    const res= await fetch(`${API_URL}/notes`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
        },
        body:JSON.stringify(note)
    });
    return res.json()
}

export async function getNote(id){
    const res= await fetch(`${API_URL}/notes/${id}`);
    return res.json();
}

export async function getAllNotes(){
    const res=await fetch(`${API_URL}/notes`);
    return res.json();
}