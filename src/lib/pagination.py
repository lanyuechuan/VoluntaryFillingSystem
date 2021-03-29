import math
from collections import OrderedDict
from rest_framework import pagination
from rest_framework.response import Response


class PagePagination(pagination.PageNumberPagination):
    '''按分页数分页
    '''
    page_size = 10 # 每页显示的条数
    page_query_param = "page" # 获取页码数的
    page_size_query_param = "page_size" # 通过传入page_size=15,改变默认每页显示的个数
    max_page_size = 100 # 最大页数不超过100

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                self.page_size = pagination._positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return self.page_size

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('page_size', self.page_size),
            ('total', self.page.paginator.count),
            ('pages', math.ceil(self.page.paginator.count/self.page_size)),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data)
        ]))


class LimitPagination(pagination.LimitOffsetPagination):
    '''按偏移量分页
    '''
    default_limit = 10  # 每页显示的条数

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', int((self.offset/self.limit)+1)),
            ('offset', self.offset),
            ('limit', self.limit),
            ('total', self.count),
            ('pages', math.ceil(self.count/self.limit)),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data)
        ]))


class MyPagePagination(PagePagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('page_size', self.page.paginator.per_page),
            ('total', self.page.paginator.count),
            ('pages', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data)
        ]))
