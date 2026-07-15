import { get } from './request'

export const getOverview = () => get('/api/stats/overview')
export const getRanking = (params) => get('/api/stats/ranking', params)
export const getScoreDistribution = (params) => get('/api/stats/score-distribution', params)
