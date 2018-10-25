# datetime
from datetime import datetime
print(datetime.now()) # 2018-10-25 12:15:26.557139


# setting date format
from datetime import datetime
 
date_time_str0 = '8-10-2018 11:52:40'
date_time_str1 = 'Jun 28 2018  7:40AM'
date_time_str2 = 'September 18, 2017, 22:19:55'
date_time_str3 = 'Sun,05/12/99,12:30PM'
date_time_str4 = '2018-03-12T10:12:45Z'
 
date_time_obj0 = datetime.strptime(date_time_str0, '%d-%m-%Y %H:%M:%S')
date_time_obj1 = datetime.strptime(date_time_str1, '%b %d %Y %I:%M%p')
date_time_obj2 = datetime.strptime(date_time_str2, '%B %d, %Y, %H:%M:%S')
date_time_obj3 = datetime.strptime(date_time_str3, '%a,%d/%m/%y,%I:%M%p')
date_time_obj4 = datetime.strptime(date_time_str4, '%Y-%m-%dT%H:%M:%SZ')
 
print('For Time0   Date:',date_time_obj0.date(), 'Time:', date_time_obj0.time()) # ('Time:', datetime.time(11, 52, 40))
print('For Time1   Date:',date_time_obj1.date(), 'Time:', date_time_obj1.time()) # ('Time:', datetime.time(7, 40))
print('For Time2   Date:',date_time_obj2.date(), 'Time:', date_time_obj2.time()) # ('Time:', datetime.time(22, 19, 55))
print('For Time3   Date:',date_time_obj3.date(), 'Time:', date_time_obj3.time()) # ('Time:', datetime.time(12, 30))
print('For Time4   Date:',date_time_obj4.date(), 'Time:', date_time_obj4.time()) # ('Time:', datetime.time(10, 12, 45))

