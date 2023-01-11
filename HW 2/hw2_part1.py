import math as m
'''
Part 1: gum balls
CS1 

Author: Varun Dhir
Date: 2/13/19
Version 1.0

Sample output

Enter the gum ball radius (in.) => 5.6
5.6
Enter the weekly sales => 43
43 

The machine needs to hold 4 gum balls along each edge. 
Total edge length is 44.80 inches.
Target sales were 54, but the machine will hold 10 extra gum balls.
Wasted space is 50191.99 cubic inches with the target number of gum balls,
or 42835.80 cubic inches if you fill up the machine.
'''
def find_volume_sphere (radius):
    v_s= (4/3) * m.pi* radius ** 3
    return v_s
def find_volume_cube (side):
    v_c = side**3
    return v_c
#use standard forumlas for volume
r= input("Enter the gum ball radius (in.) => ").strip()
print(r)
r= float (r)
sales= input("Enter the weekly sales => ").strip()
print(sales, "\n")
sales = float(sales)
total = m.ceil(sales * 1.25)
side_balls = m.ceil(total ** (1/3))
#since we are not choping up gum I need to put a ceil on it so that it rounds up
extra_fill = side_balls ** 3 - total
# to find the extra balls I found the total number of balls that would fit in the cube and subracted from the target
edge = (2* r) * side_balls 
wasted_space = find_volume_cube(edge) - total* find_volume_sphere((r))
filled_up_waste= find_volume_cube(edge) - (side_balls** 3)* find_volume_sphere((r))
out_str = "The machine needs to hold {} gum balls along each edge. \nTotal edge\
 length is {:.2f} inches.\nTarget sales were {}, but the machine will hold {} \
extra gum balls.\nWasted space is {:.2f} cubic inches with the target number \
of gum balls,\nor {:.2f} cubic inches if you fill up the machine.".format(side_balls, edge, total, extra_fill, wasted_space, filled_up_waste)
print(out_str)