from simple_interest import simple_interest

def test_simple_interest_pos():
    assert simple_interest(20000,8,12) ==19200
def test_case2():
    assert simple_interest(2500, 7.5, 3) == 562.5

    