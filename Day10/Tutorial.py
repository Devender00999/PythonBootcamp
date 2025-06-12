def is_leap_year(year):
   """Check if year is leap year or not"""
   if year % 4 == 0 and year % 100 != 0:
      return True
   elif year % 400 == 0:
      return True
   else:
      return False

print(is_leap_year(1700))
print(is_leap_year(1900))