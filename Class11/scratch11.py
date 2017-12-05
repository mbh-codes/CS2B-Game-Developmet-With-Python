list = [1,3,6,7,9]
oddslist = []
for i in list:
    print(i)
    if i % 2 == 1:
        oddslist.append(i)
    if len(oddslist) != 0:

        return random.choice(oddslist)
    if len(oddslist):
        return None

print(oddslist)
