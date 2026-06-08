from manim import * 

def op(self,introtext,introformula = None):
        title = Text(introtext).move_to(UP)
        self.play(Write(title))
        if introformula: 
            formula = MathTex(introformula).next_to(title,DOWN)
            self.play(Write(formula))   
        credit = Text("RickPhobia").next_to(title,DOWN, buff = 2)
        self.play(Write(credit))
        self.wait(1)
        fade_objects = [title]
        if introformula:
            fade_objects.append(formula)
        
        self.play(
            *[FadeOut(obj) for obj in fade_objects],
            credit.animate.scale(0.6).to_corner(DR),
        )