from datetime import datetime

class Task:
    def __init__(self, task: str = '', startdate: datetime = None, enddate: datetime = None):
        self.task = task
        self.startdate = startdate
        self.enddate = enddate

    @property
    def daystaken(self):
        if self.enddate:
            return (self.enddate - self.startdate).days
        else:
            return None

    @property
    def formated_startdate(self):
        return self.startdate.strftime("%d-%m-%Y")

    @property
    def formated_enddate(self):
        if self.enddate:
            return self.enddate.strftime("%d-%m-%Y")
        else:
            return ''

    def __str__(self):
        return f"{self.task} - {self.formated_startdate} - {self.formated_enddate} - {self.daystaken}"


f = open("tasks.txt", "rt")
tasks = []
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue  # ignore line

    t = Task()
    try:
        t.task = parts[0]
        t.startdate = datetime.strptime(parts[1], "%d-%m-%Y")
        if len(parts) > 2:  # end date is present
            t.enddate = datetime.strptime(parts[2], "%d-%m-%Y")

        tasks.append(t)
    except Exception as ex:
        #print('Error:', ex)
        pass

f.close()

for t in sorted(tasks, key = lambda t: t.startdate):
    print(t)
