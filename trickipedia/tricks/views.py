from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import TrickForm
from django.contrib.auth import authenticate, login, logout
from .models import Trick
from django.contrib.auth.decorators import login_required


# create view that allows people to submit tricks. create view only available to 
# superuser that allows them to publish submitted tricks. 
# Make a database of tricks and make the index render all of them.
# Each trick can be clicked on to load a page with description and video.
# Consider using JS, but maybe just create a new page to save time.


def index(request):
    beginner = Trick.objects.filter(difficulty = 'beginner')
    intermediate = Trick.objects.filter(difficulty = 'intermediate')
    advanced = Trick.objects.filter(difficulty = 'advanced')
    pro = Trick.objects.filter(difficulty = 'pro')
    return render(request, "tricks/index.html", {
        'beginner': beginner,
        'intermediate': intermediate,
        'advanced': advanced,
        'pro': pro
        })

def success(request): return render(request, "tricks/review.html", 
            {'msg': 'congrats on your submission!'})

def trickform(request):
    if request.method=='POST':
        form = TrickForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
            
    else: 
        form = TrickForm()
        return render(request, "tricks/trickform.html", {'form': form})

@login_required
def review(request):
    tricks = Trick.objects.filter(accepted = False)
    if tricks:
        return render(request, "tricks/review.html", 
            {'tricks': tricks})
    if not tricks:
        return render(request, "tricks/review.html", 
            {'msg': "looks like there aren't any submissions to go through. good job staying on top of things"})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def reviewtrick(request, trick_id):
    trick = Trick.objects.filter(id = trick_id)
    if request.method=="GET":
        if trick:
            trick = Trick.objects.get(id = trick_id)
            return render(request, "tricks/reviewtrick.html", 
                {'trick': trick})
        else: 
            return render(request, "tricks/review.html", 
                {'msg': "sorry, there isn't a trick here yet." })
    if request.method=="POST":
        trick = Trick.objects.get(id = trick_id)
        skier = request.POST.get('skier')
        insta = request.POST.get('insta')
        filmer = request.POST.get('filmer')
        ns = request.POST.get("ns")
        difficulty = request.POST.get('difficulty')
        description = request.POST.get('description')
        trick.skier = skier
        trick.filmer = filmer
        trick.insta = insta
        trick.ns = ns
        trick.difficulty = difficulty
        trick.description = description
        trick.accepted = True
        trick.save()
        return render(request, "tricks/review.html", 
            {'msg': "submission accepted successfully." })



@login_required
def delete(request, trick_id):
    trick = Trick.objects.filter(id = trick_id)
    if  request.method=="POST" and trick:
        trick = Trick.objects.get(id = trick_id)
        trick.delete()
        return render(request, "tricks/review.html", 
            {'msg': "submission deleted successfully." })
    else:
        return HttpResponseRedirect("/")

def trick(request, trick_id):
    trick = Trick.objects.filter(id = trick_id)
    if request.method=="GET":
        if trick and trick[0].accepted == True:
            trick = Trick.objects.get(id = trick_id)
            return render(request, "tricks/trick.html", 
                {'trick': trick})
        else: 
            return render(request, "tricks/review.html", 
                {'msg': "sorry, there isn't a trick here yet." })

        



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "tricks/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "tricks/login.html")


# Create your views here.
