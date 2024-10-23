from django.shortcuts import render


def color_table(request):
    return render(request, 'color_table.html')