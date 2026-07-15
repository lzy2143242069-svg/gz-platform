import { get } from './request'

export const getZsbScores = (params) => get('/api/zsb/scores', params)
export const getZsbScoreTrend = (params) => get('/api/zsb/score-trend', params)
export const getZsbPlans = (params) => get('/api/zsb/plans', params)
export const getZsbCompare = (params) => get('/api/zsb/compare', params)
export const getZsbGuide = () => get('/api/zsb/guide')
