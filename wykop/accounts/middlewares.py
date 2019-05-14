from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


class TosAccepted:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user
        if user.is_authenticated and \
                user.accepted_tos != settings.CURRENT_TOS_VERSION and \
                request.path != reverse('accounts:confirm_tos'):
            url = reverse('accounts:confirm_tos') + '?next=' + request.path
            return HttpResponseRedirect(url)

        response = self.get_response(request)
        return response
