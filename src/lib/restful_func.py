"""关闭某些方法
"""
from rest_framework import status
from rest_framework.response import Response

class ListDisable():
    """
    Disable list Method.
    """
    def list(self, request):
        """关闭创建方法
        """
        return Response({"detail":"该方法不被允许"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CreateDisable():
    """
    Disable Create Method.
    """
    def create(self, request):
        """关闭创建方法
        """
        return Response({"detail":"该方法不被允许"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UpdatDisable():
    """
    Disable update Method.
    """
    def update(self, request):
        """关闭更新方法
        """
        return Response({"detail":"该方法不被允许"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class DestroyDisable():
    """
    Disable delete Method.
    """
    def destroy(self, request):
        """关闭删除方法
        """
        return Response({"detail":"该方法不被允许"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
