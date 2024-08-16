from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your phone number (including country code, eg:+123432560):")
phone = phonenumbers.parse(number,"US")
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)

