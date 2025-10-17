# You want to check whether a web page loads within 3 seconds (performance test condition).

# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time =float(input("Enter the load time in seconds :"))
if load_time <= 0:
    print("Invalid Time Entered")
elif 0 < load_time <= 3:
    print("Load Time :",load_time)
elif load_time >3:
    print("⚠️ Page load too slow :" + str(load_time),"Seconds")