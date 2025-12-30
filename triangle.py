from manim import *

class DrawTriangle(Scene):
    def construct(self):
        triangle = Polygon(
            [-2, -1, 0],
            [ 2, -1, 0],
            [ 0,  2, 0],
            color=WHITE
        )

        self.play(Create(triangle))
        self.wait(1)
    