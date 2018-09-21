import json

from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from google.auth.transport import requests
from google.oauth2 import id_token

from .utils import login_or_create_administrator


class LoginView(View):
    def get(self, request):
        """
        Renders the login.html page
        """
        next_url = request.GET.get('next', '')
        return render(request, 'administrators/login.html', {
            "google_client_id": settings.GOOGLE_CLIENT_ID,
            "next_url": next_url
        })

    def post(self, request):
        """
        Log a user in. It expects in the request body the token received from google auth service.
        """
        token = json.loads(request.body.decode('utf-8')).get('token')
        if token is None:
            return HttpResponse('Token is not provided', status=400)

        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)
        except ValueError:
            return HttpResponse('Bad token', status=400)
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        login_or_create_administrator(request, id_info)
        return HttpResponse('/admin')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'administrators/logout.html', {'google_client_id': settings.GOOGLE_CLIENT_ID})
