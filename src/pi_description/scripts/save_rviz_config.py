#!/usr/bin/env python3

import os
import sys
import subprocess
import time

def save_rviz_config():
    """
    保存当前rviz2配置的脚本
    """
    print("正在启动rviz2并等待配置...")
    
    # 启动rviz2
    rviz_process = subprocess.Popen([
        'ros2', 'run', 'rviz2', 'rviz2'
    ])
    
    print("rviz2已启动，请进行以下操作：")
    print("1. 在rviz2中加载pi机器人模型")
    print("2. 调整视角和显示设置")
    print("3. 点击 File -> Save Config As...")
    print("4. 保存配置文件到 src/pi_description/config/pi_config.rviz")
    print("5. 关闭rviz2窗口")
    
    try:
        # 等待用户操作
        input("按Enter键继续...")
    except KeyboardInterrupt:
        print("\n用户中断操作")
    finally:
        # 终止rviz2进程
        rviz_process.terminate()
        rviz_process.wait()
        print("rviz2已关闭")

if __name__ == "__main__":
    save_rviz_config() 