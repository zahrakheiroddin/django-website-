from django.shortcuts import render
from django.core.mail import  send_mail
from .forms import contactformemail


# Create your views here
def testing (request):
    return render(request, 'test/test.html', {})

def contactsendmail(request):
    if request.method=="GET":
        form=contactformemail()
        return render(request, 'test/contact.html', ({'form':form}))
    else:
        form=contactformemail(request.POST)
        if form.is_valid():
            frommail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,'dobicho@dobicho.com',[frommail])
            return render(request, 'test/contact.html', ({'form':form}))
