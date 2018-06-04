import React from 'react'
import axios from 'axios'
import { ResponsiveContainer, LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts'
import CircularProgress from 'material-ui/Progress/CircularProgress';
import { withStyles, withTheme } from 'material-ui/styles';

const styles = () => ({
    progressContainer: {
        width: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center'
    }
})

class ChartActivity extends React.Component {
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
        let { userId, topicId } = this.props
        let params = {}
        if (userId != undefined) params['user_id'] = userId
        if (topicId != undefined) params['topic_id'] = topicId
        let { data } = (await axios.get('/comments/timestamp', { params }))
        data = await (rebaseData(data))
        this.setState({
            data
        })
    }

    render() {
        if (this.state.data == undefined) return (
            <div className={this.props.classes.progressContainer}>
                <CircularProgress />
            </div>
        )

        return (
            <ResponsiveContainer width='100%' aspect={4.0/2.0}>
                <LineChart data={this.state.data}>
                    <CartesianGrid />
                    <XAxis dataKey='date' />
                    <YAxis />
                    <Line dataKey='count' fill={this.props.theme.palette.primary.main} />
                    <Tooltip/>
                </LineChart>
            </ResponsiveContainer>
        );
    }
}

async function rebaseData(data) {
    let r = []

    let getValue = undefined
    let getStr = undefined
    if (getYear(data[0].date) !== getYear(data[data.length - 1].date)) {
        getValue = getYear
        getStr = getStrYear
    }
    else if (getMonth(data[0].date) !== getMonth(data[data.length - 1].date)) {
        getValue = getMonth
        getStr = getStrMonthAndYear
    }
    if (getValue === undefined) return data

    let currValue = getValue(data[0].date)
    let sum = data[0].count

    for (let i = 1; i < data.length; i++) {
        if (getValue(data[i].date) !== currValue) {
            r.push({
                date: getStr(data[i-1].date),
                count: sum
            })
            currValue = getValue(data[i].date)
            sum = data[i].count
        } else {
            sum += data[i].count
        }
    }
    r.push({
        date: getStr(data[data.length - 1].date),
        count: sum
    })

    return r
}

function getYear(str) {
    return parseInt(str.split('.')[2])
}

function getMonth(str) {
    return parseInt(str.split('.')[1])
}

function getStrYear(str) {
    return getYear(str) + ''
}

function getStrMonthAndYear(str) {
    return str.slice(str.indexOf('.') + 1) + ''
}

export default withTheme()(withStyles(styles)(ChartActivity))