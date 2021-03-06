''' Tests for the span_range function in arrow.py, when exact is set to true. '''
import datetime
import arrow

def compare_intervals(interval1, interval2):
    ''' Compare two intervals to make sure they're the same. '''
    assert(len(interval1) == len(interval2))

    for i in range(0, len(interval1)):
        # print("out: ", interval1[i][0])
        # print("expected: ", interval2[i][0])
        assert(interval1[i][0] == interval2[i][0])
        # print("out: ", interval1[i][1])
        # print("expected: ", interval2[i][1])
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

    compare_intervals(interval, expected_interval)
    print('test3 passed!')

def test4():
    ''' Fifth test. Using the month frame spanning ~3 months. '''
    # should be January 31st 2018 at 5 pm
    begin = datetime.datetime(2018, 1, 31, 17)
    # should be April 5th 2018 at 3:45 pm
    end = datetime.datetime(2018, 4, 5, 15, 45)
    interval = arrow.Arrow.span_range('month', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 1, 31, 17), arrow.Arrow(2018, 3, 3, 16, 59, 59, 999999)),
                         (arrow.Arrow(2018, 3, 3, 17), arrow.Arrow(2018, 3, 31, 16, 59, 59, 999999)),
                         (arrow.Arrow(2018, 3, 31, 17), arrow.Arrow(2018, 4, 5, 15, 44, 59, 999999))]

    compare_intervals(interval, expected_interval)
    print('test4 passed!')

def test5():
    ''' Sixth test. Using the week frame spanning ~3 weeks. '''
    # should be March 25th 2018 at noon
    begin = datetime.datetime(2018, 3, 25, 12)
    # should be April 5th 2018 at 11 am
    end = datetime.datetime(2018, 4, 5, 11)
    interval = arrow.Arrow.span_range('week', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 3, 25, 12), arrow.Arrow(2018, 4, 1, 11, 59, 59, 999999)),
                         (arrow.Arrow(2018, 4, 1, 12), arrow.Arrow(2018, 4, 5, 10, 59, 59, 999999))]

    compare_intervals(interval, expected_interval)
    print('test5 passed!')

def test6():
    ''' Seventh test. Using the day frame spanning ~3 days. '''
    # should begin April 2nd at 10:10:10:10
    begin = datetime.datetime(2018, 4, 2, 10, 10, 10, 10)
    # should end April 5th at 16:14:53:99
    end = datetime.datetime(2018, 4, 5, 16, 14, 53, 99)
    interval = arrow.Arrow.span_range('day', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 4, 2, 10, 10, 10, 10), arrow.Arrow(2018, 4, 3, 10, 10, 10, 9)),
                         (arrow.Arrow(2018, 4, 3, 10, 10, 10, 10), arrow.Arrow(2018, 4, 4, 10, 10, 10, 9)),
                         (arrow.Arrow(2018, 4, 4, 10, 10, 10, 10), arrow.Arrow(2018, 4, 5, 10, 10, 10, 9)),
                         (arrow.Arrow(2018, 4, 5, 10, 10, 10, 10), arrow.Arrow(2018, 4, 5, 16, 14, 53, 98))]

    compare_intervals(interval, expected_interval)

    print('test6 passed!')

def test7():
    ''' Eighth test. Using the minute frame spanning ~3 minutes. '''
    # should begin April 12th at 16:18:03
    begin = datetime.datetime(2018, 4, 12, 16, 18, 3)
    # should end April 12th at 16:20:55
    end = datetime.datetime(2018, 4, 12, 16, 20, 55)
    interval = arrow.Arrow.span_range('minute', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 4, 12, 16, 18, 3), arrow.Arrow(2018, 4, 12, 16, 19, 2, 999999)),
                         (arrow.Arrow(2018, 4, 12, 16, 19, 3), arrow.Arrow(2018, 4, 12, 16, 20, 2, 999999)),
                         (arrow.Arrow(2018, 4, 12, 16, 20, 3), arrow.Arrow(2018, 4, 12, 16, 20, 54, 999999))]

    compare_intervals(interval, expected_interval)
    print('test7 passed!')

def test8():
    ''' Ninth test. Using the second frame spanning ~3 seconds. '''
    # should begin April 12th at 16:18:03:02
    begin = datetime.datetime(2018, 4, 12, 16, 18, 3, 2)
    # should end April 12th at 16:18:05:01
    end = datetime.datetime(2018, 4, 12, 16, 18, 5, 1)
    interval = arrow.Arrow.span_range('second', begin, end, None, None, True)

    expected_interval = [(arrow.Arrow(2018, 4, 12, 16, 18, 3, 2), arrow.Arrow(2018, 4, 12, 16, 18, 4, 1)),
                         (arrow.Arrow(2018, 4, 12, 16, 18, 4, 2), arrow.Arrow(2018, 4, 12, 16, 18, 5, 1))]

    compare_intervals(interval, expected_interval)
    print('test8 passed!')

test0()
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
