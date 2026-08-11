# 贵州高校数据平台

> 贵州省高校信息可视化与专升本数据分析平台

## 功能

- 🗺️ 贵州省地图（ECharts）+ 高校/商圈/高铁站标记
- 🏫 院校列表（搜索、筛选、排序、分页）
- 📋 院校详情页（概况 / 专业 / 专升本数据）
- 📊 统计图表（柱状图、饼图）
- 📈 专升本历年分数线数据
- ⭐ 收藏功能
- 📱 响应式设计

## 技术栈

| 层 | 技术 |
|---|------|
| 后端 | SpringBoot 3.3 + MyBatis-Plus |
| 数据库 | H2（文件模式，重启不丢数据） |
| 前端 | 单 HTML + ECharts 5.5 |
| 数据采集 | Python 爬虫 + 高德地图 API |

## 项目结构

```
server/          ← SpringBoot 后端
├── src/main/java/com/gzplatform/   ← Java 代码
├── src/main/resources/
│   ├── static/index.html            ← 前端页面
│   ├── data.sql                     ← 院校数据（88所）
│   ├── score_data.sql               ← 专升本分数线
│   └── schema.sql                   ← 建表语句
└── pom.xml
crawler/         ← Python 数据采集脚本
web/             ← uni-app（未完成）
```

## 启动

```bash
# 需要 JDK 17+
cd server
./mvnw spring-boot:run
# 访问 http://localhost:8080
```

## API

| 接口 | 说明 |
|------|------|
| GET /api/university/list | 院校列表 |
| GET /api/university/detail?id= | 院校详情 |
| GET /api/major/list?universityId= | 专业列表 |
| GET /api/zsb/scores | 专升本分数线 |
| GET /api/zsb/plans | 专升本招生计划 |
| GET /api/statistics/* | 统计数据 |

## 数据

- 88 所贵州高校基本信息（名称、类型、城市、排名、经纬度）
- 专升本历年分数线（2020年6所院校54条记录）
- 2026年专升本招生计划

