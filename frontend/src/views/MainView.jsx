import React, { Component } from 'react'
import Chart from '../components/ChartTopTopics'
import { withStyles, withTheme } from 'material-ui/styles'
import Paper from 'material-ui/Paper'
import ChartActivity from '../components/ChartActivity.jsx'
import ChartTopTopics from '../components/ChartTopTopics.jsx'
import ChartTopUsers from '../components/ChartTopUsers.jsx'


const styles = (theme) => ({
    container: {
        width: '100%',
        position: 'relative',
    },
    element: {
        position: 'relative',
        width: '100%',
        marginBottom: '15px',
        padding: '15px',
        color: theme.palette.text.main
    },
    plot: {
        position: 'relative',
        width: '100%',
    }
})

class MainView extends Component {
    render() {
        let { theme, classes } = this.props

        return (
            <div className='container'>
                <Paper className={classes.element}>
                    <h1 style={{ marginBottom   : '15px' }}>Activity of users</h1>
                    <div className={classes.plot}>
                        <ChartActivity />
                    </div>
                </Paper>
                <Paper className={classes.element}>
                    <h1 style={{ marginBottom   : '15px' }}>Top 10 topics</h1>
                    <div className={classes.plot}>
                        <ChartTopTopics />
                    </div>
                </Paper>
                <Paper className={classes.element}>
                    <h1 style={{ marginBottom   : '15px' }}>Top 10 users</h1>
                    <div className={classes.plot}>
                        <ChartTopUsers />
                    </div>
                </Paper>
            </div>
        );
    }
}

export default withTheme()(withStyles(styles)(MainView))