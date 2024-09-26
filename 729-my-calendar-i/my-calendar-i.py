class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        if self.schedule == []:
            self.schedule.append([start, end])
            return True
        else:
            # print(self.schedule)
            # print(start, end)
            for i in self.schedule:
                if i[0] <= start < i[1] or i[0] < end <= i[1]:
                    return False
                if start < i[0] < end or start < i[1] < end:
                    return False
        self.schedule.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)