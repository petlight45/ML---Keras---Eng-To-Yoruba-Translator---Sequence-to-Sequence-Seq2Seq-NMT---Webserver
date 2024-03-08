from rest_framework import status, response

from utils.ml.helpers import MLHelper


class MLPublicAPIControllers:
    class MLViewSet:
        @staticmethod
        def eng_to_yor_translate(view, request, *args, **kwargs):
            input_ = request.data.get("input")
            if not input_:
                return response.Response(status=status.HTTP_400_BAD_REQUEST, data={
                    "message": "Provide an input to translate"
                })
            translation = MLHelper.translate(word=input_)
            if translation:
                return response.Response(status=status.HTTP_200_OK, data={
                    "translation": translation
                })
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data={
                "message": "No translation found for the given input"
            })
