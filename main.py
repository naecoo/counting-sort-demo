from manim import *

class CountingSort(Scene):
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
        count_squares = self.create_array(count_array, "计数数组", y_offset=-1)
        
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
        output_squares = self.create_array(output_array, "输出数组", y_offset=-2)
        
        # 显示输出数组标题和初始状态
        self.play(FadeIn(output_squares["title"]))
        self.play(*[FadeIn(square) for square in output_squares["squares"]])
        self.play(*[FadeIn(num) for num in output_squares["numbers"]])
        self.wait(1)
        
        # 计算累积计数
        for i in range(1, len(count_array)):
            count_array[i] += count_array[i - 1]
            
            # 更新计数数组显示
            new_count = Text(str(count_array[i]), font_size=36)
            new_count.move_to(count_squares["numbers"][i])
            
            self.play(
                count_squares["squares"][i].animate.set_fill(BLUE, opacity=0.5),
                Transform(count_squares["numbers"][i], new_count)
            )
            self.wait(0.3)
            self.play(
                count_squares["squares"][i].animate.set_fill(WHITE, opacity=0)
            )
        
        # 构建输出数组
        for i in range(len(input_array) - 1, -1, -1):
            num = input_array[i]
            output_index = count_array[num] - 1
            
            # 更新输出数组
            output_array[output_index] = num
            new_num = Text(str(num), font_size=36)
            new_num.move_to(output_squares["numbers"][output_index])
            
            # 动画展示过程
            self.play(
                input_squares["squares"][i].animate.set_fill(GREEN, opacity=0.5),
                output_squares["squares"][output_index].animate.set_fill(GREEN, opacity=0.5),
                Transform(output_squares["numbers"][output_index], new_num)
            )
            self.wait(0.3)
            
            # 更新计数并恢复颜色
            count_array[num] -= 1
            self.play(
                input_squares["squares"][i].animate.set_fill(WHITE, opacity=0),
                output_squares["squares"][output_index].animate.set_fill(WHITE, opacity=0)
            )
        
        self.wait(2)
        
    
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