from django.forms import forms, ModelForm, Textarea
from .models import Listings, User, Categories, Bid, ListingComment, WatchList


class NewListing(ModelForm):
    class Meta:
        model = Listings
        fields = [
            'title', 
            'description', 
            'bid', 
            'category', 
            'url']
        widgets = {'category': Textarea(attrs={'cols': 10, 'rows':1})}

    # new_category = forms.CharField(max_length=50, required=False, label = "New Category Name")

    # def __init__(self, *args, **kwargs):
    #     super(NewListing, self).__init__(*args, **kwargs)
    #     # make "category" not required. We'll check if it's new later on.
    #     self.fields['category'].required = False
        
    # def clean(self):
    #     category = self.cleaned_data('category')
    #     new_category = self.cleaned_data('new_category')
    #     if not studio:
    #         stu