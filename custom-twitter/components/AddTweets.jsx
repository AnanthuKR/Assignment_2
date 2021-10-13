import React, { useState } from 'react';
import { Button, Form, TextArea } from 'semantic-ui-react';


function AddTweetsForm({setTweets}) {

const [newTweet, setNewTweet] = useState({'text':""})

const change = (e) => {

    e.preventDefault()

        setNewTweet({"text":e.target.value})
        console.log(newTweet)

}

const sendTweet = () => {

    fetch(`/addtweets/${newTweet.text}`).then(response => {

        response.json().then(data => {
  
            setTweets(data)
            
            
          })
  
      })
      setNewTweet({"text":""})

}


    return ( 
        <Form onSubmit={sendTweet}>
        <Form.Field
          id='form-textarea-control-opinion'
          control={TextArea}
          name="tweet"
          placeholder='Write...'
          value={newTweet['text']}
          onChange={change}
        />
        <Form.Field
          id='form-button-control-public'
          control={Button}
          content='Confirm'
          
        />
      </Form>

     );
}

export default AddTweetsForm;

