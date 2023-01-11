frame= input("Enter frame character ==> ")
print(frame)
height = int(input ("Height of box ==> "))
print(height)
width = int(input("Width of box ==> "))
print (width, "\n")
str_w= (width*frame)
#makes the top and bottom rows
extra_int = int(((height/2 - height//2) *2))
extra_row = extra_int * (frame + (width - 2) * " " + frame)
# gives me an extra row if it's an odd number
str_htop= ((height//2-2) *(frame + (width - 2) * " " + frame + (extra_int * "\n"))).strip()
str_hbot = ((height//2-1) *(frame + (width-2) * " " + frame + "\n")).strip()
#makes the 2 rows spread apart by the width and shortended by 3 to accomidate for the 
#top and bottom rows and the row w the text
blank_= "\n" * extra_int
#gives me an extra row if theres an odd number for height and doesn't if its even

center = ((width//2) + int(((width/2 - width//2) *2))-2)
width_str= str(width)
height_str= str(height)
#turns int width into strings to use in later text
center_txt= (((center- len(str(height)) )  * " ") + width_str + "X"+ height_str + ((width//2 - 1 - len(str(width))) * " ") + frame)
print("Box:")
print(str_w)
print(str_htop, blank_, extra_row, sep=(""))
print(frame, center_txt, sep=(''))
print(str_hbot)
print(str_w)