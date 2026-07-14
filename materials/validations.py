import re

from rest_framework.serializers import ValidationError


class UrlVideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not value or not value.get(self.field):
            return
        reg = re.compile(r"^https?://(?:www\.)?youtube\.com/")
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError("Нельзя прикреплять ссылки на сторонние образовательные платформы или личные сайты")
