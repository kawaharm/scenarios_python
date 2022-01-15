'''
vaccine site array object that has a wait time array 
=> map to average the wait time.and add to object 
=> filter out the sites with that have average wait time above a certain amount
'''

wait_time = [20, 10, 15, 7, 30, 45, 60, 5, 4]
wait_time2 = ['20', '10', '15', '7', '30', '45', '60', '5', '4']
clinic = [
    'Hallingford', 'Washington', 'Griff Hospital', 'Masonford', 'Jacksonville',
    'Beurotown',  'Belltown', 'Lickenville', 'Whatsitburg'
    ]

string_wait = str(wait_time)

print("String Test", string_wait)
# ==========Map========== #

result1 = map(lambda x, y: x + " minutes at " + y, wait_time2, clinic)
print("Result 1", list(result1))

# def combine_array(arr1, arr2):
    

# ==========Filter========== #

# def too_long(time):
#     if time > 30:
#         return "Wait time longer than 30 minutes"
#     else: 
#         return "Short wait time"

def short_time(time):
    if time < 30:
        return True
    else: 
        return False

def long_time(time):
    if time >= 30:
        return True
    else: 
        return False

long_wait = list(filter(long_time, wait_time))
short_wait = list(filter(short_time, wait_time))

# print("Long Wait Time", long_wait)
# print("Short Wait Time", short_wait)