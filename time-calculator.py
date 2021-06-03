def add_time(s, d, date = None):
    start = s.replace(":", " ").split()
    duration = d.replace(":", " ").split()

    hrs = int(start[0]) + int(duration[0])
    mins = int(start[1]) + int(duration[1])
    sfix = start[2]

    hrs += mins//60
    mins = mins % 60
    days = hrs // 24

    if sfix == "PM": hrs += 12
    sfix = "PM" if hrs % 24 >= 12 else "AM"
    hrs = (hrs - 1 % 12) + 1

    if date != None:
        date = date.capitalize()
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        date = week[(week.index(date) + days) % 7]

    output = ("{hrs}:{mins} {sfix}{date} {days}").format(
        hrs = hrs, mins = '{:02}'.format(mins), sfix = sfix,
        date = '' if date == None else ', ' + date,
        days = '' if days == 0 else '(next day)' if days == 1 else ' days later)')

    return output.rstrip()
