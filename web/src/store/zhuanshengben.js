import { defineStore } from 'pinia'
import { getZsbScores, getZsbPlans } from '@/api/zhuanshengben'

export const useZsbStore = defineStore('zhuanshengben', {
  state: () => ({
    scores: [],
    plans: [],
    scoreTotal: 0,
    planTotal: 0,
    loading: false,
    filters: {
      year: null,
      universityId: null,
      majorName: '',
      category: '',
    },
  }),

  actions: {
    async fetchScores(reset = false) {
      if (reset) this.scores = []
      this.loading = true
      try {
        const res = await getZsbScores(this.filters)
        this.scores = res.records || res
        this.scoreTotal = res.total || this.scores.length
      } finally {
        this.loading = false
      }
    },

    async fetchPlans(reset = false) {
      if (reset) this.plans = []
      this.loading = true
      try {
        const res = await getZsbPlans(this.filters)
        this.plans = res.records || res
        this.planTotal = res.total || this.plans.length
      } finally {
        this.loading = false
      }
    },

    setFilters(filters) {
      this.filters = { ...this.filters, ...filters }
    },
  },
})
