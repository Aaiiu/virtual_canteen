# 项目配置文件
# 数据库配置、模拟参数配置等

class Config:
    # 数据库配置
    DATABASE_PATH = '../data/canteen.db'
    
    # 食堂配置
    WINDOW_COUNT = 8  # 窗口数量
    SEAT_COUNT = 200  # 座位数量
    
    # 模拟参数
    SIMULATION_SPEED = 1.0  # 模拟速度倍率
    PEAK_HOURS = [(11, 13), (17, 19)]  # 高峰时段
