import React from 'react'
import {Card, Icon, Image, Label } from 'semantic-ui-react'
import 'semantic-ui-css/semantic.min.css'
import moment from 'moment';


function TwCard({tweet}) {
    return(
            <div>
      <Card>
      <Card.Content>
        <Image
          floated='right'
          size='mini'
          src= {tweet.profile_url.toString()}
        />
        <Card.Header>{tweet.user_name}</Card.Header>
        <Card.Meta>{moment(tweet.createdAt).fromNow()}</Card.Meta>
        <Card.Description>
          {tweet.text}
        </Card.Description>
      </Card.Content>
      <Card.Content extra>
        <div className='ui two buttons'>
        <Label>
    <Icon name='like' color='red'/> {tweet.likes}
  </Label>
        </div>
      </Card.Content>
    </Card>  
</div>

    )  
    ;
}

export default TwCard;