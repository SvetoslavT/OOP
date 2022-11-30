from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and not room.is_taken and room.capacity >= people:
                room.guests += people
                self.guests += people
                room.is_taken = True

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.guests = 0
                room.is_taken = False

    def status(self):

        taken = filter(lambda x: x.is_taken, self.rooms)
        free = filter(lambda x: not x.is_taken, self.rooms)
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Taken rooms: {', '.join([str(x.number) for x in taken])}\n" \
               f"Free rooms: {', '.join([str(x.number) for x in free])}"
