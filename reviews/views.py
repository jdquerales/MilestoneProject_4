from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from profiles.models import UserProfile
import datetime


# Create your views here.

def submit_review_page(request):
    """ A view to submit a user review"""
    if request.user.is_authenticated:
        form = ReviewForm()
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'reviews/submit_review.html', context)
    else:
        return redirect(reverse('home'))


def submit_review(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    form = ReviewForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        comment = form.cleaned_data['content']
        rating = int(form.cleaned_data['rating'])
        review = Review()
        review.user = profile
        review.title = title
        review.content = comment
        review.rating = rating
        review.created = datetime.datetime.now()
        review.save()
        messages.success(
            request, 'Your review has been submitted. Thank you!')
    else:
        messages.error(request, 'An error has ocurred. Please try again!')
    return redirect('home')
