import React, { Component } from 'react'
import Chart from '../components/ChartTopTopics'
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
    }
})

class TopicView extends Component {
    render() {
        let { theme, classes } = this.props
        let { id } = this.props.match.params

        return (
            <div className={classes.container}>
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