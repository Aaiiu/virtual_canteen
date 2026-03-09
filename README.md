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
