from taipy import Gui
import redis

# Create a new Redis connection
r = redis.Redis(
    host='redis-12608.c85.us-east-1-2.ec2.cloud.redislabs.com',
    port=12608,
    password='1ZkRUlp5Pn5onmy5GkcKvBCXl9YcRAF3')

website = []

max = 0

nextExists = r.hexists(f'county{max}', 'rank')
print(nextExists)
while nextExists:
    max += 1
    nextExists = r.hexists(f'county{max}', 'rank')

for i in range(max):
    pyList = r.hgetall(f'county{i}')
    list = []
    list.append(pyList[b'county'].decode())
    list.append(int(pyList[b'population'].decode()))
    list.append(int(pyList[b'rank'].decode()))

    website.append(list)

stylekit = dict(color_background_light="#002569", color_paper_light="#FFD700")
md = """
# Kansas County Population
<|container container-bg|
<|{website}|chart|type=bar|>
|>
# <footer>Liam Hill, Christopher Taylor, Jacob Sears.</footer>
# <footer>Use for 2023 K-State Hackathon. Educational Purposes only. Data shown is not fact-checked</footer>
"""

Gui(page=md, css_file='kansaspop.css').run(dark_mode=False, stylekit=stylekit)
