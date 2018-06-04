import React, { Component } from 'react'
import axios from 'axios'
import Paper from 'material-ui/Paper';
import { withStyles, withTheme } from 'material-ui/styles';
import ChartActivity from '../components/ChartActivity'
import ChartTopUsers from '../components/ChartTopUsers'

const styles = (theme) => ({
    container: {
        width: '100%',
        position: 'relative',
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'center',
        margin: '0 auto'
    },
    plot: {
        padding: '20px',
        width: '550px',
        margin: '10px'
    },
    h: {
        marginBottom: '20px'
    },
    desc: {
        width: '1120px',
        padding: '30px',
        margin: '10px',

        '& h2': {
            padding: '10px',
            fontWeight: 'normal',

            '& span': {
                fontWeight: 'bold'
            },
        }
    }
})

class TopicView extends Component {
    constructor(props){
        super(props)
        this.state = {
            desc: {}
        }
    }

    async loadDesc(){
        this.setState({
            desc: (await axios.get(`/topic/${this.props.match.params.id}`)).data
        })
    }

    componentDidMount(){
        this.loadDesc()
    }

    render() {
        let { desc } = this.state
        let { theme, classes } = this.props
        let { id } = this.props.match.params
        console.log(desc)

        return (
            <div className={classes.container}>
                <Paper className={classes.desc}>
                    <h2>
                        <span>Name: </span>
                        {desc.name}
                    </h2>
                    <h2>
                        <span>URL: </span>
                        <a href={desc.url}>{desc.url}</a>
                    </h2>
                    <h2>
                        <span>Number of messages: </span>
                        {desc.num_of_messages}
                    </h2>
                </Paper>
                <Paper className={classes.plot}>
                    <h1 className={classes.h}>Top 10 users</h1>
                    <ChartTopUsers topicId={id} />
                </Paper>
                <Paper className={classes.plot}>
                    <h1 className={classes.h}>User`s activity</h1>
                    <ChartActivity topicId={id} />
                </Paper>
            </div>
        );
    }
}

export default withTheme()(withStyles(styles)(TopicView))