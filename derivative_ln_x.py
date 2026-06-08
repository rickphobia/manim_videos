from manim import *
import intro

class LnX(Scene):
    def construct(self):
        intro.op(self,introtext="Finding The Derivatives of ln x")
        self.creating_func()
    
    def creating_func(self):
        """create two function and give it a diff color """
        f_x = MathTex("f(x) = e^{x}",color = BLUE).shift(LEFT*2)
        g_x = MathTex("g(x) = \ln \,x", color = RED).shift(RIGHT*2)
        self.play(Write(f_x),Write(g_x))
        self.wait(1)


        func = VGroup(f_x,g_x)
        self.play(func.animate.shift(UP*3.5))
        self.wait(1)


        f_g_x = MathTex("f(g(x)) = e^{\ln \, x}").shift(UP*2.5)
        f_g_x[0][0:7].set_color(BLUE)
        f_g_x[0][2:6].set_color(RED)
        f_g_x[0][8:9].set_color(BLUE)
        f_g_x[0][9:].set_color(RED)
        self.play(Write(f_g_x),run_time = 1.7)
        self.wait(1)


        note_01 = MathTex("a^{\log_{a} x } = x ").to_corner(UR,buff = 0.7)
        box_01 = SurroundingRectangle(note_01,color = WHITE, buff = 0.23)
        notes = Text("Notes:",font_size=30).next_to(note_01,UP*1.2).shift(LEFT*0.8)
        notes_1 = VGroup(note_01,box_01,notes)
        self.play(
            Write(notes))
        self.play(
            Write(box_01),
            Write(note_01),
        )

        self.wait(1.7)


        f_g_x_1 = MathTex("f(g(x)) = x").next_to(f_g_x,DOWN,aligned_edge=LEFT)
        f_g_x_1[0][0:7].set_color(BLUE)
        f_g_x_1[0][2:6].set_color(RED)
        self.play(Write(f_g_x_1[0][:-1]))
        self.play(TransformFromCopy(f_g_x[0][8:],note_01[0][:-2]),run_time = 1.5)
        self.play(TransformFromCopy(note_01[0][-1],f_g_x_1[0][-1]))
        self.wait(1.7)


        self.play(FadeOut(notes_1))
        self.wait(1)


        f_g_x_3 = MathTex(r"\frac{d}{dx}",r"f(g(x))= ",r"f^{\prime} (g(x)) \cdot g^{\prime} (x)").next_to(f_g_x_1, DR).shift(DOWN*0.5).shift(LEFT*0.3)
        f_g_x_3[1][0:7].set_color(BLUE)
        f_g_x_3[1][2:6].set_color(RED)
        f_g_x_3[2][0:8].set_color(BLUE)
        f_g_x_3[2][3:7].set_color(RED)
        f_g_x_3[2][9:].set_color(RED)
        f_g_x_2 = MathTex(r"\frac{d}{dx}",r"f(g(x)) = \frac{d}{dx} \,x ").next_to(f_g_x_3,LEFT).shift(LEFT*2)
        f_g_x_2[1][0:7].set_color(BLUE)
        f_g_x_2[1][2:6].set_color(RED)
        arrow1 = Arrow(start = f_g_x.get_right(), end = f_g_x_3.get_center(), buff = 0.4, color = TEAL_D)
        arrow2 = Arrow(start = f_g_x_1.get_left(), end = f_g_x_2.get_center(), buff = 0.4, color = TEAL_D)
        self.play(Create(arrow2))
        self.play(Write(f_g_x_2),run_time = 2)
        self.wait(1)


        replacement = MathTex('1').move_to(f_g_x_2,RIGHT).shift(LEFT*0.5)
        self.play(Transform(VGroup(f_g_x_2[1][8:]),replacement))
        self.wait(1)


        self.play(FadeOut(arrow2))
        self.play(Create(arrow1))
        self.play(Write(f_g_x_3),run_time = 3)
        self.play(FadeOut(arrow1))
        self.wait(1.7)


        f_g_x_35 = MathTex(r"\frac{d}{dx}",r"f(g(x))=e^{\ln\, x} \cdot g'(x)").next_to(f_g_x_3, DOWN,aligned_edge=LEFT)
        f_g_x_35[1][0:7].set_color(BLUE)
        f_g_x_35[1][2:6].set_color(RED)
        f_g_x_35[1][8].set_color(BLUE)
        f_g_x_35[1][9:12].set_color(RED)
        f_g_x_35[1][13:].set_color(RED)
        self.play(Write(f_g_x_35),run_time = 2)
        self.wait(1)
        
        elnx_grp = VGroup(f_g_x_35[1][8:12])
        replacement_1 = MathTex('x').move_to(elnx_grp).shift(DOWN*0.1)
        self.play(Transform(elnx_grp,replacement_1))
        self.wait(1)

        xgx_grp = VGroup(replacement_1,f_g_x_35[1][12:])

        f_g_x_4 = MathTex(r"x \cdot g'(x)", "=",r"1").next_to(f_g_x_35,DOWN).shift(LEFT*4.3).shift(DOWN*0.7)
        f_g_x_4[0][2:].set_color(RED)
        self.play(
            TransformFromCopy(xgx_grp,f_g_x_4[0]),
            Write(f_g_x_4[1]),
            TransformFromCopy(replacement,f_g_x_4[-1][:]),
            run_time = 2
            )
        
        self.wait(1)

        replacement_3 = MathTex(r"\frac{1}{x}").move_to(f_g_x_4[-1])
        
        self.play(
            FadeOut(f_g_x_4[-1]),
            ReplacementTransform(f_g_x_4[0][0:2],replacement_3))

        self.wait(1)
        replacement_4 = MathTex(r"\frac{d}{dx} \, \ln \, x").move_to(f_g_x_4[0][2]).shift(UP*0.1+RIGHT*0.1)
        self.play(Transform(f_g_x_4[0][2:],replacement_4),run_time = 2)
        self.wait(2)
        dydx_grp = VGroup(f_g_x_4,replacement_4,replacement_3)
        eq1 = MathTex(r"\int \frac{1}{x} \, dx = \ln{\left|x\right|} + C").move_to(f_g_x_4)

        self.play(
            Transform(dydx_grp,eq1),
            run_time = 2)
        self.wait(2)


        

