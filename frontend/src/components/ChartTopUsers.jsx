import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import { ResponsiveContainer, BarChart, Bar, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts'
import CircularProgress from 'material-ui/Progress/CircularProgress';
import { withStyles, withTheme } from 'material-ui/styles';

const styles = (theme) => ({
    container: {
        width: '100%',
        position: 'relative',
        display: 'flex',
        justifyContent: 'center'
    },
    plot: {
        width: '60%',
        minWidth: '355px',
        marginLeft: '0',
        position: 'relative',
        height: '100%',
        marginRight: '20px'
    },
    links: {
        position: 'relative',
        flex: '1',
        minWidth: '50px'
    },
    link: {
        width: '100%',
        padding: '5px',
        display: 'block',
        color: theme.palette.text.primary,
        'text-decoration': 'none',
        overflow: 'hidden',
        textOverflow: 'ellipsis',
        whiteSpace: 'nowrap',
        '&:hover': {
            color: theme.palette.primary.contrastText,
            backgroundColor: theme.palette.primary.main
        }
    }
})

class ChartTopUsers extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            data: undefined
        }
    }

    componentDidMount() {
        this.loadData()
    }

    async loadData() {
        let { topicId } = this.props
        let params = {}
        if (topicId != undefined) params['topic_id'] = topicId
        let { data } = (await axios.get('/comments/top/users', { params }))
        data = data.slice(0, 10)
        this.setState({
            data
        })
    }

    render() {
        let { classes, topicId, theme } = this.props

        if (this.state.data === undefined) return (
            <div className={classes.container}>
                <CircularProgress />
            </div>
        )

        let links = this.state.data.map(value => (
            <Link
                to={`/user/${value.user_id}${topicId === undefined ? '' : '/' + topicId}`}
                key={value.user_id}
                className={classes.link}
            >
                {value.user_name}
            </Link>
        ))

        return (
            <div className={classes.container}>
                <div className={classes.plot}>
                    <ResponsiveContainer width='100%' aspect={4.0 / 3.0}>
                        <BarChart data={this.state.data}>
                            <CartesianGrid />
                            <XAxis dataKey='user_name' hide={true} />
                            <YAxis />
                            <Bar dataKey='count' fill={theme.palette.primary.main} />
                            <Tooltip />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
                <div className={classes.links}>{links}</div>
            </div>
        );
    }
}

export default withTheme()(withStyles(styles)(ChartTopUsers))