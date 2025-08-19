#!/usr/bin/env python3

import subprocess
import os
from ament_index_python.packages import get_package_share_directory

def save_current_rviz_config():
    """
    保存当前rviz2配置到文件
    """
    package_dir = get_package_share_directory('pi_description')
    config_dir = os.path.join(package_dir, 'config')
    config_file = os.path.join(config_dir, 'pi_config_saved.rviz')
    
    print(f"正在保存rviz2配置到: {config_file}")
    
    # 启动rviz2并指定配置文件
    try:
        # 使用当前配置启动rviz2
        subprocess.run([
            'ros2', 'run', 'rviz2', 'rviz2',
            '--display-config', config_file
        ])
    except KeyboardInterrupt:
        print("\n用户中断操作")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    save_current_rviz_config() 