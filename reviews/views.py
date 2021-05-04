from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


# Create your views here.

def submit_review(request):
    """ A view to submit a user review"""

    return render(request, 'reviews/submit_review.html')