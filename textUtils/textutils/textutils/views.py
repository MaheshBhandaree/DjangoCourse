#I have created this filecd
from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request,'index.html')
    # return HttpResponse("<h1>Home</h1>")


# def about(request):
#     return HttpResponse("About mahesh")
#
# def navigate(request):
#     s = '''<h2>Navigation Bar<br></h2>
#                <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>
#                <a href="https://www.facebook.com/">Facebook</a><br>
#                <a href="https://www.flipkart.com/">Flipkart</a><br>
#                <a href="https://www.hindustantimes.com">News</a><br>
#                <a href="https://www.google.com/">Google</a><br>
#                <a href="https://www.instagram.com/">Instagram</a>'''
#     return HttpResponse(s)


# def NewLineRemove(request):
#     return HttpResponse("<h1>newLineRemove</h1> <a href='http://127.0.0.1:8000/'>back to home</a><br>")
# def RemovePunc(request):
#     djtext= request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("<h1>RemovePunc</h1 <a href='http://127.0.0.1:8000/'>back to home</a><br>")
# def Capfirst(request):
#     return HttpResponse("<h1>Capfirst</h1> <a href='http://127.0.0.1:8000/'>back to home</a><br>")
# def SpaceRemove(request):
#     return HttpResponse("<h1>SpaceRemove</h1> <a href='http://127.0.0.1:8000/'>back to home</a><br>")
# def CharCount(request):
#     return HttpResponse("<h1>CharCount</h1> <a href='http://127.0.0.1:8000/'>back to home</a><br>")

def Analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('Removepunc','Off')
    Fullcaps=request.POST.get('Fullcaps','Off')
    NewlineRemover=request.POST.get('NewlineRemover','Off')
    Extraspaceremover=request.POST.get('Extraspaceremover','Off')
    if removepunc=="on":
        analysed =""
        plist ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in plist:
                analysed = analysed+char

        params= {'purpose':'Remove Punctuation','analyase_text':analysed}
        djtext= analysed
        # return render(request,'analyse.html', params)
    if(Fullcaps=="on"):
        analysed=""
        for char in djtext:
            analysed = analysed+ char.upper()
        params = {'purpose': 'Change to uppercase', 'analyase_text': analysed}
        djtext=analysed
        # return render(request, 'analyse.html', params)
    if (NewlineRemover == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char!= "\r":
                analysed = analysed + char
        params = {'purpose': 'remove New Line', 'analyase_text': analysed}
        djtext=analysed
        # return render(request, 'analyse.html', params)
    if (Extraspaceremover == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
            params = {'purpose': 'Remove New Line', 'analyase_text': analysed}
            djtext=analysed
            # return render(request, 'analyse.html', params)

    if(removepunc!="on" and NewlineRemover !="on" and Extraspaceremover!="on" and Fullcaps!="on"):
        return HttpResponse("You not click the Correct input:(")
    # else:
    #     return HttpResponse("Error")

    return render(request, 'analyse.html', params)
