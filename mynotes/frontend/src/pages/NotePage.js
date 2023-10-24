import React, {useState, useEffect} from 'react'  
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'   
import { Link } from 'react-router-dom'      

const NotePage = ({ match, history }) => {

    let noteId = match.params.id
    let[note, setNote] = useState(null)    
    
    useEffect(() => {
        getNote()

    }, [noteId])

    //Funtion (API call) to get the single note from the database
    let getNote = async () => {
        if (noteId === 'new') return

        let response =  await fetch(`/api/note/${noteId}/`)
        let data  = await response.json()
        setNote(data)

    }

    //API call for createNote
    let createNote = async () => {
        fetch(`/api/notes/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }

    // Function (API call) to update the notes using async
    let updateNote = async () => {
        fetch(`/api/notes/${noteId}/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }

    // API call function to delete the note
    let deleteNote = async () => {
        fetch(`/api/notes/${noteId}/`, {
            method: 'DELETE',
            'headers': {
                'Content-Type' : 'application/json'
            }
        })
        history.push('/')
    }


    // Arrow function to save the note if we back arrow is clicked
    let handleSubmit = () => {
        console.log('NOTE:', note)
        if(noteId !== 'new' && !note.body === '') {
            console.log('Delete method Triggered')
            deleteNote()
        } 
        else if(noteId !== 'new') {
            updateNote()
        }
        else if(noteId === 'new' &&  note !== null){
            createNote()
        }
        updateNote()
        history.push('/')
    }

    // error handling if there is no note body
    return (
        <div className='note'>
            <div className='note-header'>
                <h3>
                    <Link>
                        <ArrowLeft onClick={handleSubmit}/>  
                    </Link>
                </h3>

                {/*Condition for delete button in new notes */}
                {noteId !== 'new' ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )}

            </div>

            {/* event to update the notes */}
            <textarea OnChange={(e) => {setNote({...note,  'body': e.target.value})}} defaultValue={note?.body}></textarea>
        </div>
    )
}

export default NotePage