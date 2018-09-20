from django.http import HttpResponse
from django.views import View

from tactical_dolls.models import Doll


class Update(View):
    """
    인형 정보를 업데이트 합니다.
    """

    def get(request, *args, **kwargs):
        Doll.object.update_doll()
        return HttpResponse('update')
