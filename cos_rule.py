from manim import *



import intro 
class CosRuleProof(Scene):
    def construct(self):
        intro.op(self,"Proving Cos Rule",introformula=MathTex("c^2 = a^2 + b^2 - 2ab\cos(C)"))
        self.drawing_triangles_angles()
        self.firsteq()
        self.secondeq()
        self.sfeq()
        self.thirdeq()
        self.fourtheq()
        self.fiftheq()
        # self.angleeq()
        self.proving_cos_rule()


        
    def drawing_triangles_angles(self):
        A = np.array([1, 2, 0])
        B = np.array([-5, -1, 0])
        C = np.array([3, -1, 0])
        triangle = Polygon(A, B, C, color=WHITE)
        
        self.play(Create(triangle))

        angle_A = Angle(Line(B,A), Line(C,A), radius=0.6, quadrant= (-1,-1),other_angle=False, color=BLUE)
        angle_B = Angle(Line(A,B), Line(C,B), radius= 1.4, quadrant= (-1,-1), other_angle=True, color = BLUE)
        angle_C = Angle(Line(A,C), Line(B,C), radius=1.2,quadrant= (-1,-1), other_angle=False, color=BLUE)

        angle_A_label = MathTex("A").move_to(angle_A.get_center() + 0.5*DOWN)
        angle_B_label = MathTex("B").move_to(angle_B.get_center() + 0.1*UR + 0.2*RIGHT)
        angle_C_label = MathTex("C").move_to(angle_C.get_center() + 0.3*UL)
        self.play(Create(angle_A),Write(angle_A_label))
        self.play(Create(angle_B),Write(angle_B_label))
        self.play(Create(angle_C),Write(angle_C_label))
        # Add labels for sides
        side_a = MathTex("a").move_to((B + C)/2 + DOWN*0.5).scale(1.5)
        side_ax = MathTex("a-x").next_to(side_a, LEFT).scale(1.5)
        side_x = MathTex("x").next_to(side_a,RIGHT,buff=2.4).scale(1.5)
        sidegrp = VGroup(side_ax,side_x)
        side_b = MathTex("b").move_to((A + C)/2 + RIGHT*0.5).scale(1.5)
        side_c = MathTex("c").move_to((A + B)/2 + 0.4+  LEFT*0.5).scale(1.5)
        self.play(Write(side_a), Write(side_b), Write(side_c))
        self.wait(2)

        foot = np.array([1, -1, 0])
        height = DashedLine(A, foot, color=YELLOW)
        right_angle = RightAngle(Line(C, foot), Line(foot, A), length=0.3)
        self.play(Create(height), Create(right_angle))

        h_label = MathTex("h").next_to(height, LEFT)
        self.play(Write(h_label))
        
        self.A, self.B, self.C = A, B, C
        self.foot = foot
        self.h_label = h_label
        self.sides = side_a,side_ax,side_x,side_b,side_c,sidegrp
        self.triangle = triangle 
        self.angles = angle_A, angle_B, angle_C
        self.angles_labels = angle_A_label, angle_B_label, angle_C_label, height,right_angle

        left_trig = Polygon(A,B,foot,fill_color = TEAL_A, fill_opacity = 0.5, stroke_color =WHITE )
        right_trig = Polygon(A,C,foot,fill_color = TEAL_E,fill_opacity = 0.5, stroke_color =WHITE)
        self.trigs = left_trig,right_trig
        eq01 = MathTex("(a-x)^2" ,"+", "h^2", "=", "c^2").next_to(side_ax,DOWN).shift(LEFT*1)
        eq02 = MathTex("x^2" ,"+", "h^2", "=", "b^2").next_to(eq01,RIGHT,buff = 1)
        eq011 = MathTex("(a-x)^2","-c^2", "=", "-h^2").next_to(eq01,DOWN)
        eq021 = MathTex("x^2" ,"-b^2", "=", "-h^2").next_to(eq02,DOWN)
        eq03 = MathTex("x^2","-b^2","=","-h^2","=","(a-x)^2","-c^2",).to_corner(UR,buff = 0.3)
        eq04 = MathTex("x^2","-b^2","=","a^2","-2ax","+","x^2","-c^2" ).next_to(eq03,DOWN)
        seq04 = MathTex("-b^2","=","a^2","-2ax","-c^2" ).next_to(eq03,DOWN)
        eq05 = MathTex("c^2", "=", "a^2","+b^2" ,"-2ax").next_to(seq04,DOWN)
        coseq = MathTex(r"\cos","(","C",")","=",r"\frac{x}{b}").next_to(eq01,DOWN,buff = 0.7).scale(0.8)
        coseq01 = MathTex("x","=","b",r"\cdot",r"\cos(C)" ).next_to(coseq,RIGHT,buff = 1.5)
        eq =  MathTex("c^2","="," a^2","+b^2", "-2a","b\cos(C)").next_to(eq05,DOWN,buff = 1.3).shift(RIGHT*0.4)


        self.eq01 = eq01 
        self.eq02 = eq02 
        self.eq011 = eq011
        self.eq021 = eq021 
        self.eq03 = eq03 
        self.eq04 = eq04 
        self.eq05 = eq05 
        self.coseq = coseq
        self.coseq01 = coseq01
        self.eq = eq
        




    def firsteq(self):
        eq01 = self.eq01
        left_trig, right_trig = self.trigs
        side_a,side_ax,side_x,side_b,side_c,sidegrp = self.sides
        A,B,C = self.A, self.B, self.C
        foot = self.foot
        h_label = self.h_label
        self.play(side_a.animate.shift(DR*1.3))

        self.play(TransformFromCopy(side_a,sidegrp))
        self.play(FadeOut(side_a))
        # self.play(angle_C_label.set_color(YELLOW))
        self.play(FadeIn(left_trig))

        
        self.wait(1.5)
        
        self.play(TransformFromCopy(side_ax,eq01[0]))
        self.play(Write(eq01[1]))
        self.play(TransformFromCopy(h_label,eq01[2]))
        self.play(Write(eq01[3]))
        self.play(TransformFromCopy(side_c,eq01[4]))

        self.wait(1)


        self.play(FadeOut(left_trig))
        self.wait(1.5)
        self.play(FadeIn(right_trig))


    def secondeq(self):
        eq02 = self.eq02
        side_a,side_ax,side_x,side_b,side_c,sidegrp = self.sides
        A,B,C = self.A, self.B, self.C
        h_label = self.h_label
        left_trig, right_trig = self.trigs
        self.play(TransformFromCopy(side_x,eq02[0]))
        self.play(Write(eq02[1]))
        self.play(TransformFromCopy(h_label,eq02[2]))
        self.play(Write(eq02[3]))
        self.play(TransformFromCopy(side_b,eq02[4]))
        self.play(FadeOut(right_trig))

        self.eq02 = eq02
    def sfeq(self):
        eq011 = self.eq011
        eq021 = self.eq021
        side_a,side_ax,side_x,side_b,side_c,sidegrp = self.sides
        A,B,C = self.A, self.B, self.C
        foot = self.foot
        h_label = self.h_label
        triangle = self.triangle
        angle_A, angle_B, angle_C = self.angles
        angle_A_label, angle_B_label, angle_C_label,height,right_angle = self.angles_labels
        eq01 = self.eq01
        eq02 = self.eq02
    
        self.play(
            TransformFromCopy(eq01[0],eq011[0]),
            TransformFromCopy(eq01[3],eq011[2]),
            TransformFromCopy(eq01[2],eq011[3]),
            TransformFromCopy(eq01[4],eq011[1]),
            run_time = 1.5
        )
        

    
        self.play(
            TransformFromCopy(eq02[0],eq021[0]),
            TransformFromCopy(eq02[3],eq021[2]),
            TransformFromCopy(eq02[2],eq021[3]),
            TransformFromCopy(eq02[4],eq021[1]),
            run_time = 1.5

        )
    
        trig = VGroup(triangle,eq021,eq011,side_ax,side_x,side_b,side_c,angle_A,angle_B,angle_C,angle_A_label,angle_B_label, angle_C_label,eq01, eq02,h_label,height,right_angle)
        self.play(
            trig.animate.shift(LEFT*2)
            
        )

    def thirdeq(self):
        eq03 = self.eq03
        eq011 = self.eq011
        eq021 = self.eq021
        hgrp = VGroup(eq011[3],eq021[3])
        equalgrp = VGroup(eq03[2],eq03[4])
        self.play(TransformFromCopy(hgrp,eq03[3]),run_time = 1.3)
        self.play(
            TransformFromCopy(eq011[2],eq03[2]),
            TransformFromCopy(eq021[2],eq03[4])
        )
        
        self.wait(1)
        self.play(
            TransformFromCopy(eq021[0],eq03[0]),
            TransformFromCopy(eq021[1],eq03[1]),
            run_time = 1.5
        )
        self.play(TransformFromCopy(eq011[0],eq03[5]),
            TransformFromCopy(eq011[1],eq03[6]),
            run_time = 1.5
        )

        self.wait(2)
    def fourtheq(self):
        eq03 = self.eq03
        eq04 = self.eq04
        equalgrp = VGroup(eq03[2],eq03[4])


        expandgrp = VGroup(eq04[3:7])
        self.play(
            TransformFromCopy(eq03[0],eq04[0]),
            TransformFromCopy(eq03[1],eq04[1]),
            TransformFromCopy(equalgrp,eq04[2])
        )
        self.wait(1.2)
        self.play(
            TransformFromCopy(eq03[5],expandgrp),
            TransformFromCopy(eq03[6],eq04[7]),
            run_time = 2
        )
        cross1 = Line(
            eq04[0].get_corner(UR),
            eq04[0].get_corner(DL),
            color = WHITE
        )
        cross2 = Line(
            eq04[6].get_corner(UR),
            eq04[6].get_corner(DL),
            color = WHITE
        )
        self.play(Create(cross1),Create(cross2))
        self.wait(1)
        self.play(
            FadeOut(eq04[0]),
            FadeOut(eq04[6]),
            FadeOut(cross1),
            FadeOut(cross2),
        )
        self.wait(2)
    def fiftheq(self):
        eq04 = self.eq04
        eq05 = self.eq05
        self.play(
            TransformFromCopy(eq04[7],eq05[0]))
        self.play(TransformFromCopy(eq04[2],eq05[1]))
        self.play(TransformFromCopy(eq04[3],eq05[2]))
        self.play(TransformFromCopy(eq04[1],eq05[3]))
        self.play(TransformFromCopy(eq04[4],eq05[4]))
        
    def angleeq(self):
        angle_A, angle_B, angle_C = self.angles
        angle_A_label, angle_B_label, angle_C_label,height,right_angle = self.angles_labels
        side_a,side_ax,side_x,side_b,side_c,sidegrp = self.sides

        left_trig, right_trig = self.trigs
        eq01 = self.eq01

        coseq = MathTex(r"\cos","(","C",")","=",r"\frac{x}{b}").next_to(eq01,DOWN,buff = 0.7).scale(0.8)
        coscgrp = VGroup(coseq[0:4])
        cosbracket = VGroup(coseq[0],coseq[1],coseq[3])
    
        right_trig.shift(LEFT*2)
        self.play(FadeIn(right_trig))
        self.play(Write(cosbracket))
        self.play(TransformFromCopy(angle_C_label,coseq[2]))
        self.play(Write(coseq[4]))
        self.play(TransformFromCopy(side_x,coseq[5][0][0]))
        self.play(Write(coseq[5][1][0]))
        self.play(TransformFromCopy(side_b,coseq[5][2][0]))
        self.play(FadeOut(right_trig))

        coseq01 = MathTex("x","=","b",r"\cdot",r"\cos(C)" ).next_to(coseq,RIGHT,buff = 1.5)
        cosgrp = VGroup(coseq01[3],coseq01[4])
        bcosgrp = VGroup(coseq01[2],coseq01[3],coseq01[4])
        self.play(TransformFromCopy(coseq[5][0][0],coseq01[0]))

        
        self.play(TransformFromCopy(coseq[4],coseq01[1]))
        self.play(TransformFromCopy(coseq[5][2][0],coseq01[2]))
        self.play(TransformFromCopy(coscgrp,cosgrp))

    def proving_cos_rule(self):
        eq = self.eq 
        eq05 = self.eq05
        coseq = self.coseq
        coseq01 = self.coseq01

        downgrp = VGroup(eq05[0:4])
        agrp = VGroup(eq05[4][0:3])

        downgrp01 = VGroup(eq[0:4])
        cosgrp = VGroup(coseq01[3],coseq01[4])
        bcosgrp = VGroup(coseq01[2],coseq01[3],coseq01[4])
        self.play(TransformFromCopy(downgrp,downgrp01))
        self.play(TransformFromCopy(agrp,eq[4]))
        self.play(TransformFromCopy(eq05[4][3],coseq01[0]))
        self.play(TransformFromCopy(bcosgrp,eq[5]))


        box = SurroundingRectangle(eq,color=WHITE,buff = 0.23)
        self.play(Create(box))
        self.wait(3)