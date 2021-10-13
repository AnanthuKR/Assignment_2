import './App.css';
import {useEffect, useState} from 'react'
import TwCard from './components/TwCard'
import { Container } from 'semantic-ui-react';
import AddTweetsForm from './components/AddTweets';

function App() {

    const [tweets, setTweets] = useState([])

  useEffect(() => {

    fetch('tweets').then(response => {

      response.json().then(data => {

          setTweets(data)

        })

    })

}, []);


  return (
    <Container>

      <AddTweetsForm setTweets={setTweets}></AddTweetsForm>
    <div className="App">

      {tweets && tweets.map(tweet => {
        return <TwCard key={tweet.t_id} tweet={tweet}></TwCard>
  
      })}
      
    </div>
    </Container>
  );
}

export default App;
