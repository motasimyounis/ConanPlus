from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .forms import ContactForm
from django.contrib import messages
import markdown2
# Create your views here.

def convert(f):

        html= markdown2.markdown(f)
        return html
    

def home(request):
    team =  Allteam.objects.filter(arabic = False , myteam=True)
    package = Package.objects.filter(arabic = False)
    que = Frequentlyquestion.objects.filter(arabic = False)
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    context = {
        'team':team,
        'package':package,
        'que':que,
        'form': form
        
    }    
    return render(request,'index.html' , context)


def home_ar(request):
    team = Allteam.objects.filter(arabic = True, myteam=True)
    package = Package.objects.filter(arabic = True)
    que = Frequentlyquestion.objects.filter(arabic = True)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    context = {
        'team':team,
        'package':package,
        'que':que,
        'form': form
        
    }    
    return render(request,'index - ar.html' , context)

def team(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    team = Allteam.objects.filter(arabic = False)
    context = {
        'team':team,
        'form':form
    }
    return render(request,'team.html' ,context)

def team_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
        
    team = Allteam.objects.filter(arabic = True)
    
    context = {
        'team':team,
        'form':form
    }
    return render(request,'team - ar.html',context)



def web(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    web = Services.objects.filter(type="website")
    context = {
        'web':web,
        'form':form
    }
    return render(request,'web.html',context)



def web_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    web = Services.objects.filter(type="website")
    context = {
        'web':web,
        'form':form
    }
    return render(request,'web - ar.html',context)


def ui(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    ui = Services.objects.filter(type="ux ui")
    context = {
        'ui':ui,
        'form':form
    }
    return render(request,'UX & UI.html',context)



def ui_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    ui = Services.objects.filter(type="ux ui")
    context = {
        'ui':ui,
        'form':form
    }
    return render(request,'UX & UI - ar.html',context)




def graphic(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    graphic = Graphicdesign.objects.all()
    context = {
        'graphic':graphic,
        'form':form
    }
    return render(request,'graphic-design.html',context)


def graphic_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    graphic = Graphicdesign.objects.all()
    context = {
        'graphic':graphic,
        'form':form
    }
    return render(request,'graphic-design - ar.html',context)


def mobile(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    mobile = Mobileapplication.objects.all()
    context = {
        'mobile':mobile,
        'form':form
    }
    return render(request,'Mobile application.html',context)


def mobile_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    mobile = Mobileapplication.objects.all()
    context = {
        'mobile':mobile,
        'form':form
    }
    return render(request,'Mobile application - ar.html',context)


def motion(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    motion = Services.objects.filter(type="Motion graphic")
    context = {
        'motion':motion,
        'form':form
    }
    return render(request,'Motion graphic.html',context)

def motion_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    motion = Services.objects.filter(type="Motion graphic")
    context = {
        'motion':motion,
        'form':form
    }
    return render(request,'Motion graphic - ar.html',context)



def social(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and form != None:
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to the service')
            return redirect('/')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    social = Socialmedia.objects.all()
    context = {
        'social':social,
        'form':form
    }
    return render(request,'Social media management.html',context)



def social_ar(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'لقد اشتركت في الخدمة بنجاح')
            return redirect('/ar')  # Redirect to a success page
    else:
        form = SubscriptionForm()
    social = Socialmedia.objects.all()
    context = {
        'social':social,
        'form':form
    }
    return render(request,'Social media management - ar.html',context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent, Thank you for contacting us')
            return redirect('contact')# Save the form data to the database
          # Redirect to a success page after form submission
    else:
        form = ContactForm()

    return render(request,'contact-us.html', {'form': form})



def contact_ar(request):
    if request.method == 'POST':
        form = ContactFormar(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'تم إرسال رسالتك ، شكراً لك على تواصلك معنا')
            return redirect('contact-ar')
    else:
        form = ContactFormar()

    return render(request,'contact-ar.html', {'form': form})