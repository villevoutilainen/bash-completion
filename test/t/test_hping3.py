import pytest


class Test(object):

    @pytest.mark.complete("hping3 ")
    def test_(self, completion):
        assert completion.list