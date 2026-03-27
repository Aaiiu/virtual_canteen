# -*- coding: utf-8 -*-
import os

path = r'd:\Project\Virtual_Canteen_Repository\virtual_canteen\docs\设计规格说明书.md'

part3 = """
---

## 四、系统架构

### 4.1 模块划分总览

本系统划分为五大模块：数据模型模块、仿真引擎模块、API接口模块、前端展示模块、数据存储模块。

    前端展示模块
      2D可视化 | 悬停浮窗 | 图表 | 对比面板
           ↕ HTTP/JSON
    API接口模块
      Flask路由 | 数据序列化 | CORS
         ↕                    ↕
    仿真引擎模块          数据模型模块
      排队模拟  ←→  窗口/学生/座位/词条
      特性词条               ↕
      对比分析          数据存储模块
      时间分析            SQLite数据库

### 4.2 各模块功能详述

#### 模块一：数据模型模块（src/models/）
负责人：成员A

| 子模块 | 文件 | 核心功能 |
|--------|------|----------|
| 窗口模型 | window.py | 打饭窗口的编号、菜系名称、基础服务时间 |
| 学生模型 | student.py | 学生ID、姓名、菜品偏好、个体速度系数 |
| 特性词条模型 | trait.py | 词条名称、触发概率、效果类型和参数 |
| 座位模型 | seat.py | 座位编号、占用状态、关联学生ID、是否曾被使用 |
| 队列模型 | queue.py | 各窗口实时排队人数和预计等待时间 |
| 数据库配置 | database.py | 初始化SQLAlchemy连接，管理数据库会话 |

#### 模块二：仿真引擎模块（src/simulation/）
负责人：成员B（部分与成员A协作）

| 子模块 | 文件 | 核心功能 |
|--------|------|----------|
| 学生生成器 | student_generator.py | 按到达率生成学生，按概率分配特性词条 |
| 排队模拟器 | queue_simulator.py | 多窗口排队、偏好匹配、等待阈值切换 |
| 座位管理器 | seat_manager.py | 座位分配释放，孤独症学生专属逻辑 |
| 时间段分析 | time_analysis.py | 统计各时段等待时间，标注高峰期 |
| 对比模拟 | comparison.py | 策略A和策略B双路运行，输出对比数据 |
| 推荐引擎 | recommendation.py | 基于历史数据推荐最佳就餐时间 |

#### 模块三：API接口模块（src/routes/）
负责人：成员A

| 接口路径 | 方法 | 功能说明 |
|----------|------|----------|
| /api/status | GET | 获取食堂整体状态 |
| /api/windows | GET | 获取所有窗口排队信息 |
| /api/seats | GET | 获取所有座位状态 |
| /api/seat/{id} | GET | 获取指定座位学生详情（悬停浮窗用） |
| /api/simulate/start | POST | 启动新一轮模拟（传入超参数配置） |
| /api/simulate/status | GET | 获取当前模拟进度和实时数据 |
| /api/analysis/time | GET | 获取时间段分析数据 |
| /api/analysis/comparison | POST | 启动对比模拟，传入偏好参数 |
| /api/recommendation | GET | 获取最佳就餐时间推荐结果 |

所有接口统一返回JSON格式：

    { "code": 200, "message": "success", "data": { ... } }

#### 模块四：前端展示模块（src/static/ + src/templates/）
负责人：成员C

| 子模块 | 文件 | 核心功能 |
|--------|------|----------|
| 主逻辑 | main.js | 定时轮询API，统筹各模块数据更新 |
| 2D可视化 | visualization.js | Canvas绘制食堂平面图、窗口、队列、座位 |
| 悬停浮窗 | tooltip.js | 监听鼠标事件，悬停座位时显示学生信息卡 |
| 数据图表 | charts.js | Chart.js渲染折线图、柱状图、饼图 |
| 对比面板 | comparison.js | 展示策略A vs 策略B的对比数据卡片 |

#### 模块五：数据存储模块

使用SQLite作为本地数据库，通过Flask-SQLAlchemy进行ORM操作，数据库文件位于 data/canteen.db。

### 4.3 模块间协同关系

    用户触发操作
        ↓
    前端展示模块 → API接口模块
                        ↓
                   仿真引擎模块
                    ↓         ↓
              数据模型模块  数据存储模块
                    ↓
              计算结果返回
                    ↓
         API接口模块 → 前端展示模块
                            ↓
                   更新Canvas/图表/浮窗

### 4.4 模块间数据交换说明

| 数据交换方向 | 数据内容 | 接口形式 |
|-------------|----------|----------|
| 前端 → API | 模拟启动参数（超参数、偏好设置） | HTTP POST / JSON Body |
| API → 前端 | 窗口排队信息、座位状态、学生详情 | HTTP GET / JSON Response |
| API → 仿真引擎 | 模拟配置参数 | Python函数调用 |
| 仿真引擎 → 数据模型 | 学生对象、队列状态、座位分配结果 | SQLAlchemy ORM操作 |
| 数据模型 → 数据存储 | 窗口/学生/座位/队列数据 | SQLite SQL语句 |
| 数据存储 → API | 查询结果集 | SQLAlchemy查询对象 |
"""

with open(path, 'a', encoding='utf-8') as f:
    f.write(part3)

print('part3 done')
