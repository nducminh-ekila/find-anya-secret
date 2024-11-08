from rest_framework.renderers import JSONRenderer

from app_core.responses import APIFailedResponse, APISuccessResponse


class APIJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        response = renderer_context["response"]
        data_response = {
            "msg": "SUCCESS" if not response.exception else "FAILURE",
            "code": response.status_code,
            "data": data,
        }

        if isinstance(response, (APISuccessResponse, APIFailedResponse)):
            data_response["msg"] = response.msg
            data_response["data"] = response.res_data

        return super().render(data_response, accepted_media_type, renderer_context)
