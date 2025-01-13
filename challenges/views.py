from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    'january': 'Learn programming languages',
    'february': 'Do homework every day for 20 minutes',
    'march': 'Do some exercises',
    'april': 'Learn programming languages',
    'may': 'Do homework every day for 20 minutes',
    'june': 'Do some exercises',
    'july': 'Learn programming languages',
    'august': 'Do homework every day for 20 minutes',
    'september': 'Do some exercises',
    'october': 'Learn programming languages',
    'november': 'Do homework every day for 20 minutes',
    'december': 'Do some exercises',
}
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month < 1:
        return HttpResponseNotFound('The month you entered is out of range')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not available')
