<template>
  <view class="page">
    <!-- 顶部导航栏 -->
    <view class="nav-bar" :style="{ paddingTop: statusBarHeight + 'px' }">
      <view class="nav-content">
        <text class="nav-title">贵州高校数据平台</text>
      </view>
    </view>

    <!-- 搜索框 -->
    <view class="search-bar" @click="goSearch">
      <uni-icons type="search" size="18" color="#999" />
      <text class="search-placeholder">搜索高校名称、专业...</text>
    </view>

    <!-- 数据概览卡片 -->
    <view class="overview-cards">
      <view class="overview-item">
        <text class="overview-num">{{ overview.totalUniversities || '--' }}</text>
        <text class="overview-label">高校总数</text>
      </view>
      <view class="overview-item">
        <text class="overview-num accent">{{ overview.zsbUniversities || '--' }}</text>
        <text class="overview-label">专升本院校</text>
      </view>
      <view class="overview-item">
        <text class="overview-num">{{ overview.totalMajors || '--' }}</text>
        <text class="overview-label">专业数量</text>
      </view>
    </view>

    <!-- 快捷入口 -->
    <view class="quick-entry">
      <view class="entry-item" @click="goPage('/pages/zhuanshengben/index')">
        <view class="entry-icon zsb-icon">
          <uni-icons type="compose" size="24" color="#fff" />
        </view>
        <text class="entry-text">专升本专区</text>
      </view>
      <view class="entry-item" @click="goPage('/pages/score/query')">
        <view class="entry-icon score-icon">
          <uni-icons type="bars" size="24" color="#fff" />
        </view>
        <text class="entry-text">分数线查询</text>
      </view>
      <view class="entry-item" @click="goPage('/pages/compare/index')">
        <view class="entry-icon compare-icon">
          <uni-icons type="checkbox" size="24" color="#fff" />
        </view>
        <text class="entry-text">院校对比</text>
      </view>
      <view class="entry-item" @click="goPage('/pages/statistics/index')">
        <view class="entry-icon stats-icon">
          <uni-icons type="pie" size="24" color="#fff" />
        </view>
        <text class="entry-text">数据统计</text>
      </view>
    </view>

    <!-- 贵州地图区域（占位，后续接入 ECharts） -->
    <view class="card map-section">
      <text class="section-title">贵州省高校分布</text>
      <view class="map-placeholder">
        <text class="map-hint">地图加载中...</text>
        <text class="map-sub">将展示全省高校地理位置分布</text>
      </view>
    </view>

    <!-- 热门高校 -->
    <view class="card">
      <text class="section-title">热门高校</text>
      <view class="hot-list">
        <view
          class="hot-item"
          v-for="uni in hotUniversities"
          :key="uni.id"
          @click="goDetail(uni.id)"
        >
          <text class="hot-name">{{ uni.name }}</text>
          <text class="hot-tag" v-if="uni.isZsbTarget">可专升本</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const statusBarHeight = ref(44)
const overview = ref({
  totalUniversities: 0,
  zsbUniversities: 0,
  totalMajors: 0,
})
const hotUniversities = ref([])

onMounted(() => {
  const sysInfo = uni.getSystemInfoSync()
  statusBarHeight.value = sysInfo.statusBarHeight || 44
})

const goSearch = () => {
  uni.navigateTo({ url: '/pages/university/list?focus=true' })
}

const goPage = (url) => {
  if (url.includes('pages/zhuanshengben') || url.includes('pages/university') || url.includes('pages/mine')) {
    uni.switchTab({ url })
  } else {
    uni.navigateTo({ url })
  }
}

const goDetail = (id) => {
  uni.navigateTo({ url: `/pages/university/detail?id=${id}` })
}
</script>

<style lang="scss" scoped>
.page {
  min-height: 100vh;
  background: #f5f6fa;
}

.nav-bar {
  background: linear-gradient(135deg, #2B6CB0, #4A90D9);
  padding-bottom: 20rpx;
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 88rpx;
}

.nav-title {
  font-size: 36rpx;
  font-weight: bold;
  color: #fff;
}

.search-bar {
  display: flex;
  align-items: center;
  margin: 20rpx 24rpx;
  padding: 16rpx 24rpx;
  background: #fff;
  border-radius: 40rpx;
  box-shadow: 0 2rpx 12rpx rgba(0, 0, 0, 0.06);
}

.search-placeholder {
  margin-left: 12rpx;
  color: #999;
  font-size: 28rpx;
}

.overview-cards {
  display: flex;
  justify-content: space-around;
  margin: 20rpx 24rpx;
  padding: 30rpx 0;
  background: #fff;
  border-radius: 12rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.08);
}

.overview-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.overview-num {
  font-size: 44rpx;
  font-weight: bold;
  color: #2B6CB0;
}

.overview-num.accent {
  color: #FF6B35;
}

.overview-label {
  font-size: 24rpx;
  color: #999;
  margin-top: 8rpx;
}

.quick-entry {
  display: flex;
  justify-content: space-around;
  margin: 20rpx 24rpx;
  padding: 30rpx 0;
  background: #fff;
  border-radius: 12rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.08);
}

.entry-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.entry-icon {
  width: 80rpx;
  height: 80rpx;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.zsb-icon { background: #FF6B35; }
.score-icon { background: #2B6CB0; }
.compare-icon { background: #38A169; }
.stats-icon { background: #805AD5; }

.entry-text {
  font-size: 24rpx;
  color: #666;
  margin-top: 12rpx;
}

.card {
  margin: 20rpx 24rpx;
  padding: 24rpx;
  background: #fff;
  border-radius: 12rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.08);
}

.section-title {
  font-size: 32rpx;
  font-weight: bold;
  color: #333;
  margin-bottom: 20rpx;
}

.map-placeholder {
  height: 400rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #f0f4ff;
  border-radius: 8rpx;
}

.map-hint {
  font-size: 28rpx;
  color: #2B6CB0;
}

.map-sub {
  font-size: 24rpx;
  color: #999;
  margin-top: 8rpx;
}

.hot-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16rpx;
}

.hot-item {
  display: flex;
  align-items: center;
  padding: 12rpx 24rpx;
  background: #f5f6fa;
  border-radius: 8rpx;
}

.hot-name {
  font-size: 26rpx;
  color: #333;
}

.hot-tag {
  margin-left: 8rpx;
  font-size: 20rpx;
  color: #FF6B35;
  padding: 2rpx 8rpx;
  border: 1rpx solid #FF6B35;
  border-radius: 4rpx;
}
</style>
