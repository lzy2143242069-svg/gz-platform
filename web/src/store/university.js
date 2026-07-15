import { defineStore } from 'pinia'
import { getUniversityList, getMapData } from '@/api/university'

export const useUniversityStore = defineStore('university', {
  state: () => ({
    list: [],
    total: 0,
    page: 1,
    size: 20,
    loading: false,
    filters: {
      type: '',
      city: '',
      nature: '',
      isZsbTarget: null,
    },
    mapData: [],
  }),

  actions: {
    async fetchList(reset = false) {
      if (reset) {
        this.page = 1
        this.list = []
      }
      this.loading = true
      try {
        const res = await getUniversityList({
          page: this.page,
          size: this.size,
          ...this.filters,
        })
        this.list = reset ? res.records : [...this.list, ...res.records]
        this.total = res.total
      } finally {
        this.loading = false
      }
    },

    async fetchMapData() {
      this.mapData = await getMapData()
    },

    setPage(page) {
      this.page = page
    },

    setFilters(filters) {
      this.filters = { ...this.filters, ...filters }
    },
  },
})
