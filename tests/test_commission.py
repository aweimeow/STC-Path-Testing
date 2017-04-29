from STC_Path_Testing.commission import Commission


class TestCommissionCoverageClass:
    """
    Valid Value Range:
    1 <= locks <= 70
    1 <= stocks <= 80
    1 <= barrels <= 90
    """

    def test_commission_c0(self):
        assert Commission(-1, 1, 1).bonus == "Terminate"
        assert Commission(50, 50, 100).bonus == "Invalid"
        assert Commission(70, 80, 90).bonus == 1420
        assert Commission(20, 10, 4).bonus == 145
        assert Commission(4, 5, 4).bonus == 43

    def test_commission_c1(self):
        # C1 includes C0
        assert Commission(0, 50, 50).bonus == "Invalid"
        assert Commission(50, 0, 50).bonus == "Invalid"
        assert Commission(50, 50, 0).bonus == "Invalid"

    def test_commission_c2(self):
        # Commission Problem without loop, no c2 test
        pass

    def test_commission_mcdc(self):
        # According to Flow Chart, we dont have Multi-Condition
        pass
