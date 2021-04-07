from django.utils.deprecation import MiddlewareMixin

class MyCors(MiddlewareMixin):
    """解决跨域中间件"""
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = "Content-Type"
            response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
        return response