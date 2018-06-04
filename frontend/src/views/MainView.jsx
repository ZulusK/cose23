import React, { Component } from 'react'
import Chart from '../components/ChartTopTopics'
import { withStyles, withTheme } from 'material-ui/styles';
import Paper from 'material-ui/Paper'
import ChartActivity from '../components/ChartActivity'
import ChartTopTopics from '../components/ChartTopTopics'
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
    smallPlot: {
        padding: '20px',
        width: '550px',
        margin: '10px'
    },
    h: {
        marginBottom: '20px'
    }
})

class MainView extends Component {
    render() {
        let { theme, classes } = this.props

        return (
            <div className={classes.container}>
                <Paper className={classes.smallPlot}>
                    <h1 className={classes.h}>Top 10 topics</h1>
                    <ChartTopTopics/>
                </Paper>
                <Paper className={classes.smallPlot}>
                    <h1 className={classes.h}>Top 10 users</h1>
                    <ChartTopUsers/>
                </Paper>
                <Paper className={classes.smallPlot}>
                    <h1 className={classes.h}>User`s activity</h1>
                    <ChartActivity/>
                </Paper>
            </div>
        );
    }
}

export default withTheme()(withStyles(styles)(MainView))