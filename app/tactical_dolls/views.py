from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from tactical_dolls.models import Doll, DollEffect


class Update(View):
    """
    전술 인형 정보를 업데이트합니다.
    """

    def get(request, *args, **kwargs):
        Doll.object.update_doll()
        return HttpResponse('update')




