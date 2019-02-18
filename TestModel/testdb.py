from django.http import HttpResponse
from .models import Testing


def testdb(request):
    test1 = Testing(t_name='hahahah')
    test2 = Testing(t_method='oooo')

    test1.save()
    test2.save()

    return HttpResponse("<p>add data successfully</p>")
