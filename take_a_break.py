# Program that reminds the user to take a break every two hours.
import webbrowser
import time

total_breaks = 1
break_num=1
seconds_in_hours = 60*60
hours = 2
break_time = hours*seconds_in_hours

print "This program started on " +time.ctime()
while break_num <= total_breaks:
    time.sleep(break_time)
    print "It's been " +str(hours)+' hours. It is currently '+time.ctime()+'. Take a break!'
    webbrowser.open("https://www.youtube.com/watch?v=ReTP6x_sDiM")
    break_num += 1
