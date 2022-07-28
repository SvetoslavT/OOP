class Time:
    max_hour = 23
    max_minute = 59
    max_second = 59

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, new_hour, new_minute, new_second):
        self.hour = new_hour
        self.minute = new_minute
        self.second = new_second

    def get_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def next_second(self):
        if self.second == Time.max_second:
            self.second = 0
            self.minute += 1
        else:
            self.second += 1
        if self.minute >= Time.max_minute:
            self.minute = 0
            self.hour += 1

        if self.hour >= Time.max_hour:
            self.hour = 0

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
