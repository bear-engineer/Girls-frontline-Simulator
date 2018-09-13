from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Update(View):
    def get(self, request):
        return HttpResponse('크롤링 완료')
