from django.shortcuts import render


def numbers():
    nums = []
    for i in range(51):
        nums.append(i)
    return nums

def color_table(request):
    nums = numbers()
    print(nums)
    return render(request, 'color_table.html', {'range': range(51)})