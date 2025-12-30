from manim import *

class Bezier(Scene):
    def construct(self):
        cp_1 = Dot([-4, -2, 0])
        cp_2 = Dot([-3, 3, 0])
        cp_3 = Dot([3, -3, 0])
        cp_4 = Dot([4, 3, 0])

        line_A_1 = Line(cp_1.get_center(), cp_2.get_center()).set_color(WHITE)
        line_A_2 = Line(cp_2.get_center(), cp_3.get_center()).set_color(WHITE)
        line_A_3 = Line(cp_3.get_center(), cp_4.get_center()).set_color(WHITE)

        self.play(FadeIn(cp_1), FadeIn(cp_2), FadeIn(cp_3), FadeIn(cp_4), run_time=1)
        self.play(Create(line_A_1), Create(line_A_2), Create(line_A_3), run_time=1)

        t = ValueTracker(0)

        lerp_1 = Dot(color=ORANGE)
        lerp_2 = Dot(color=ORANGE)
        lerp_3 = Dot(color=ORANGE)

        lerp_1.add_updater(lambda d: d.move_to(line_A_1.point_from_proportion(t.get_value())))
        lerp_2.add_updater(lambda d: d.move_to(line_A_2.point_from_proportion(t.get_value())))
        lerp_3.add_updater(lambda d: d.move_to(line_A_3.point_from_proportion(t.get_value())))

        self.add(line_A_1, lerp_1, line_A_2, lerp_2, line_A_3, lerp_3)

        line_B_1 = always_redraw(lambda: Line(lerp_1.get_center(), lerp_2.get_center(), color=ORANGE))
        line_B_2 = always_redraw(lambda: Line(lerp_2.get_center(), lerp_3.get_center(), color=ORANGE))

        self.add(line_B_1, line_B_2)
        
        lerp_B_1 = Dot(color=BLUE)
        lerp_B_2 = Dot(color=BLUE)
        
        lerp_B_1.add_updater(lambda d: d.move_to(line_B_1.point_from_proportion(t.get_value())))
        lerp_B_2.add_updater(lambda d: d.move_to(line_B_2.point_from_proportion(t.get_value())))
        
        self.add(lerp_B_1, lerp_B_2)

        line_C = always_redraw(lambda: Line(lerp_B_1.get_center(), lerp_B_2.get_center(), color=BLUE))
        self.add(line_C)

        lerp_C = Dot(color=WHITE)
        lerp_C.add_updater(lambda d: d.move_to(line_C.point_from_proportion(t.get_value())))

        self.add(lerp_C)

        curve = TracedPath(lerp_C.get_center, stroke_color=WHITE, stroke_width=4)
        self.add(curve)

        self.play(t.animate.set_value(1), run_time=2, rate_func=linear)
        self.wait()