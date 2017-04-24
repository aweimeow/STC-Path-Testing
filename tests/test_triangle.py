from STC_Path_Testing.triangle import triangle


class TestTriangleCoverageClass:
    """ C0 Coverage """
    def test_triangle_c0(self):
        assert triangle(5, 5, 10).type == "NOT TRIANGLE"
        assert triangle(10, 10, 10).type == "EQUALATERAL"
        assert triangle(13, 12, 5).type == "RIGHT TRIANGLE"
        assert triangle(10, 10, 5).type == "ISOSCELES"
        assert triangle(10, 9, 8).type == "SCALENE"

    def test_triangle_c1(self):
        assert triangle(0, 0, 0).type == "NOT TRIANGLE"
        assert triangle(5, 5, 12).type == "NOT TRIANGLE"
        assert triangle(20, 20, 20).type == "EQUALATERAL"
        assert triangle(12, 15, 9).type == "RIGHT TRIANGLE"
        assert triangle(100, 50, 100).type == "ISOSCELES"
        assert triangle(100, 102, 101).type == "SCALENE"

    def test_triangle_c2(self):
        """
        Because of Triangle Problem doesn't have a Loop
        so we don't have C2 Coverage Test
        """

    def test_triangle_mcdc(self):
        # MCDC: a == b && b == c, FF, FT, TF, TT
        assert triangle(2, 3, 4).type == "SCALENE"
        assert triangle(4, 5, 5).type == "ISOSCELES"
        assert triangle(5, 5, 4).type == "ISOSCELES"
        assert triangle(6, 6, 6).type == "EQUALATERAL"

        # MCDC: a != b && b == c, FF, FT, TF, TT
        # BTW, in here a, b, c will sorted
        assert triangle(5, 5, 6).type == "ISOSCELES"
        assert triangle(5, 5, 5).type == "EQUALATERAL"
        assert triangle(3, 5, 6).type == "SCALENE"
        assert triangle(5, 6, 6).type == "ISOSCELES"
