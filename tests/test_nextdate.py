from STC_Path_Testing.nextdate import Date


class TestNextDateCoverageClass:
    """
    Valid Value Range:
    1812 <= year <= 2012
    1 <= month <= 12
    1 <= day <= 31
    """

    def test_nextdate_c0(self):
        assert Date(1811, 0, 0).nextdate == "INVALID"
        assert Date(2015, 12, 31).nextdate == "2016, 1, 1"
        assert Date(2016, 2, 29).nextdate == "2016, 3, 1"
        assert Date(2016, 3, 1).nextdate == "2016, 3, 2"

    def test_nextdate_c1(self):
        assert Date(2020, 13, 13).nextdate == "INVALID"
        assert Date(2015, 12, 31).nextdate == "2016, 1, 1"
        assert Date(2015, 1, 31).nextdate == "2015, 2, 1"
        assert Date(2015, 4, 30).nextdate == "2015, 5, 1"
        assert Date(2015, 2, 28).nextdate == "2015, 3, 1"
        assert Date(2012, 2, 29).nextdate == "2013, 3, 1"
        assert Date(2015, 5, 1).nextdate == "2015, 5, 2"

    def test_nextdate_c2(self):
        """
        Because of NextDate Problem doesn't have a Loop
        so we don't have C2 Coverage Test
        """

    def test_nextdate_mcdc(self):
        # MCDC: action to Year + 1, Month = 1, Day = 1
        assert Date(2013, 12, 31).nextdate == "2014, 1, 1"
        assert Date(2014, 12, 31).nextdate == "2015, 1, 1"

        # MCDC: action to Year, Month + 1, Day = 1
        assert Date(2013, 1, 31).nextdate == "2013, 2, 1"
        assert Date(2013, 4, 30).nextdate == "2013, 5, 1"
        assert Date(2014, 2, 28).nextdate == "2014, 3, 1"
        assert Date(2012, 2, 29).nextdate == "2012, 3, 1"

        # MCDC: action to Year, Month, Day + 1
        assert Date(2015, 1, 1).nextdate == "2015, 1, 2"
        assert Date(2015, 2, 1).nextdate == "2015, 2, 2"
