import React, { Component } from 'react'
import axios from 'axios'
import Paper from 'material-ui/Paper';
import { withStyles, withTheme } from 'material-ui/styles';
import ChartActivity from '../../components/ChartActivity'
import ChartTopTopics from '../../components/ChartTopTopics'

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

class UserViewGlobal extends Component {
    constructor(props){
        super(props)
        this.state = {
            desc: {}
        }
    }

    async loadDesc(){
        this.setState({
            desc: (await axios.get(`/user/${this.props.match.params.id}`)).data
        })
    }

    componentDidMount(){
        this.loadDesc()
    }

    render() {
        let { desc } = this.state
        let { theme, classes } = this.props
        let { id } = this.props.match.params

        return (
            <div className={classes.container}>
                <Paper className={classes.desc}>
                    <h2>
                        <span>Name: </span>
                        {desc.name}
                    </h2>
                    <h2>
                        <span>ID from forum: </span>
                        {desc.id_from_forum}
                    </h2>
                    <h2>
                        <span>Number of topics: </span>
                        {desc.num_of_topics}
                    </h2>
                    <h2>
                        <span>Number of messages: </span>
                        {desc.num_of_messages}
                    </h2>
                </Paper>
                <Paper className={classes.plot}>
                    <h1 className={classes.h}>Top of topics</h1>
                    <ChartTopTopics userId={id} />
                </Paper>
                <Paper className={classes.plot}>
                    <h1 className={classes.h}>User`s activity</h1>
                    <ChartActivity userId={id} />
                </Paper>
            </div>
        );
    }
}

export default withTheme()(withStyles(styles)(UserViewGlobal))