# x=[4,6,1,3,5,7,25]
# y=0
# def draw_stars(x):
#     for val in range (0,len(x)):
#         y= x[val]* "*"
#         print y
# draw_stars(x)

x=[4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
y=0
def draw_stars(x):
    for val in range (0,len(x)):
        if type(x[val]) is str:
            y = len(x[val]) * str.lower(x[val][0])
            print y
        else:
            y = x[val] * "*"
            print y
draw_stars(x)
