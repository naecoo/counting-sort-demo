from manim import *

class CountingSort(Scene):
    def construct(self):
        # 介绍标题
        title = Text("计数排序 (Counting Sort)", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # 介绍算法
        intro_text = Text("计数排序是一种非比较排序算法", font_size=36)
        intro_text2 = Text("它的时间复杂度为O(n+k)，其中k是数值范围", font_size=36)
        intro_text2.next_to(intro_text, DOWN)
        
        self.play(Write(intro_text))
        self.wait(1)
        self.play(Write(intro_text2))
        self.wait(2)
        self.play(FadeOut(intro_text), FadeOut(intro_text2))
        
        # 展示输入数组
        input_array = [4, 2, 8, 3, 1, 5, 7, 6, 9]
        input_squares = self.create_array(input_array, "输入数组")
        
        self.play(FadeIn(input_squares["title"]))
        self.play(*[FadeIn(square) for square in input_squares["squares"]])
        self.play(*[FadeIn(num) for num in input_squares["numbers"]])
        self.wait(1)
        
        # 创建计数数组
        count_array = [0] * 10  # 0-9的计数数组
        count_squares = self.create_array(count_array, "计数数组 (索引 0-9)", y_offset=-2)
        
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
        
        # 创建累积计数数组
        cumulative_text = Text("计算累积计数", font_size=36)
        cumulative_text.to_edge(UP)
        self.play(Write(cumulative_text))
        
        cumulative_array = count_array.copy()
        for i in range(1, 10):
            cumulative_array[i] += cumulative_array[i-1]
        
        cumulative_squares = self.create_array(cumulative_array, "累积计数数组", y_offset=-4)
        
        self.play(FadeIn(cumulative_squares["title"]))
        self.play(*[FadeIn(square) for square in cumulative_squares["squares"]])
        
        # 动画展示累积计数过程
        for i in range(10):
            self.play(FadeIn(cumulative_squares["numbers"][i]))
            if i > 0:
                self.play(
                    count_squares["squares"][i-1].animate.set_fill(BLUE, opacity=0.2),
                    count_squares["squares"][i].animate.set_fill(YELLOW, opacity=0.2)
                )
                self.wait(0.5)
                self.play(
                    count_squares["squares"][i-1].animate.set_fill(WHITE, opacity=0),
                    count_squares["squares"][i].animate.set_fill(WHITE, opacity=0)
                )
        
        self.wait(1)
        
        # 创建输出数组
        output_array = [0] * len(input_array)
        output_squares = self.create_array(output_array, "输出数组", y_offset=-6)
        
        self.play(FadeIn(output_squares["title"]))
        self.play(*[FadeIn(square) for square in output_squares["squares"]])
        self.play(*[FadeIn(num) for num in output_squares["numbers"]])
        
        # 从后向前遍历输入数组，根据累积计数数组放置元素
        for i in range(len(input_array)-1, -1, -1):
            num = input_array[i]
            
            # 高亮当前处理的元素
            self.play(
                input_squares["squares"][i].animate.set_fill(YELLOW, opacity=0.5)
            )
            
            # 高亮累积计数数组中对应的位置
            self.play(
                cumulative_squares["squares"][num].animate.set_fill(YELLOW, opacity=0.5)
            )
            
            # 计算输出位置
            position = cumulative_array[num] - 1
            cumulative_array[num] -= 1
            
            # 更新累积计数数组显示
            new_cumulative = Text(str(cumulative_array[num]), font_size=36)
            new_cumulative.move_to(cumulative_squares["numbers"][num])
            
            # 在输出数组中放置元素
            new_output = Text(str(num), font_size=36)
            new_output.move_to(output_squares["numbers"][position])
            
            self.play(
                Transform(cumulative_squares["numbers"][num], new_cumulative),
                Transform(output_squares["numbers"][position], new_output),
                output_squares["squares"][position].animate.set_fill(GREEN, opacity=0.3)
            )
            
            # 恢复颜色
            self.play(
                input_squares["squares"][i].animate.set_fill(WHITE, opacity=0),
                cumulative_squares["squares"][num].animate.set_fill(WHITE, opacity=0)
            )
            
        self.wait(1)
        
        # 展示最终排序结果
        result_text = Text("排序完成!", font_size=48)
        result_text.to_edge(UP)
        
        self.play(
            FadeOut(cumulative_text),
            FadeIn(result_text)
        )
        
        # 高亮显示排序后的数组
        self.play(*[
            output_squares["squares"][i].animate.set_fill(GREEN, opacity=0.5)
            for i in range(len(output_array))
        ])
        
        self.wait(2)
        
        # 总结
        self.play(
            FadeOut(result_text),
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        summary = VGroup(
            Text("计数排序总结:", font_size=48),
            Text("1. 适用于已知范围的整数排序", font_size=36),
            Text("2. 时间复杂度: O(n+k)", font_size=36),
            Text("3. 空间复杂度: O(n+k)", font_size=36),
            Text("4. 是稳定的排序算法", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(summary))
        self.wait(3)
        
        # 结束
        end_text = Text("感谢观看!", font_size=60)
        self.play(FadeOut(summary))
        self.play(Write(end_text))
        self.wait(2)
        self.play(FadeOut(end_text))
    
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