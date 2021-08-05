#  python project for finding the location and service provider of Phone numbers

import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import timezone
# format  number = phonenumbers.parse(number.phone_number, number.region_code)

#  for finding country name of a specific number geocoder is a package for locating the address of a number
cntry_num = phonenumbers.parse(number, "+91")
print(geocoder.description_for_number(cntry_num, "en"))
from phonenumbers import carrier

service_num = phonenumbers.parse(number,"+91")
print(carrier.name_for_number(service_num, "en"))
timeZone = timezone.time_zones_for_number(service_num)
print("timeZone",{timeZone})


#  created by seikh sam
