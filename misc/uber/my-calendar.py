# 729 My Calendar I
# https://leetcode.com/problems/my-calendar-i/description/

# ou are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

import bisect

class MyCalendar:

    def __init__(self):
        self.cal = []
        

    def book(self, startTime: int, endTime: int) -> bool:

        # find the first element that is larget than startTime in self.cal
        if not self.cal:
              self.cal.append((startTime, endTime))
              return True

        idx = bisect.bisect_left(self.cal, (startTime, endTime))
        if idx != 0 and self.cal[idx-1][1] > startTime:
                return False
        if idx < len(self.cal) and self.cal[idx][0] < endTime:
                return False

        self.cal.insert(idx, (startTime, endTime))

        return True
    
# To test the `MyCalendar` class, we can create an instance of it and call the `book` method with various start and end times to see if the events can be booked without causing a double booking.
# Here is a simple test script:
# Test script
myCalendar = MyCalendar()
assert myCalendar.book(10, 20) == True  # return True
assert myCalendar.book(15, 25) == False # return False, It can not be booked because time 15 is already booked by another event.
assert myCalendar.book(20, 30) == True  # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.\\

myCalendar = MyCalendar()
assert myCalendar.book(47,50) == True
assert myCalendar.book(33,41) == True
assert myCalendar.book(39,45) == False
assert myCalendar.book(33,42) == False
assert myCalendar.book(25,32) == True
assert myCalendar.book(26,35) == False
assert myCalendar.book(19,25) == True
assert myCalendar.book(3,8) == True
assert myCalendar.book(8,13) == True
assert myCalendar.book(18,27) == False