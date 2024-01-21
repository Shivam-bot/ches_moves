from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .moves import *


@csrf_exempt
def chess(request, **kwargs):
    try:
        message = f"{request.method} Method not allowed"
        if request.method.lower() == 'post':
            data = JSONParser().parse(request)
            if data is not None:
                positions = data.get("positions", None)

                if positions.__class__.__name__ == 'dict':
                    piece_name = kwargs.get('piece_name', None)
                    if piece_name is not None:
                        valid_moves = get_moves(piece_name, positions)
                        return JsonResponse({"status":"success", 'valid_moves':valid_moves})
                    else:
                        message = "Piece to move not given"
                else:
                    message = "Invalid type for position"
            else:
                message = "Data Not given"
        return JsonResponse({"status": "success", 'valid_moves': [],"error_message":message})
    except Exception as e:
        return JsonResponse({"status":"failed", "valid_moves":[], 'error_message':f'{e}'})



