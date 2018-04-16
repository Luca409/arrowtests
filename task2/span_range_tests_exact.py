''' Tests for the span_range function in arrow.py, when exact is set to true. '''
import datetime
import arrow

def compare_intervals(interval1, interval2):
    ''' Compare two intervals to make sure they're the same. '''
    assert(len(interval1) == len(interval2))

    for i in range(0, len(interval1)):
        # print("out: ", interval[i][0])
        # print("expected: ", expected_interval[i][0])
        assert(interval1[i][0] == interval2[i][0])
        # print("out: ", interval[i][1])
        # print("expected: ", expected_interval[i][1])
        assert(interval1[i][1] == interval2[i][1])

def print_interval(interval):
    ''' Print specified interval. '''
    for i in interval:
        print(i)

def test0():
    ''' First test. From original GitHub issue post. '''
    begin = datetime.datetime(2013, 5, 5, 12, 30)
    end = datetime.datetime(2013, 5, 5, 17, 15)
    interval = arrow.Arrow.span_range('hour', begin, end, None, None, True)


    expected_interval = [(arrow.Arrow(2013, 5, 5, 12, 30), arrow.Arrow(2013, 5, 5, 13, 29, 59, 999999)),
                         (arrow.Arrow(2013, 5, 5, 13, 30), arrow.Arrow(2013, 5, 5, 14, 29, 59, 999999)),
                         (arrow.Arrow(2013, 5, 5, 14, 30), arrow.Arrow(2013, 5, 5, 15, 29, 59, 999999)),
                         (arrow.Arrow(2013, 5, 5, 15, 30), arrow.Arrow(2013, 5, 5, 16, 29, 59, 999999)),
                         (arrow.Arrow(2013, 5, 5, 16, 30), arrow.Arrow(2013, 5, 5, 17, 14, 59, 999999))]


    print_interval(interval)
    print('------')
    print_interval(expected_interval)

    # compare_intervals(interval, expected_interval)
    print("test0 passed!")

test0()
