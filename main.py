from manim import *
import sys
import os

class CountingSort(Scene):
    def __init__(self):
        super().__init__()
        # 设置配置以确保正确居中
        self.camera.frame_width = 16  # 增加帧宽度
        self.camera.frame_height = 9  # 设置帧高度，保持16:9比例
        self.camera.pixel_width = 1920  # 设置像素宽度
        self.camera.pixel_height = 1080  # 设置像素高度

    def construct(self):
        # 介绍标题
        title = Text("计数排序", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # 展示输入数组
        input_array = [2, 3, 2, 3, 1, 4, 5, 5, 6, 7]
        input_squares = self.create_array(input_array, "输入数组")
        
        self.play(FadeIn(input_squares["title"]))
        self.play(*[FadeIn(square) for square in input_squares["squares"]])
        self.play(*[FadeIn(num) for num in input_squares["numbers"]])
        self.wait(1)
        
        # 创建计数数组
        count_array = [0] * 10  # 0-9的计数数组
        count_squares = self.create_array(count_array, "计数数组", y_offset=-2)
        
        # 添加索引标签
        index_labels = []
        for i in range(10):
            label = Text(str(i), font_size=24)
            label.next_to(count_squares["squares"][i], UP, buff=0.3)
            index_labels.append(label)
        
        self.play(FadeIn(count_squares["title"]))
        self.play(*[FadeIn(square) for square in count_squares["squares"]])
        self.play(*[FadeIn(num) for num in count_squares["numbers"]])
        self.play(*[FadeIn(label) for label in index_labels])
        self.wait(1)
        
        # 执行计数过程
        for i, num in enumerate(input_array):
            # 高亮当前处理的元素
            self.play(
                input_squares["squares"][i].animate.set_fill(YELLOW, opacity=0.5)
            )
            
            # 更新计数数组
            count_array[num] += 1
            new_count = Text(str(count_array[num]), font_size=36)
            new_count.move_to(count_squares["numbers"][num])
            
            self.play(
                count_squares["squares"][num].animate.set_fill(YELLOW, opacity=0.5),
                Transform(count_squares["numbers"][num], new_count)
            )
            self.wait(0.5)
            
            # 恢复颜色
            self.play(
                input_squares["squares"][i].animate.set_fill(WHITE, opacity=0),
                count_squares["squares"][num].animate.set_fill(WHITE, opacity=0)
            )
        
        self.wait(1)
        
        # 生成输出结果
        output_array = [0] * len(input_array)
        output_squares = self.create_array(output_array, "输出数组", y_offset=-4)
        
        # 显示输出数组标题和初始状态
        self.play(FadeIn(output_squares["title"]))
        self.play(*[FadeIn(square) for square in output_squares["squares"]])
        self.play(*[FadeIn(num) for num in output_squares["numbers"]])
        self.wait(1)
        
        # 构建输出数组
        j = 0
        for i in range(len(count_array)):
            while count_array[i] > 0:
                count_array[i] -= 1
                output_array[j] = i
                
                new_output_num = Text(str(output_array[j]), font_size=36)
                new_output_num.move_to(output_squares["numbers"][j])
                new_count_num = Text(str(count_array[i]), font_size=36)
                new_count_num.move_to(count_squares["numbers"][i])
                self.play(
                    Transform(count_squares["numbers"][i], new_count_num),
                    Transform(output_squares["numbers"][j], new_output_num),
                    count_squares["squares"][i].animate.set_fill(GREEN, opacity=0.5),
                    output_squares["squares"][j].animate.set_fill(GREEN, opacity=0.5),
                )
                self.wait(0.1)
                self.play(
                    count_squares["squares"][i].animate.set_fill(WHITE, opacity=0),
                    output_squares["squares"][j].animate.set_fill(WHITE, opacity=0)
                )
                
                j = j + 1
            
        self.wait(1)
            
        
    
    def create_array(self, array, title_text, y_offset=0):
        """创建数组的可视化表示"""
        result = {"squares": [], "numbers": []}
        
        # 创建标题
        title = Text(title_text, font_size=36)
        title.to_edge(UP).shift(DOWN + y_offset * UP)
        result["title"] = title
        
        # 计算数组总宽度，以便居中
        square_width = 0.8
        spacing = 0.1
        total_width = len(array) * square_width + (len(array) - 1) * spacing
        
        # 创建方块和数字
        for i, num in enumerate(array):
            square = Square(side_length=square_width)
            square.set_stroke(WHITE)
            square.set_fill(WHITE, opacity=0)
            
            number = Text(str(num), font_size=36)
            
            # 水平排列并居中
            if i == 0:
                # 第一个元素位置，考虑整体居中
                square.move_to([-total_width/2 + square_width/2, title.get_bottom()[1] - 1, 0])
            else:
                square.next_to(result["squares"][i-1], RIGHT, buff=spacing)
            
            number.move_to(square.get_center())
            
            result["squares"].append(square)
            result["numbers"].append(number)
        
        return result
      
if __name__ == "__main__":
    # 低质量预览: python main.py -pql
    # 中等质量: python main.py -pqm
    # 高质量: python main.py -pqh
    # 最高质量: python main.py -pqk
    scene = CountingSort()
    scene.render()