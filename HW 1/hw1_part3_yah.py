import math as m
frame= input("Enter frame character ==> ")
print(frame)
height = int(input ("Height of box ==> "))
print(height)
width = int(input("Width of box ==> "))
print (width, "\n")
str_w= (width*frame)
print("Box:")
print(str_w)
#prints top row
h_pri = height / 2

h_top= int((m.trunc(h_pri- 1))) *(frame + (width - 2) * " " + frame + "\n")
h_bot = (int((m.ceil(h_pri)- 2)) *(frame + (width - 2) * " " + frame + "\n")).strip()

center = m.trunc(width/2)
width_str= str(width)
height_str= str(height)
#turns int width into strings to use in later text
center_txt= ((center - len(width_str) - len(height_str) )  * " ") + width_str + "X"+ height_str + (((width//2 - 1-  len(str(width))) * " ") + frame)


print(h_top, frame, center_txt, sep=(''))
#print()
print(h_bot, end ="\n")
print(str_w)