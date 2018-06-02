import React, { Component } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import MainView from './views/MainView.jsx'
import TopicView from './views/TopicView.jsx'
import UserViewPerTopic from './views/user/UserViewPerTopic.jsx'
import UserViewGlobal from './views/user/UserViewGlobal.jsx'

export default class App extends Component{
    render() {
        return (
            <Router>
                <div>
                    <Route exact path='/' component={MainView}/>
                    <Route exact path='/topic/:id' component={TopicView}/>
                    <Route exact path='/user/:id' component={UserViewGlobal}/>
                    <Route exact path='/user/:id/:topicId' component={UserViewPerTopic}/>
                </div>
            </Router>
        );
    }
}