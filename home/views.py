from django.shortcuts import render


def home(request):
    template = 'index.html'
    # context = {'form': form}
    return render(request, template, {})
