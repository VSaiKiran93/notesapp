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
        let response =  await fetch(`/api/note/${noteId}/`)
        let data  = await response.json()
        setNote(data)

    }

    // Function (API call) to update the notes using async
    let updateNote = async () => {
        fetch(`/api/notes/${noteId}/update`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }

    // Arrow function to save the note if we back arrow is clicked
    let handleSubmit = () => {
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
    

            </div>

            {/* event to update the notes */}
            <textarea OnChange={(e) => {setNote({...note,  'body': e.target.value})}} defaultValue={note?.body}></textarea>
        </div>
    )
}

export default NotePage