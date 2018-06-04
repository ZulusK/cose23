import React, { Component } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
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
    },
    link: {
        display: 'block',
        position: 'relative',
        color: theme.palette.primary.main,
        textDecoration: 'none',
        padding: '10px',
        float: 'right',

        '&:hover': {
            backgroundColor: theme.palette.primary.main,
            color: theme.palette.primary.contrastText
        }
    }
})

class UserViewPerTopic extends Component {
    constructor(props) {
        super(props)
        this.state = {
            desc: {}
        }
    }

    async loadDesc() {
        this.setState({
            desc: (await axios.get(`/user/${this.props.match.params.id}`, {
                params: {
                    topic_id: this.props.match.params.topicId
                }
            })).data
        })
    }

    componentDidMount() {
        this.loadDesc()
    }

    render() {
        let { desc } = this.state
        let { theme, classes } = this.props
        let { id, topicId } = this.props.match.params

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
                        <span>Number of messages: </span>
                        {desc.num_of_messages}
                    </h2>
                    <Link to={`/user/${id}`} className={classes.link} >
                        Show global data
                    </Link>
                </Paper>
                <Paper className={classes.plot}>
                    <h1 className={classes.h}>User`s activity</h1>
                    <ChartActivity userId={id} topicId={topicId} />
                </Paper>
            </div>
        );
    }
}

export default withTheme()(withStyles(styles)(UserViewPerTopic))