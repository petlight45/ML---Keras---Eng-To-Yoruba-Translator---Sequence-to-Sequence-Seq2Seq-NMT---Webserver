import os
from django.conf import settings


class MLHelperConfig:
    RESOURCE_PATH = os.path.join(settings.BASE_DIR, "utils/ml/resource")

    class TokenizerType:
        ENGLISH = "eng"
        YORUBA = "yor"

    class MaxSentenceCount:
        ENGLISH = 7
        YORUBA = 13
