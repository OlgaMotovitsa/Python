

import pytest
from task2 import remove_char

def test_no_change():
    assert remove_char("qwer") == "qwer"

def test_result_is_str():
    assert isinstance(remove_char("qwer"), str)

def test_in():
    assert " " in remove_char("qw er")

def test_nonenon():
    assert remove_char("qewr") is not None

if __name__ == '__main__':
    pytest.main(["Seminars/Seminar14/test_pytest.py"])

# ввести в терминал локал
# pytest Seminars/Seminar14/test_pytest.py -v
