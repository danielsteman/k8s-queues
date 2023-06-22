from tasks import work

for _ in len(range(10)):
    work.delay()
