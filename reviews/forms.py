from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'content']
        labels = {
            "content": "Message",
            "title": "Subject",
            "rating": "How would you rate your experience? \
                        1: poor, 5: Excellent"
        }
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 5,
                                       'placeholder': 'Please write your message\
                                        for us here.'})
        }
