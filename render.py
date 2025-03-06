from manim import *
from main import CountingSort
import sys
import os

if __name__ == "__main__":
    # 使用以下命令渲染动画
    # 低质量预览: python render.py -pql
    # 中等质量: python render.py -pqm
    # 高质量: python render.py -pqh
    # 最高质量: python render.py -pqk
    
    # 检查是否在虚拟环境中运行
    if not os.environ.get('VIRTUAL_ENV'):
        print("警告：建议在虚拟环境中运行此脚本")
        print("请使用以下命令激活虚拟环境：")
        print("source venv/bin/activate")
    
    # 设置配置以确保正确居中
    config.frame_width = 16  # 增加帧宽度
    config.frame_height = 9  # 设置帧高度，保持16:9比例
    config.pixel_width = 1920  # 设置像素宽度
    config.pixel_height = 1080  # 设置像素高度
    
    scene = CountingSort()
    scene.render()