from rest_framework.exceptions import APIException

class ProgramNotFound(APIException):
    status_code = 404
    default_detail = 'Program not found'


class ProgramIdNotFound(APIException):
    status_code = 403
    default_detail = 'Please provide valid program ID'
