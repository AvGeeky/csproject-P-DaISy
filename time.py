from datetime import date

today = date.today()
d1 = today.strftime("%m/%d/%y")
today = date.today()
d1 = today.strftime("%m/%d/%y")
cdlist=d1.split("/")
cdate=cdlist[1]
cyear=cdlist[2]
cmonth=cdlist[0]
print(cdate,type(cdate))
print(cyear,type(cyear))
print(cmonth,type(cmonth))