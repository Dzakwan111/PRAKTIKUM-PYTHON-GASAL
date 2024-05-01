# import calendar

# cal = calendar.month(2008, 1)
# print("Dibawah ini adalah kalender:")
# print(cal) #python 3


from calendar import prcal
year = int(input("Enter year:"))
month = int(input("Enter month (1-12)"))

prcal(year, month)