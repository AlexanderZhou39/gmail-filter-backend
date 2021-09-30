from rest_framework.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CollegeSerializer
from .models import College
from django.http import JsonResponse
# Create your views here.
@api_view(['POST'])
def college_post(request):
 
    request_body = request.data
    filters = {}
    domains = []
    for k, v in request_body.items():
        if k == 'domains':
            domains = v
        else: 
            filters[k] = v

    print(filters)
    # # print(request_body.keys)
    # # for key in request_body.keys:
    # #     print(key)
    
    # for key in request_body:
    #     print(key)
    college_dict = {
        
    }
    
    for d in domains:
        college_dict[d] = False

    


    for domain in domains:

        college_info = None #College.objects.filter(domain__equals = domain)
        try:
            college_info = College.objects.get(domain = domain)
        except College.DoesNotExist:
            college_dict[domain] = True
            continue
        conclusion = True
        if filters["filters"]["optStatus"]["useRanking"]:
            if filters["filters"]["schoolRankings"]["lowestRanking"] > college_info.overall_rank:
                conclusion = False
                print('dsds09870987')

        if filters["filters"]["optStatus"]["useAcceptanceRate"]:
            if filters["filters"]["acceptanceRate"]["min"] > college_info.acceptance or filters["filters"]["acceptanceRate"]["max"] < college_info.acceptance:
                conclusion = False
                print('dsds7564')

        if filters["filters"]["optStatus"]["useStudentBodySize"]:
            if filters["filters"]["studentbodysize"]["min"] > college_info.undergrad_student_body or filters["filters"]["studentbodysize"]["max"] < college_info.undergrad_student_body:
                conclusion = False
                print('dsds421421412')

        if filters["filters"]["optStatus"]["useSATScore"]:
            if filters["filters"]["sat"]["min"] > college_info.sat or filters["filters"]["sat"]["max"] < college_info.sat:
                conclusion = False
                print('dsds312')

        if filters["filters"]["optStatus"]["useACTScore"]:
            if filters["filters"]["act"]["min"] > college_info.act or filters["filters"]["act"]["max"] < college_info.act:
                conclusion = False
                print('dsds12')

        if filters["filters"]["optStatus"]["useTution"]:
            if filters["filters"]["tuition"]["max"] < college_info.tuition:
                conclusion = False
                print('dsds312321321321')
        college_dict[domain] = conclusion
    # for k in request_body.items():
    #     print(k)
    # print(request_body.lists())
    # # min_sat_score = request_body.get('filters').get('sat').get('min')
    # # if min_sat_score is not None:
    # #     colleges_match = College.objects.filter(sat=min_sat_score)
    # # all_domains = request_body.get('domains')
    
    # # for domain in request_body.get('domains'):
    # #     # college_dict[domain] = True
    # #     print(domain)
    
    return JsonResponse(college_dict)