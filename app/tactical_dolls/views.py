from django.http import HttpResponse
from django.views import View

from tactical_dolls.forms import DollForms
from .models import Doll, DollEffect


class Update(View):
    """
    전술 인형 정보를 업데이트합니다.
    """

    def get(request, *args, **kwargs):
        Doll.object.update_doll()
        return HttpResponse('update')

    def post(self, *args, **kwargs):
        forms = DollForms
        pass
