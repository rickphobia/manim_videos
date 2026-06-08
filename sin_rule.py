from manim import * 
import intro 

class SinRule(Scene): 
    def construct(self):
        intro.op(self,introtext="Proving Sin Rule", introformula=r"\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}")
        self.drawing_triangles_angles()
        self.equations()
        self.firsteq()
        self.secondeq()
        self.thirdeq() 
        self.fourtheq()
        self.proving_sin_rule()


    def drawing_triangles_angles(self):
        self.A = np.array([1, 2, 0])
        self.B = np.array([-5, -1, 0])
        self.C= np.array([3, -1, 0])
        triangle = Polygon(self.A, self.B, self.C, color=WHITE)
        
        self.play(Create(triangle))

        self.angle_A = Angle(Line(self.B,self.A), Line(self.C,self.A), radius=0.6, quadrant= (-1,-1),other_angle=False, color=BLUE)
        self.angle_B = Angle(Line(self.A,self.B), Line(self.C,self.B), radius= 1.4, quadrant= (-1,-1), other_angle=True, color = BLUE)
        self.angle_C = Angle(Line(self.A,self.C), Line(self.B,self.C), radius=1.2,quadrant= (-1,-1), other_angle=False, color=BLUE)

        self.angle_A_label = MathTex("A").move_to(self.angle_A.get_center() + 0.5*DOWN)
        self.angle_B_label = MathTex("B").move_to(self.angle_B.get_center() + 0.1*UR + 0.2*RIGHT)
        self.angle_C_label = MathTex("C").move_to(self.angle_C.get_center() + 0.3*UL)
        self.play(Create(self.angle_A),Write(self.angle_A_label))
        self.play(Create(self.angle_B),Write(self.angle_B_label))
        self.play(Create(self.angle_C),Write(self.angle_C_label))
        # Add labels for sides
        self.side_a = MathTex("a").move_to((self.B + self.C)/2 + DOWN*0.5).scale(1.5)
        self.side_b = MathTex("b").move_to((self.A + self.C)/2 + RIGHT*0.5).scale(1.5)
        self.side_c = MathTex("c").move_to((self.A + self.B)/2 + 0.4+  LEFT*0.5).scale(1.5)
        self.play(Write(self.side_a), Write(self.side_b), Write(self.side_c))
        self.wait(2)


        self.foot = np.array([1, -1, 0])
        self.height = DashedLine(self.A, self.foot, color=YELLOW)
        self.right_angle = RightAngle(Line(self.C, self.foot), Line(self.foot, self.A), length=0.3)
        self.play(Create(self.height), Create(self.right_angle))

        self.h_label = MathTex("h").next_to(self.height, LEFT)
        self.play(Write(self.h_label))
        
        # self.play(self.angle_C_label.set_color(YELLOW))
        self.left_trig = Polygon(self.A,self.B,self.foot,fill_color = TEAL_A, fill_opacity = 0.5, stroke_color =WHITE )
        self.right_trig = Polygon(self.A,self.C,self.foot,fill_color = TEAL_E,fill_opacity = 0.5, stroke_color =WHITE)

        self.triangle = triangle
    def equations(self):
        self.eq01 = MathTex(r"\sin", "(", "B", ")", "=", r"\frac{h}{c}").next_to(self.side_a,DL,buff = 0.3)
        self.eq02 = MathTex(r"\sin", "(", "C", ")", "=", r"\frac{h}{b}").next_to(self.eq01,RIGHT,buff = 2)
        self.eq03 = MathTex("c",r"\cdot",r"\sin(B)", "=", "h", "=", "b", r"\cdot",r"\sin(C)", ).to_corner(UR,buff = 0.3)
        self.eq04 = MathTex( r"\frac{c}{\sin(C)}", "=", r"\frac{b}{\sin(B)}").next_to(self.eq03,DOWN)
        self.eq =  MathTex( r"\frac{a}{\sin(A)}","=",r"\frac{b}{\sin(B)}", "=", r"\frac{c}{\sin(C)}").next_to(self.eq04,DOWN).shift(LEFT*0.1)
    
    def firsteq(self):
        eq01 = self.eq01
        B_target = eq01[2]
        sin_brackets = VGroup(eq01[0], eq01[1], eq01[3])
        self.play(Write(sin_brackets))
        self.wait(1.5)

        
        self.play(TransformFromCopy(self.angle_B_label,B_target))
        self.play(Write(eq01[4]))
        fraction = eq01[5]
        self.h_target = fraction[0][0]

        self.c_target = fraction[2][0]
        self.play(TransformFromCopy(self.h_label, self.h_target))
        self.play(Write(eq01[5][1]))
        self.play(TransformFromCopy(self.side_c, self.c_target))
        self.wait(1)
        self.play(FadeOut(self.left_trig))
        self.wait(1.5)
        self.play(FadeIn(self.right_trig))        

    def secondeq(self):
        eq02 = self.eq02
        triangle = self.triangle
        self.C_target = eq02[2]
        sin_brackets = VGroup(eq02[0], eq02[1], eq02[3])
        self.play(Write(sin_brackets))
        self.play(TransformFromCopy(self.angle_C_label,self.C_target))
        self.play(Write(eq02[4]))
        fraction02 = eq02[5]
        self.h_target02 = fraction02[0][0]

        self.b_target = fraction02[2][0]
        self.play(TransformFromCopy(self.h_label, self.h_target02))
        self.play(Write(eq02[5][1]))
        self.play(TransformFromCopy(self.side_b, self.b_target))

        self.play(FadeOut(self.right_trig))
        trig = VGroup(self.triangle,self.side_a,self.side_b,self.side_c,self.angle_A,self.angle_B,self.angle_C,self.angle_A_label,self.angle_B_label, self.angle_C_label,self.eq01, self.eq02,self.h_label,self.height,self.right_angle)
        self.play(
            trig.animate.shift(LEFT*2)
            )
    def thirdeq(self):
        eq01 =self.eq01
        eq02 = self.eq02

        sinBgrp = VGroup(eq01[0:4])
        sinCgrp = VGroup(eq02[0:4])
        
        hgrp = VGroup(self.h_target,self.h_target02)
        self.play(TransformFromCopy(hgrp,self.eq03[4]))
        self.play(Write(self.eq03[3]),Write(self.eq03[5]))
        self.play(
            TransformFromCopy(self.c_target,self.eq03[0],run_time = 2),
            TransformFromCopy(sinBgrp,self.eq03[2],run_time = 2),
            Write(self.eq03[1])
        )
        self.wait(1)
        self.play(
            TransformFromCopy(self.b_target,self.eq03[6],run_time = 2),
            TransformFromCopy(sinCgrp,self.eq03[8],run_time = 2),
            Write(self.eq03[7])
        )
        self.wait(2)
    

    def fourtheq(self):
        eq04 = self.eq04
        eq03 = self.eq03
        self.eqfrac01 = eq04[0]
        self.numerator_c = self.eqfrac01[0][0]
        self.sinC = VGroup(self.eqfrac01[2:])

        self.eqfrac02 = eq04[2]
        self.numerator_b = self.eqfrac02[0][0]
        self.sinB = VGroup(self.eqfrac02[2:])
        self.play(
            Write(eq04[0][1]),
            Write(eq04[1]),
            Write(eq04[2][1]),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(eq03[8], self.sinC),
            TransformFromCopy(eq03[2], self.sinB),
            run_time = 2.5
        )
        self.wait(1)
        self.play(
            TransformFromCopy(eq03[0],self.numerator_c),
            TransformFromCopy(eq03[6], self.numerator_b),
            run_time = 1.4
            )
        

    def proving_sin_rule(self):
        eq = self.eq

        self.play(
            Write(eq[0][1]),
            Write(eq[2][1]),
            Write(eq[4][1]),

            Write(eq[1]),
            Write(eq[3]),

        )

        self.play(
            Write(eq[0]),
            TransformFromCopy(self.numerator_c,eq[4][0][0]),
            TransformFromCopy(self.sinC,eq[4][2:]),
            TransformFromCopy(self.numerator_b,eq[2][0][0]),
            TransformFromCopy(self.sinB,eq[2][2:]),
            run_time = 2      
        )


        box = SurroundingRectangle(eq,color=WHITE,buff = 0.23)
        self.play(Create(box))
        self.wait(3)