# Virtual Canteen Simulation System
# 虚拟食堂仿真系统

## 项目简介

这是一个食堂排队模拟与可视化系统，旨在帮助学生：
- 🕐 预测不同时间段的排队等待时间
- 👀 可视化展示食堂实时状态
- 💡 智能推荐最佳就餐时间
- 🪑 辅助快速找到空闲座位

## 技术栈

- **后端**: Python 3.8+ / Flask
- **前端**: HTML5 / CSS3 / JavaScript / Bootstrap
- **数据库**: SQLite
- **模拟引擎**: SimPy / 自定义队列模拟
- **可视化**: Canvas API / Chart.js

## 项目框架说明

### 整体架构
本项目采用前后端分离架构，后端提供RESTful API，前端通过AJAX调用获取数据并进行可视化展示。

### 目录结构与功能说明

```
Virtual_Canteen/
├── src/                          # 源代码目录
│   ├── app.py                   # Flask应用主入口
│   │   └── 功能：启动Web服务器，注册路由
│   │
│   ├── models/                  # 数据模型层（负责人：成员A）
│   │   ├── __init__.py         # 模块初始化
│   │   ├── database.py         # 数据库连接配置
│   │   ├── window.py           # 窗口模型（窗口编号、服务时间等）
│   │   ├── queue.py            # 队列模型（排队人数、等待时间等）
│   │   └── seat.py             # 座位模型（座位编号、占用状态等）
│   │   └── 功能：定义数据库表结构，提供数据CRUD操作
│   │
│   ├── simulation/              # 模拟引擎层（负责人：成员B）
│   │   ├── __init__.py         # 模块初始化
│   │   ├── queue_simulator.py  # 排队模拟算法
│   │   │   └── 功能：实现单/多窗口排队模拟、时间推进、等待时间计算
│   │   ├── time_analysis.py    # 时间段分析
│   │   │   └── 功能：统计各时段平均等待时间、标注高峰时段
│   │   └── recommendation.py   # 最佳时间推荐
│   │       └── 功能：基于等待时间和座位情况推荐最佳就餐时间
│   │
│   ├── routes/                  # API路由层（负责人：成员A）
│   │   ├── __init__.py         # 模块初始化
│   │   └── api.py              # API接口定义
│   │       └── 功能：提供获取食堂状态、排队信息、座位信息等接口
│   │
│   ├── static/                  # 静态资源（负责人：成员C）
│   │   ├── css/                # 样式文件
│   │   │   └── style.css       # 主样式表
│   │   ├── js/                 # JavaScript文件
│   │   │   ├── main.js         # 主逻辑（前后端交互、实时更新）
│   │   │   ├── visualization.js # 2D可视化（Canvas绘制食堂平面图）
│   │   │   └── charts.js       # 数据图表（Chart.js生成统计图表）
│   │   └── images/             # 图片资源
│   │
│   └── templates/               # HTML模板（负责人：成员C）
│       └── index.html          # 主页面
│           └── 功能：展示食堂可视化界面、排队信息、座位状态
│
├── data/                        # 数据文件目录
│   ├── canteen.db              # SQLite数据库文件（运行时生成）
│   └── test_data/              # 测试数据
│
├── docs/                        # 项目文档目录
│   ├── 需求文档.md             # 详细需求说明
│   └── API文档.md              # 接口文档
│
├── tests/                       # 测试文件目录
│   ├── unit/                   # 单元测试
│   └── integration/            # 集成测试
│
├── config/                      # 配置文件目录
│   └── config.py               # 项目配置（数据库路径、模拟参数等）
│
├── scripts/                     # 工具脚本目录
│   └── init_database.py        # 数据库初始化脚本（负责人：成员A）
│       └── 功能：创建数据库表、插入测试数据
│
├── requirements.txt             # Python依赖包列表
├── README.md                    # 项目说明文档
├── TODO.md                      # 任务清单
├── ProjectInfo.md               # 项目日志
└── 项目规划.md                  # 完整项目规划
```

### 核心功能模块详解

#### 1. 数据模型层（models/）
**负责人：成员A**
- **窗口管理**：管理打饭窗口的基本信息（编号、菜品类型、服务速度）
- **队列管理**：记录各窗口的排队人数、等待时间
- **座位管理**：管理座位的占用状态、位置信息
- **数据库操作**：提供统一的数据访问接口

#### 2. 模拟引擎层（simulation/）
**负责人：成员B**
- **排队模拟**：模拟学生到达、排队、打饭的完整流程
- **时间推进**：按时间步进推进模拟，更新系统状态
- **数据分析**：统计不同时间段的排队情况、计算平均等待时间
- **智能推荐**：根据历史数据推荐最佳就餐时间

#### 3. API接口层（routes/）
**负责人：成员A**
- **状态查询**：提供食堂实时状态查询接口
- **数据统计**：提供历史数据统计接口
- **推荐服务**：提供最佳时间推荐接口
- **CORS配置**：处理跨域请求

#### 4. 前端展示层（static/ + templates/）
**负责人：成员C**
- **2D可视化**：使用Canvas绘制食堂平面图、动态显示排队人数
- **数据图表**：使用Chart.js展示等待时间趋势、人流量分布
- **交互界面**：提供用户友好的操作界面
- **实时更新**：通过AJAX定时刷新数据

### 开发顺序建议

1. **第一阶段**：数据库设计 + 基础API（成员A）
2. **第二阶段**：排队模拟算法（成员B）+ 前端框架搭建（成员C）
3. **第三阶段**：前后端联调 + 2D可视化（全员）
4. **第四阶段**：数据分析 + 功能完善（全员）

## 团队成员

- 成员A: 后端开发 + 数据库设计
- 成员B: 排队模拟算法
- 成员C: 前端可视化

## 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/your-team/Virtual_Canteen.git
cd Virtual_Canteen
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行项目
```bash
cd src
python app.py
```

### 4. 访问系统
打开浏览器访问: http://localhost:5000

## 项目结构

```
Virtual_Canteen/
├── src/                    # 源代码
│   ├── app.py             # Flask主程序
│   ├── models/            # 数据模型
│   ├── simulation/        # 模拟引擎
│   ├── routes/            # API路由
│   ├── static/            # 静态资源
│   └── templates/         # HTML模板
├── data/                  # 数据文件
├── docs/                  # 项目文档
├── tests/                 # 测试文件
└── requirements.txt       # 依赖包列表
```

## 核心功能

### ✅ 已完成
- [ ] 项目初始化
- [ ] 开发环境搭建

### 🚧 开发中
- [ ] 排队模拟算法
- [ ] 2D可视化界面
- [ ] 数据分析功能

### 📋 计划中
- [ ] 座位查找功能
- [ ] 最佳时间推荐
- [ ] 3D可视化升级

## 开发规范

### Git提交规范
```
feat: 新增功能
fix: 修复bug
docs: 文档更新
style: 代码格式
refactor: 代码重构
test: 测试相关
```

### 分支管理
- `main`: 稳定版本
- `dev`: 开发分支
- `feature/*`: 功能分支

## 文档

- [项目规划](./项目规划.md) - 完整的项目规划文档
- [项目日志](./ProjectInfo.md) - 开发日志记录
- [API文档](./docs/API文档.md) - 接口文档（待完善）
- [需求文档](./docs/需求文档.md) - 需求说明（待完善）

## 学习资源

- [Python教程](https://www.runoob.com/python3/python3-tutorial.html)
- [Flask文档](https://dormousehole.readthedocs.io/)
- [Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)

## 许可证

本项目仅用于课程学习和演示。

## 联系方式

如有问题，请在GitHub Issues中提出。

---

**开发周期**: 2026年3月 - 2026年6月  
**最后更新**: 2026-03-08
