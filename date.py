date = '2022-01-17'

def compute_tomorrow(date):
    year=date[0:4]
    month=date[5:7]
    day=int(date[-2:])
    return year + '-' + month + '-' + str(day + 1)


print('Next class is on ',compute_tomorrow(date))


def feet2meter(feet):
     meter=0.3048*feet  
     return(meter)

print('200 feet in meters =', feet2meter(200))