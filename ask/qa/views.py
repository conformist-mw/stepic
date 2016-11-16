from django.shortcuts import render


def test(request, *args, **kwargs):
    return render(request, 'index.html',
                  content_type='text/html')
