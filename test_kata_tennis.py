from kata_tennis import switch_score

def test_should_return_switched_score():
    a = 3
    actual = switch_score(a)
    expected = "Quarante"
    assert actual == expected

def test_should_return_none_score():
    a = 4
    actual = switch_score(a)
    expected = None
    assert actual == expected