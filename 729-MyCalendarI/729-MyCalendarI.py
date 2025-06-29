# Last updated: 6/29/2025, 12:33:45 AM
class MyCalendar:

    def __init__(self):
        self.bookings = {}

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.bookings.items():
            # If it overlaps
            if not(startTime >= e or endTime <= s):
                return False
        self.bookings[startTime] = endTime
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)