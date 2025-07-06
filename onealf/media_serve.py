import mimetypes
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import View

class MediaServeView(View):
    def get(self, request, path):
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if not os.path.exists(file_path):
            raise Http404("Arquivo não encontrado")

        with open(file_path, 'rb') as f:
            content = f.read()
        content_type, _ = mimetypes.guess_type(file_path)
        return HttpResponse(content, content_type=content_type)