<template>
  <view class="page">
    <view class="header">
      <text class="title">专升本专区</text>
      <text class="subtitle">贵州专升本数据一站式查询</text>
    </view>

    <view class="quick-entry">
      <view class="entry-card" @click="goPage('/pages/zhuanshengben/score-query')">
        <text class="entry-title">分数线查询</text>
        <text class="entry-desc">历年各校各专业分数线</text>
      </view>
      <view class="entry-card" @click="goPage('/pages/zhuanshengben/plan-list')">
        <text class="entry-title">招生计划</text>
        <text class="entry-desc">各年度招生人数与要求</text>
      </view>
      <view class="entry-card" @click="goPage('/pages/zhuanshengben/comparison')">
        <text class="entry-title">院校对比</text>
        <text class="entry-desc">多维度对比分析</text>
      </view>
      <view class="entry-card" @click="goPage('/pages/zhuanshengben/guide')">
        <text class="entry-title">报考指南</text>
        <text class="entry-desc">政策解读与经验分享</text>
      </view>
    </view>
  </view>
</template>

<script setup>
const goPage = (url) => {
  uni.navigateTo({ url })
}
</script>

<style lang="scss" scoped>
.page {
  min-height: 100vh;
  background: #f5f6fa;
}

.header {
  background: linear-gradient(135deg, #FF6B35, #FF8F65);
  padding: 40rpx 30rpx;
  color: #fff;
}

.title {
  font-size: 40rpx;
  font-weight: bold;
}

.subtitle {
  font-size: 26rpx;
  opacity: 0.9;
  margin-top: 8rpx;
}

.quick-entry {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20rpx;
  padding: 24rpx;
}

.entry-card {
  background: #fff;
  border-radius: 12rpx;
  padding: 30rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.08);
}

.entry-title {
  font-size: 30rpx;
  font-weight: bold;
  color: #333;
}

.entry-desc {
  font-size: 24rpx;
  color: #999;
  margin-top: 8rpx;
}
</style>
