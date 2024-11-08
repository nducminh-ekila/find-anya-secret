from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError, _get_error_details
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and "detail" in response.data:
        key = response.data["detail"].code
        response.data[key] = response.data.pop("detail")

    return response


class AppValidationError(ValidationError):
    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        # For validation failures, we may collect many errors together,
        # so the details should always be coerced to a list if not already.
        if isinstance(detail, tuple) or (not isinstance(detail, dict) and not isinstance(detail, list)):
            detail = detail

        self.detail = _get_error_details(detail, code)
