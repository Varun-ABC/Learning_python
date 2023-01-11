import math as m
min_= int(input("Minutes ==> "))
print(min_)
sec_= input("Seconds ==> ")
print(sec_)
sec_= int(sec_)
miles_str= input("Miles ==> ")
print(miles_str)
miles_ = float(miles_str)
tar_str= input("Target Miles ==> ")
print(tar_str,"\n", sep=(''))
tar_mi= float(tar_str)
hour= float(min_+sec_/60)
pace_minint= int((min_+sec_/60)/ miles_)
pace_minfloat= float((min_+sec_/60)/ miles_)
#seperate into 2 int and float so that I can use the diffrent values for later calculations 
pace_sec= int(((min_+sec_/60)/ miles_ -round(pace_minint))*60)
#the first calculated value is not rounded the second value is so i can iscolate the stuff after the decimal 
pace_str= "Pace is {} minutes and {} seconds per mile.".format(round(pace_minint), pace_sec)
print(pace_str)
speed= round(pace_minfloat**-1*60,2)
speed_unrounded= pace_minfloat**-1*60
#speed is the inverse of the pace multilplied by 60
print("Speed is {:.2f} miles per hour.".format(speed))
target_min = tar_mi * 60 // speed_unrounded
target_sec = m.trunc((tar_mi/ speed_unrounded * 60 - target_min)*60) 
out_line_2= "Time to run the target distance of {:.2f} miles is {:} minutes and {:} seconds.". format(tar_mi,round(target_min),round(target_sec)) 
print(out_line_2)
#print("Time to run the target distance of", round(tar_mi,3), "miles is",round(target_min), "minutes and", round(target_sec), "seconds.")
