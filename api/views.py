# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Third-party app imports

# Imports from your apps


@api_view(['GET'])
def api_root(request, format=None):
    """
    Endpoint de toda a API REST
    """

    return Response(
        {
            'speakers': reverse('speaker-list', request=request),
            'talks': reverse('talk-list', request=request),
        }
    )
