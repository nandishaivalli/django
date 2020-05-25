from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def analise(request):
    djtext = request.POST.get('text','null')
    removepunc = request.POST.get('removepunc','off')
    allcaps = request.POST.get('allcaps','off')
    newline = request.POST.get('newline', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.POST.get('countchar','off')

    req = 0

    if removepunc == 'on':
        req += 1
        analised = ""
        punctuations = '''!()[]-:;.,'"\/?<>@#$%^&*_|~`'''
        for char in djtext:
            if char not in punctuations:
                analised = analised + char
        params = {'purpose':'removed punctuations' , 'analised_text':analised}

        djtext = analised
    if allcaps=='on':
        req += 1
        analised = ""
        for char in djtext:
            analised = analised + char.upper()
        params = {'purpose':'CONVERT TO UPPER CASE' , 'analised_text':analised}

        djtext = analised
    if newline=='on':
        req += 1
        analised = ""
        for char in djtext:
            if char !='\n' and char != '\r':
                analised = analised + char
        params = {'purpose':'new line remover' , 'analised_text':analised}

        djtext = analised
    if extraspaceremover =='on':
        req += 1
        analised = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analised = analised+char
        params = {'purpose': 'remove extra space', 'analised_text': analised}

    analised = djtext
    length  = 0
    if countchar=='on':
        req += 1
        length = len(analised)
        params = {'purpose': 'remove extra space', 'analised_text': analised ,'work':'Number of charactors','charcount' : length}

    if req == 0 :
        return HttpResponse('''<i>toggle atleast one input</i> ''')
    return render(request,'analise.html',params)