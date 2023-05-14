# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


#print(add_time("11:06 PM", "2:02", "MoNDay"))

#Working tests
#print(add_time("3:30 PM", "2:12"))
#print(add_time("11:55 AM", "3:12"))
#print(add_time("9:15 PM", "5:30"))
#print(add_time("11:59 PM", "24:05", "Wednesday"))
#print(add_time("8:16 PM", "466:02", "tuesday"))
#print(add_time("2:59 AM", "24:00"))
#print(add_time("11:59 PM", "24:05"))
#print(add_time("8:16 PM", "466:02"))
#print(add_time("5:01 AM", "0:00"))
#print(add_time("3:30 PM", "2:12", "Monday"))

#Should be 12:05 PM
print(add_time("11:40 AM", "0:25"))


#expected = "2:59 AM, Sunday (next day)"
#print(add_time("2:59 AM", "24:00", "saturDay"))
#print(add_time("2:59 AM", "24:00"))



# Run unit tests automatically
main(module='test_module', exit=False)