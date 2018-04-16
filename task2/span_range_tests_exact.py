''' Tests for the span_range function in arrow.py, when exact is set to true. '''
import datetime
import arrow

def compare_intervals(interval1, interval2):
    ''' Compare two intervals to make sure they're the same. '''
    assert(len(interval1) == len(interval2))

    for i in range(0, len(interval1)):
        assert(interval1[i][0] == interval2[i][0])
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

    compare_intervals(interval, expected_interval)
    print("test0 passed!")

def test1():
    ''' Second test. Just one hour to another. '''
    # should be april 5th 1 am
    begin = datetime.datetime(2018, 4, 5, 1)
    # should be april 5th 3 am
    end = datetime.datetime(2018, 4, 5, 3)
    interval = arrow.Arrow.span_range('hour', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 4, 5, 1), arrow.Arrow(2018, 4, 5, 1, 59, 59, 999999)),
                         (arrow.Arrow(2018, 4, 5, 2), arrow.Arrow(2018, 4, 5, 2, 59, 59, 999999))]

    compare_intervals(interval, expected_interval)
    print("test1 passed!")

def test2():
    ''' Third test. Using the hour frame spanning two different days. '''
    # should be april 5th 11:03 pm 
    begin = datetime.datetime(2018, 4, 5, 23, 3)
    # should be april 6th at 1:01 am
    end = datetime.datetime(2018, 4, 6, 1, 1)
    interval = arrow.Arrow.span_range('hour', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 4, 5, 23, 3), arrow.Arrow(2018, 4, 6, 0, 2, 59, 999999)),
                         (arrow.Arrow(2018, 4, 6, 0, 3), arrow.Arrow(2018, 4, 6, 1, 0, 59, 999999))]


    compare_intervals(interval, expected_interval)
    print("test2 passed!")

def test3():
    ''' Fourth test. Using the year frame spanning ~3 years. '''
    # should be april 5th 2016
    begin = datetime.datetime(2016, 4, 5)
    # should be april 1st 2018
    end = datetime.datetime(2018, 4, 1)
    interval = arrow.Arrow.span_range('year', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2016, 4, 5), arrow.Arrow(2017, 4, 4, 23, 59, 59, 999999)),
                         (arrow.Arrow(2017, 4, 5), arrow.Arrow(2018, 3, 31, 23, 59, 59, 999999))]

    print_interval(interval)
    print("*******")
    print(expected_interval)

    compare_intervals(interval, expected_interval)
    print('test3 passed!')

test0()
test1()
test2()
test3()
