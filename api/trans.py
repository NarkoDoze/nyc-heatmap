import json
import datetime

with open('treecoor.json') as f:
    coor = json.load(f)

with open('before_up.json', 'r') as f:
    dic = json.load(f)

start_date = datetime.datetime(2016, 1, 1)
end_date = datetime.datetime(2016, 1, 2)

d = start_date
delta = datetime.timedelta(days=1)
result = []

while d <= end_date:
    dstr = d.strftime('%Y%m%d')
    for t in range(0, 23*4):
        for data in dic[dstr]:
            start = data['start']
            end = data['end']
            speed = data['speed'][t]
            if speed < 20:
                result.append({
                    'location': {
                        'start': coor[start],
                        'end': coor[end],
                    },
                    'speed': speed,
                    'date': datetime.datetime(d.year, d.month, d.day, int(t / 4), t % 4).isoformat()
                })
    d += delta

print(result)
