import pytest


class TestPerl(object):

    @pytest.mark.complete("perl ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -e ")
    def test_2(self, completion):
        assert not completion.list

    @pytest.mark.complete("perl -V:install")
    def test_3(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -V::install")
    def test_4(self, completion):
        assert completion.list

    # Assume File::Spec and friends are always installed

    @pytest.mark.complete("perl -MFile")
    def test_5(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -MFile::Sp")
    def test_6(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -MFile::Spec::Func")
    def test_7(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -M-File")
    def test_8(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -m-File::")
    def test_9(self, completion):
        assert completion.list

    @pytest.mark.complete("perl -")
    def test_10(self, completion):
        assert completion.list

    @pytest.mark.complete("perl foo shared/default/f")
    def test_11(self, completion):
        """Second arg should complete files+dirs."""
        assert completion.list == "foo foo.d/".split()

    @pytest.mark.complete("perl -Ishared/default/")
    def test_12(self, completion):
        """-I without space should complete dirs."""
        assert completion.list == ["bar bar.d/", "foo.d/"]

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("perl -I shared/default/")
    def test_13(self, completion):
        """-I with space should complete dirs."""
        assert completion.list == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("perl -xshared/default/b")
    def test_14(self, completion):
        """-x without space should complete dirs."""
        assert completion.list == ["-xshared/default/bar bar.d/"]

    @pytest.mark.complete("perl -x shared/default/b")
    def test_15(self, completion):
        """-x with space should complete dirs."""
        assert completion.list == ["shared/default/bar bar.d/"]
