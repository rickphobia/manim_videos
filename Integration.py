from manim import * 
import intro 


class Integration(Scene):
    def construct(self):
        audio = 'assets/snowman.mp3'
        self.add_sound(audio)
        intro.op(self,introtext="Calculating Area Under Curve",introformula='\int f(x) \,d(x)')

        self.drawing_graph()
        self._2_rect()    
        self._4_rect()    
        self._32_rect()
        self._64_rect()
        self._128_rect()
        self._1024_rect()

    def drawing_graph(self):
        ax = Axes(
            x_range = [0,9,1], 
            y_range = [0,18,2],
            x_length = 8,
            y_length=  8,
            axis_config={"include_numbers":True}
            
        ).scale(0.8)
            
        
        
        self.ax = ax 
        x_label = MathTex('x').next_to(ax.x_axis.get_right(),RIGHT).scale(0.8)
        y_label = MathTex('f(x)').next_to(ax.y_axis.get_top(),UP).scale(0.8)
        axis_labels = VGroup(x_label, y_label)


        f1_formula = MathTex("f(x) = -x^2+8x").next_to(ax,UP).shift(DR*0.15)
        f1 = ax.plot(lambda x: (-x**2+8*x), x_range=[0,8],color = WHITE)
        self.play(Create(ax),run_time = 3)
        self.play(Write(axis_labels))
        self.play(
            Write(f1_formula),
            Create(f1),
            
            run_time= 2

            )
        
        self.graph = VGroup(axis_labels,f1,f1_formula,ax)
        self.play(self.graph.animate.shift(LEFT*3))
        self.wait(2)
        


    def rect_approximate_area(self, amount, area_v, dx):
        if hasattr(self, 'values'):
            self.play(FadeOut(self.values))

        fontsize = 46

        if not hasattr(self, 'labels'):
            rect_label = Text("Rectangle Used = ", font_size=32)
            length_label = Text("Length of dx = ", font_size=32)
            real_area_label = Text("Real Area = ", font_size=32)
            area_label = MathTex(r"\int f(x) \,\, dx \, = ", font_size=42)
            self.labels = VGroup(rect_label, length_label, real_area_label, area_label).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            self.labels.next_to(self.graph, buff=0.6)
            self.play(Write(self.labels))

        rect_value = MathTex(str(amount), font_size=fontsize)
        length_value = MathTex(str(dx), font_size=fontsize)
        real_area_value = MathTex("85.3333", font_size=fontsize)
        area_value = MathTex(f"{area_v:.4f}", font_size=fontsize)

        values_list = [rect_value, length_value, real_area_value, area_value]
        
        # Get the rightmost x-coordinate of all labels to align values consistently
        right_edge = max([label.get_right()[0] for label in self.labels])
        
        # First, position each value next to its corresponding label
        for i, value in enumerate(values_list):
            # Match y position to the center of corresponding label
            y_pos = self.labels[i].get_center()[1]
            z_pos = value.get_center()[2]
            
            # Temporarily position the value
            value.move_to([right_edge + 0.4, y_pos, z_pos])
        
        # Create VGroup and arrange with RIGHT alignment
        self.values = VGroup(*values_list)
        self.values.arrange(DOWN, aligned_edge=RIGHT, buff=0.3)
        
        # Position the entire group next to labels
        self.values.next_to(self.labels, RIGHT, buff=0.4)
        
        # Re-align each value with its corresponding label vertically
        for i, value in enumerate(values_list):
            # Keep the right-aligned x position
            current_x = value.get_center()[0]
            # Get y position from corresponding label
            label_y = self.labels[i].get_center()[1]
            # Move to correct position
            value.move_to([current_x, label_y, 0])

        self.play(Write(self.values))


    def creating_rect(self,dx):
        rectangles = VGroup()
        x_max = 8
        num = int(x_max/dx)
        total_area = 0 
        self.rect_data = []
        for i in range(num):

            x_left = i * dx
            mid = x_left +dx/2
            height = mid*(8-mid)


            bottom_left = self.ax.c2p(x_left,0)
            bottom_right = self.ax.c2p(x_left+dx,0 )
            top_right = self.ax.c2p(x_left+dx, height)
            top_left = self.ax.c2p(x_left,height )
            rect =Polygon(
                bottom_left,
                bottom_right,
                top_right,
                top_left,
                fill_color = BLUE_E,
                fill_opacity = 0.6
            )




            rectangles.add(rect)
            total_area += height*dx


            self.rect_data.append({
                "indexs" : i,
                "x_left" : x_left,
                "x_right" : x_left + dx,
                "height":height,
                "rect" : rect
            })

        return rectangles,total_area
            

                
    
    def showing_rect(self,dx):
        if hasattr(self,"current_rects"):
            self.play(FadeOut(self.current_rects))
        rect, area = self.creating_rect(dx)
        
        self.current_rects = rect 

        self.play(
            LaggedStart(*[GrowFromEdge(r,DOWN) for  r in rect], lag_ratio = 0.2),
            run_time = 2,
        )

        self.rect_approximate_area(int(8/dx),area,dx)
        self.wait(2)

    def _2_rect(self):
        dx = 4 
        x_left = 0 
        height = -2**2+8*2
        _1_bottom_left = self.ax.c2p(x_left,0)
        _1_bottom_right = self.ax.c2p(x_left+dx,0)
        _1_top_right = self.ax.c2p(x_left+dx,height)
        _1_top_left = self.ax.c2p(x_left,height)
        
        rect1 = Polygon(_1_bottom_left,_1_bottom_right,_1_top_right,_1_top_left,fill_color = BLUE_E,fill_opacity = 0.6)
        


        _2_bottom_left = self.ax.c2p(x_left+4,0)
        _2_bottom_right = self.ax.c2p(x_left+4+dx,0)
        _2_top_right = self.ax.c2p(x_left+4+dx,height)
        _2_top_left = self.ax.c2p(x_left+4,height)
        
        rect2 = Polygon(_2_bottom_left,_2_bottom_right,_2_top_right,_2_top_left,fill_color = BLUE_E,fill_opacity = 0.6)
        

        self.play(Create(rect1),Create(rect2),run_time = 2)
        fontsize = 36
        dx_text = MathTex('dx_{1}',font_size=fontsize).next_to(rect1,DOWN,buff= -0.4)
        dx_text1 = MathTex('dx_{2}',font_size=fontsize).next_to(rect2,DOWN,buff= -0.4)
        height_text = MathTex('f(x)',font_size=fontsize).next_to(rect1,RIGHT,buff = -1)
        self.play(
            Write(dx_text),
            Write(dx_text1),
            Write(height_text),
        )
        fontsize1 = 40
        area = MathTex('Approximate \, Area',font_size = fontsize)
        tips = MathTex('*','\int','means \,sum \,(continuous)',font_size = fontsize-10)
        sum_label = MathTex("= \,Sum \, of \,all \,rectangles\,",'(',"\int rectangles",')',font_size= fontsize)
        rect_label = MathTex('=','rectangle_{1}', '+','rectangle_{2}',font_size = fontsize)
        width_label = MathTex('=', 'height_{1}','*','width_{1}','+','height_{2}','*','width_{2}',font_size = fontsize)
        formula_label = MathTex('=', '\int', 'height', '*', 'width',font_size = fontsize)
        formula_label1 = MathTex('=', '\int', 'f(x)', '\,\,dx',font_size = fontsize)
        real_area = MathTex('=', '12','*','4', '+', '12','*','4',font_size = fontsize)
        real_area1 = MathTex('=', '96',font_size = fontsize)
        approximate_label = VGroup(area,sum_label,rect_label,width_label,formula_label,formula_label1,real_area,real_area1).arrange(DOWN,aligned_edge = LEFT).next_to(self.graph,RIGHT,buff = -0.5)
        grp = VGroup(approximate_label,dx_text,dx_text1,height_text,tips)
        self.wait(2)
        self.play(Write(area))
        self.wait(1)

        self.play(Write(sum_label),run_time = 2)
        self.wait(1)

        tips.next_to(area,UP,buff = 0.4)
        self.play(Write(tips))
        self.wait(1)

        self.play(Write(rect_label))
        self.wait(1)

        self.play(Write(width_label),run_time =2)
        self.wait(2)

        self.play(Write(formula_label),run_time = 2)
        self.wait(2)

        dx_grp = VGroup(dx_text,dx_text1)
        self.play(
            TransformFromCopy(formula_label[2],height_text),
            TransformFromCopy(formula_label[4],dx_grp),
            run_time = 3
        )
        self.wait(1)
        self.play(Write(formula_label1[0:2]))
        self.play(
            TransformFromCopy(height_text,formula_label1[2]),
            TransformFromCopy(dx_grp,formula_label1[3]),
            run_time = 3
        )
        fx_grp = VGroup(real_area[1],real_area[5])
        dx_grp1 = VGroup(real_area[3],real_area[7])
        self.play(
            Write(real_area[0]),
            TransformFromCopy(formula_label1[2],fx_grp),
            Write(real_area[2]),
            TransformFromCopy(formula_label1[3],dx_grp1),
            Write(real_area[4]),
            Write(real_area[6]),
            run_time = 3
        )
        self.wait(1)
        self.play(Write(real_area1))
        self.wait(3)

        self.play(FadeOut(grp))

        self.rect_approximate_area(2,96,4)
        self.wait(2)
        rect_grp = VGroup(rect1,rect2)
        self.play(
            FadeOut(rect_grp),
            FadeOut(self.values),
            FadeOut(self.labels)
            )


    def _4_rect(self):
        dx = 2 
        num = 8
        dx_text_grp = [] 
        height_text_grp = [] 
        rectangles = VGroup() 
        for i in range(4):
            x_left = i*dx
            x_right = x_left + dx 
            x_mid = (x_left + x_right)/2 
            height = -x_mid**2 + x_mid*8

            bottom_left = self.ax.c2p(x_left,0)
            bottom_right = self.ax.c2p(x_right,0)
            top_right = self.ax.c2p(x_right,height)
            top_left = self.ax.c2p(x_left,height)
            rect = Polygon(
                bottom_left,
                bottom_right,
                top_right,
                top_left,                
                fill_color = BLUE_E,
                fill_opacity = 0.6
            )
            

            rectangles.add(rect)
            num = i+1 
            fontsize = 36   
            dx_text = MathTex(f'dx_{({num})}',font_size=fontsize).next_to(rect,DOWN,buff= -0.4)
            height_text = MathTex(f'f(x)_{{{num}}}',font_size=fontsize).next_to(rect,RIGHT,buff = -0.9)
            dx_text_grp.append(dx_text)
            height_text_grp.append(height_text)
        self.play(
                LaggedStart(*[GrowFromEdge(r,DOWN) for  r in rectangles], lag_ratio = 0.2),
                run_time = 2,
        )
        self.wait(1)
        dx_height_text = VGroup(dx_text_grp,height_text_grp)
        self.play(Write(dx_height_text))
        area = MathTex('Approximate \, Area',font_size = fontsize)
        sum_label = MathTex("=\, \int rectangles",font_size= fontsize)
        formula_label1 = MathTex('=', '\int', 'f(x)', '\,\,dx',font_size = fontsize)
        real_area = MathTex('=', 'f(x)_{1}*dx_{1}','+','f(x)_{2}*dx_{2}','+','f(x)_{3}*dx_{3}',font_size = fontsize)
        real_area3 = MathTex('\, \, +f(x)_{4}*dx_{4}',font_size = fontsize)
        real_area1 = MathTex('=', '7*2','+','15*2','+','15*2','+','7*2',font_size = fontsize)
        real_area2 = MathTex('=', '88',font_size = fontsize)
        approximate_label = VGroup(area,sum_label,formula_label1,real_area,real_area3,real_area1,real_area2).arrange(DOWN,aligned_edge = LEFT).next_to(self.graph,RIGHT,buff = -0.5)
        grp = VGroup(approximate_label,dx_height_text)
        self.play(Write(area))
        self.wait(1)

        self.play(Write(sum_label))
        self.wait(1)

        self.play(Write(formula_label1),run_time = 2)
        self.wait(1.5)

        self.play(Write(real_area))
        self.play(Write(real_area3))
        self.wait(2)

        self.play(
            Write(real_area1[0]),
            Write(real_area1[2]),
            Write(real_area1[4]),
            Write(real_area1[6]),

            Write(real_area1[1][1]),
            Write(real_area1[3][2]),
            Write(real_area1[5][2]),
            Write(real_area1[7][1]),

            TransformFromCopy(dx_text_grp[0],real_area1[1][0]),
            TransformFromCopy(height_text_grp[0],real_area1[1][2]),

            TransformFromCopy(dx_text_grp[1],real_area1[3][0:2]),
            TransformFromCopy(height_text_grp[1],real_area1[3][3]),

            TransformFromCopy(dx_text_grp[2],real_area1[5][0:2]),
            TransformFromCopy(height_text_grp[2],real_area1[5][3]),
            
            TransformFromCopy(dx_text_grp[3],real_area1[7][0]),
            TransformFromCopy(height_text_grp[3],real_area1[7][2]),

            run_time = 4

        )
        self.wait(2)
        self.play(Write(real_area2))
        

        self.play(FadeOut(grp))
        self.play(FadeIn(self.labels))
        if hasattr(self, 'values'):
            self.remove(self.values)
            delattr(self, 'values')
        self.rect_approximate_area(4,88,2)
        self.wait(2)
        
        self.play(FadeOut(rectangles))
        



    def _32_rect(self):
        self.showing_rect(1/4)




    def _64_rect(self):
        self.showing_rect(1/8)
    def _128_rect(self):
        self.showing_rect(8/128)
    def _1024_rect(self):
        self.showing_rect(1/128)
        self.wait(1)
        text = MathTex('As', r"\lim_{dx \to 0} \int f(x) \, dx \,= \, Real Area ",font_size = 40).next_to(self.values,DOWN,buff = 0.5 ).shift(LEFT*2)
        self.play(Write(text),run_time = 4)
        self.wait(3)
        




"""
showing the approximate area is width*height of every rect
even show the million rect and says try to prove the formula 
"""

