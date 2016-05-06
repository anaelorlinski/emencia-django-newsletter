
"""Forms for emencia.django.newsletter"""
from django import forms
from django.utils.translation import ugettext_lazy as _

from emencia.django.newsletter.models import Contact
from emencia.django.newsletter.models import MailingList


class MailingListSubscriptionForm(forms.ModelForm):
    """Form for subscribing to a mailing list"""
    # Notes : This form will not check the uniquess of
    # the 'email' field, by defining it explictly and setting
    # it the Meta.exclude list, for allowing registration
    # to a mailing list even if the contact already exists.
    # Then the contact is always added to the subscribers field
    # of the mailing list because it will be cleaned with no
    # double.

    email = forms.EmailField(label=_('Email'), max_length=75)

    def save(self, mailing_list):
        data = self.cleaned_data
        contact, created = Contact.objects.get_or_create(
            email=data['email'],
            defaults={'first_name': data.get('first_name', None),
                      'last_name': data.get('last_name', None)})

        mailing_list.subscribers.add(contact)
        mailing_list.unsubscribers.remove(contact)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name')
        exclude = ('email',)


class AllMailingListSubscriptionForm(MailingListSubscriptionForm):
    """Form for subscribing to all mailing list"""

    mailing_lists = forms.ModelMultipleChoiceField(
        queryset=MailingList.objects.all(),
        initial=[],
        label=_('Mailing lists'),
        widget=forms.MultipleHiddenInput(attrs={"checked": ""}))

    def __init__(self, *args, **kwargs):
        super(AllMailingListSubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['mailing_lists'].initial = [obj.id
                                                for obj in MailingList.objects.all()]

    def save(self, mailing_list):
        data = self.cleaned_data
        contact, created = Contact.objects.get_or_create(
            email=data['email'],
            defaults={'first_name': data.get('first_name', None),
                      'last_name': data.get('last_name', None)})

        for mailing_list in data['mailing_lists']:
            mailing_list.subscribers.add(contact)
            mailing_list.unsubscribers.remove(contact)
