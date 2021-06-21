from gps import gps_read

def test_gps_read() -> None:
    """
    test for gps_read function

    :return: none
    """
    t0 = 1624199100.0
    T = 3650
    tle = ['1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991','2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482']

    expected_e_r_v = (1, (5416.865622844231, -3782.384041964031, 1552.3436001598536), (1.6869914192846271, 4.78070532238271, 5.751683834302403))

    assert gps_read(t0,T,tle) == expected_e_r_v,"the function gps_read does not match the expected output"

    
test_gps_read()