from django.shortcuts import render

def color_table(request):
    shades = []
    for i in range(51):
        shades.append(i * 5)
    print(shades)
    return render(request, 'color_table.html', {'shades' : shades})
