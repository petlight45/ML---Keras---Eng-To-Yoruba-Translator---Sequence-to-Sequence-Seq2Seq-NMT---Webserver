from rest_framework import viewsets, decorators

from app.api.public.controllers import MLPublicAPIControllers


class MLViewSet(
    viewsets.ViewSet
):

    @decorators.action(detail=False, methods=["get", "post"])
    def eng_to_yor_translate(self, request, *args, **kwargs):
        return MLPublicAPIControllers.MLViewSet.eng_to_yor_translate(self, request, *args, **kwargs)
