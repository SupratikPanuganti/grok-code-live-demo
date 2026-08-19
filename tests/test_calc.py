from calc import uptime_pct

def test_uptime_pct():
    assert uptime_pct(99, 100) == 99.0
