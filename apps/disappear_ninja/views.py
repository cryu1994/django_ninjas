from django.shortcuts import render
def index(request):

    return render(request, "index/index.html")
def ninjas(request):
    return render(request, "index/index.html")
def color(request, color):
    if color == 'blue':
        file_path = "leonardo.jpg"
    if color == 'red':
        file_path = 'raphael.jpg'
    if color == 'purple':
        file_path = 'donatello.jpg'
    if color == 'orange':
        file_path = 'michelangelo.jpg'
    if color == 'all_ninjas':
        file_path = 'tmnt.png'
    if color == 'ninjas':
        file_path = 'notapril.jpg'
    context = {
        'file_path': file_path
    }
    return render(request, "index/index.html", context)
