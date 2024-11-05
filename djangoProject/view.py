import json
from django.http import JsonResponse
from django.shortcuts import render
from style.models import personstyle
import logging

logger = logging.getLogger(__name__)

def index1(request):
    context = {'wyb': 'gw'}
    return render(request, 'index1.html', context)


def recommend(request):
    context = {'wyb': 'gw'}
    return render(request, 'recommend.html', context)

# def recommend(request):
#     if request.method == 'POST':
#         try:
#             # 获取提交的数据
#             data = json.loads(request.body)
#
#             # 检查请求体中是否包含所有必需的字段
#             required_fields = ['height', 'weight', 'setting', 'weather', 'type']
#             if not all(field in data for field in required_fields):
#                 return JsonResponse({'error': 'Missing required fields'}, status=400)
#
#             # 将用户输入的数据保存到数据库中
#             person = personstyle(
#                 name="Anonymous",  # 假设姓名是匿名的
#                 height=data['height'],
#                 setting=data['setting'],
#                 weather=data['weather'],
#                 type=data['type']
#             )
#             person.save()
#
#             # 返回保存的数据作为响应
#             return JsonResponse({
#                 'height': data['height'],
#                 'weight': data['weight'],
#                 'setting': data['setting'],
#                 'weather': data['weather'],
#                 'type': data['type']
#             })
#         except json.JSONDecodeError:
#             logger.error("Invalid JSON format")
#             return JsonResponse({'error': 'Invalid JSON format'}, status=400)
#         except Exception as e:
#             logger.error(f"An error occurred: {str(e)}")
#             return JsonResponse({'error': 'Internal server error'}, status=500)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)