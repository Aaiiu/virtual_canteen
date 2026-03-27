# Virtual Canteen Simulation System
# 虚拟食堂仿真系统

## 项目简介

这是一个食堂排队模拟与可视化系统，旨在帮助学生：
- 预测不同时间段的排队等待时间
- 可视化展示食堂实时状态（含窗口菜系、排队人数、座位占用）
- 智能推荐最佳就餐时间
- 辅助快速找到空闲座位
- 模拟不同行为特性的学生群体（特性词条系统）
- 对比两种排队策略的效率差异

## 技术栈

- **后端**: Python 3.8+ / Flask
- **前端**: HTML5 / CSS3 / JavaScript / Bootstrap
- **数据库**: SQLite / Flask-SQLAlchemy
- **模拟引擎**: 自定义队列模拟（SimPy可选）
- **可视化**: Canvas API / Chart.js

## 项目框架说明

### 整体架构
本项目采用前后端分离架构，后端提供RESTful API，前端通过AJAX调用获取数据并进行可视化展示。

### 目录结构与功能说明

    Virtual_Canteen/
    src/
      app.py                   Flask应用主入口（启动服务器、注册路由）
      models/                  数据模型层（负责人：成员A）
        database.py            数据库连接配置
        window.py              窗口模型（编号、菜系名称、服务时间）
        queue.py               队列模型（排队人数、等待时间）
        seat.py                座位模型（座位编号、占用状态、就餐学生ID）
        student.py             学生模型（姓名、菜品偏好、速度系数）
        trait.py               特性词条模型（词条名称、触发概率、效果参数）
      simulation/              模拟引擎层（负责人：成员B）
        student_generator.py   学生生成器（随机生成学生及特性词条分配）
        queue_simulator.py     排队模拟算法（多窗口、偏好匹配、智能切换）
        seat_manager.py        座位管理（分配、释放、孤独症专属逻辑）
        time_analysis.py       时间段分析（统计各时段等待时间、标注高峰）
        comparison.py          对比模拟（策略A偏好 vs 策略B最短等待）
        recommendation.py      最佳时间推荐（基于等待时间+座位+偏好）
      routes/                  API路由层（负责人：成员A）
        api.py                 所有API接口
      static/                  静态资源（负责人：成员C）
        css/style.css          主样式表
        js/main.js             主逻辑（前后端交互、定时刷新）
        js/visualization.js    2D可视化（Canvas绘制食堂平面图）
        js/tooltip.js          悬停浮窗（学生信息、特性词条、剩余时间）
        js/charts.js           统计图表（折线图、柱状图、饼图）
        js/comparison.js       对比模拟面板（策略A vs 策略B）
        images/
      templates/               HTML模板（负责人：成员C）
        index.html             主页（2D可视化+实时数据）
        analysis.html          分析页（时间段图表+推荐）
        comparison.html        对比页（模拟对比结果）
    config/
      config.py                全局配置（数据库路径、食堂参数、特性词条库、超参数）
    data/
      canteen.db               SQLite数据库（运行时生成）
      test_data/               测试数据
    docs/
      需求文档.md
      API文档.md
      软件开发环境搭建说明.md
    tests/
      unit/                    单元测试
      integration/             集成测试
    scripts/
      init_database.py         数据库初始化脚本（建表+插入测试数据）
    requirements.txt
    README.md
    TODO.md
    ProjectInfo.md
    项目规划.md

### 核心功能模块详解

#### 1. 数据模型层（models/）
**负责人：成员A**
- **窗口管理**：每个窗口有编号、菜系名称（天津菜/湘菜/汉堡快餐等）、服务时间
- **学生模型**：每个学生有菜品偏好、个体速度系数（影响就餐时长）
- **特性词条**：存储各词条的触发概率和效果参数
- **座位管理**：记录每个座位的占用状态和当前就餐学生

#### 2. 模拟引擎层（simulation/）
**负责人：成员B**
- **学生生成**：按到达率生成学生，按概率随机分配特性词条（0至多个）
- **特性词条库**（在 config.py 中定义）：
  - 选择恐惧症：打饭时间+50%
  - 急性子：强制选择等待时间最短窗口
  - 社恐：优先选择排队人数最少的窗口
  - 孤独症：只坐没有人坐过的座位
- **排队决策**：学生优先去偏好菜系窗口；等待超过阈值后切换至最短等待窗口
- **就餐时间**：基础时间（按菜系）× 个体速度系数，词条可进一步修正
- **对比模拟**：同一批学生分别用策略A（偏好优先）和策略B（最短等待）运行，输出对比数据

#### 3. API接口层（routes/）
**负责人：成员A**
- 食堂状态、各窗口排队信息、座位占用情况
- 模拟触发与进度查询
- 时间段分析数据、最佳时间推荐
- 对比模拟结果

#### 4. 前端展示层（static/ + templates/）
**负责人：成员C**
- **2D可视化**：Canvas绘制食堂平面图，显示各菜系窗口排队和座位状态
- **悬停浮窗**：鼠标悬停已占用座位时，弹出浮窗显示学生姓名、学号、菜品偏好、特性词条、剩余就餐时间
- **数据图表**：Chart.js展示各时段等待时间趋势、人流量分布、特性人群占比
- **对比面板**：并排展示策略A和策略B的等待/就餐/总耗时对比

### 新增功能架构对照表

| 新功能 | 所在文件 | 开发阶段 | 负责人 |
|--------|----------|----------|--------|
| 窗口菜系设置 | models/window.py + config/config.py | 第3-4周 | 成员A |
| 学生菜品偏好 | models/student.py | 第3-4周 | 成员B |
| 特性词条系统 | models/trait.py + config/config.py + simulation/student_generator.py | 第3-4周 | 成员B |
| 智能排队决策 | simulation/queue_simulator.py | 第4-5周 | 成员B |
| 就餐时间系数 | simulation/seat_manager.py | 第4-5周 | 成员A+B |
| 悬停浮窗 | static/js/tooltip.js | 第4-5周 | 成员C |
| 模拟对比功能 | simulation/comparison.py + static/js/comparison.js | 第6-8周 | 成员B+C |

### 开发顺序（按工程依赖）

1. 【4】数据库模块 → 所有功能的基础
2. 【5】后端API框架 + 【6】学生属性与特性词条系统 → 并行开发
3. 【7】排队模拟算法 → 依赖【6】
4. 【8】就餐时间与座位系统 → 依赖【6】【7】
5. 【9】前端基础框架 + 【10】2D可视化 → 可与【7】并行
6. 【11】前后端联调 → 整合所有模块
7. 【12】模拟对比 + 【13】时间段分析 → 依赖【11】
8. 【14】图表 + 【15】推荐 + 【16】UI优化 → 依赖【13】

详细任务清单见 TODO.md

## 团队成员

- 成员A: 后端开发 + 数据库设计
- 成员B: 排队模拟算法 + 特性词条系统
- 成员C: 前端可视化 + UI设计

## 快速开始

### 1. 克隆项目

    git clone https://github.com/your-team/Virtual_Canteen.git
    cd Virtual_Canteen

### 2. 安装依赖

    pip install -r requirements.txt

### 3. 初始化数据库

    python scripts/init_database.py

### 4. 运行项目

    cd src
    python app.py

### 5. 访问系统
打开浏览器访问: http://localhost:5000

## 核心功能

### 已完成
- [x] 项目初始化
- [x] 基础目录结构搭建
- [x] 开发环境搭建说明文档

### 开发中（第3-5周）
- [ ] 数据库模块（窗口、学生、特性词条、座位表）
- [ ] 学生属性与特性词条系统
- [ ] 排队模拟算法（含智能排队决策）
- [ ] 就餐时间与座位系统
- [ ] 2D可视化界面（含悬停浮窗）

### 计划中（第6-8周）
- [ ] 模拟对比功能（策略A vs 策略B）
- [ ] 时间段分析功能
- [ ] 数据可视化图表
- [ ] 最佳时间推荐
- [ ] UI优化

### 可选（时间充裕时）
- [ ] 3D可视化升级
- [ ] 特性词条扩展
- [ ] 数据导出功能

## 开发规范

### Git提交规范

    feat: 新增功能
    fix: 修复bug
    docs: 文档更新
    style: 代码格式
    refactor: 代码重构
    test: 测试相关

### 分支管理
- main: 稳定版本
- dev: 开发分支
- feature/*: 功能分支

## 文档

- 项目规划.md - 完整的项目规划文档
- ProjectInfo.md - 开发日志记录
- TODO.md - 任务清单（含完整开发顺序）
- docs/API文档.md - 接口文档
- docs/需求文档.md - 需求说明
- docs/软件开发环境搭建说明.md - 环境配置指南

## 学习资源

- Python教程: https://www.runoob.com/python3/python3-tutorial.html
- Flask文档: https://dormousehole.readthedocs.io/
- Git教程: https://www.liaoxuefeng.com/wiki/896043488029600

## 许可证

本项目仅用于课程学习和演示。

---

**开发周期**: 2026年3月 - 2026年6月
**最后更新**: 2026-03-17