# Write a Pandas program to create
# a) Date time object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# t) Time from a date time.
# g) Current local time.
import pandas as pd

dataa = pd.Timestamp("2012-01-15")
print("a) Jan 15 2012:", dataa)

datab = pd.Timestamp("2022-01-15 21:20:00")
print("b) Specific date and time (9:20 pm):", datab)

datac = pd.Timestamp.now()
print("c) Local date and time:", datac)

datad = pd.to_datetime("2012-01-15").date()
print("d) Date without time:", datad)

currentdate = pd.Timestamp.now().date()
print("e) Current date:", currentdate)

timefromdate = datab.time()
print("t) Time from datetime:", timefromdate)

currentdate = pd.Timestamp.now().time()
print("g) Current local time:", currentdate)
