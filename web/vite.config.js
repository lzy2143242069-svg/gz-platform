import { defineConfig } from 'vite'

// uni-app 4.x 自动检测 src/ 目录下的 manifest.json
// 无需手动引入 vite-plugin-uni，CLI 已内置
export default defineConfig({
  // uni-app CLI 会自动注入插件
})
