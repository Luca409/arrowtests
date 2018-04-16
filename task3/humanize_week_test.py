''' Tests for the humanize function in arrow.py, when time is set to week. '''
import arrow

def test0():
    ''' Testing 0 weeks ago. '''
	# the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

	# less than a week ago
    week_ago = arrow.Arrow(2018, 4, 12)

    assert(week_ago.humanize(right_now, granularity="week") == "0 weeks ago")
    print("test0 passed!!")

def test1():
    ''' Testing in 0 weeks. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # in less than a week
    week_to = arrow.Arrow(2018, 4, 20)

    assert(week_to.humanize(right_now, granularity="week") == "in 0 weeks")
    print("test1 passed!!")

def test2():
    ''' Testing 1 week ago. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # less than a week ago
    week_ago = arrow.Arrow(2018, 4, 9)

    assert(week_ago.humanize(right_now, granularity="week") == "a week ago")
    print("test2 passed!!")

def test3():
    ''' Testing in 1 week. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # in less than a week
    week_to = arrow.Arrow(2018, 4, 23)

    assert(week_to.humanize(right_now, granularity="week") == "in a week")
    print("test3 passed!!")

def test4():
    ''' Testing 12 weeks ago. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # less than a week ago
    week_ago = arrow.Arrow(2018, 1, 22)

    assert(week_ago.humanize(right_now, granularity="week") == "12 weeks ago")
    print("test4 passed!!")

def test5():
    ''' Testing in 12 weeks. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # in less than a week
    week_to = arrow.Arrow(2018, 7, 9)

    assert(week_to.humanize(right_now, granularity="week") == "in 12 weeks")
    print("test5 passed!!")

def test6():
    ''' Testing 52 weeks ago. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # less than a week ago
    week_ago = arrow.Arrow(2017, 4, 16)

    assert(week_ago.humanize(right_now, granularity="week") == "52 weeks ago")
    print("test6 passed!!")

def test7():
    ''' Testing in 52 weeks. '''
    # the time when this code was written
    right_now = arrow.Arrow(2018, 4, 16)

    # in less than a week
    week_to = arrow.Arrow(2019, 4, 16)

    assert(week_to.humanize(right_now, granularity="week") == "in 52 weeks")
    print("test7 passed!!")

test0()
test1()
test2()
test3()
test4()
test5()
test6()
test7()
