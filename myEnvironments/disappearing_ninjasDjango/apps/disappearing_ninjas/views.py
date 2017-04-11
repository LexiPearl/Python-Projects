from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render (request, "disappearing_ninjas/index.html")

def ninjas(request):
    if request.method == "GET":
        context={
            'image': "disappearing_ninjas/images/tmnt.png"
        }
        return render (request, "disappearing_ninjas/ninjas.html", context)
    else:
        return redirect("/")

def color(request, color):
    if request.method == "GET":
        options ={
        'red':"disappearing_ninjas/images/raphael.jpg",
        'blue':"disappearing_ninjas/images/leonardo.jpg",
        'orange': "disappearing_ninjas/images/michelangelo.jpg",
        'purple': "disappearing_ninjas/images/donatello.jpg"
        }
        if color in options:
            context={
                'image': options[color]
            }
        else:
            context={
                'image': 'disappearing_ninjas/images/notapril.jpg'
            }
        print context
        return render (request, "disappearing_ninjas/ninjas.html", context)
    else:
        return redirect ("/")

#     A less concise version:
#     if ninja_color == 'red':
#         context= {
#             'image':'ninjaapp/raphael.jpg'
#         }
#     elif ninja_color == 'blue':
#         context= {
#             'image':'ninjaapp/leonardo.jpg'
#         }
#     elif ninja_color == 'purple':
#         context= {
#             'image':'ninjaapp/donatello.jpg'
#         }
#     elif ninja_color == 'orange':
#         context= {
#             'image':'ninjaapp/michaelangelo.jpg'
#         }
#     else:
#         context= {
#             'image':'ninjaapp/april.jpg'
#         }
#     """
#     return render(request,'ninjaapp/index.html',context)
