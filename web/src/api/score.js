import { get } from './request'

export const getAdmissionScores = (params) => get('/api/score/admission', params)
export const getScoreTrend = (params) => get('/api/score/trend', params)
