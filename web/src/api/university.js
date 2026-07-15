import { get } from './request'

export const getUniversityList = (params) => get('/api/university/list', params)
export const getUniversityDetail = (id) => get(`/api/university/${id}`)
export const searchUniversity = (keyword) => get('/api/university/search', { keyword })
export const getMapData = () => get('/api/university/map-data')
