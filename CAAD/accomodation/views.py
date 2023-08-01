from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



# Accomodation Proforma API
@api_view(['GET', 'POST','PUT','DELETE'])
def AccomodationProformaApi(request,id=0):
    if request.method=="GET":
        accomodation_prof = AccomodationProforma.objects.all()
        accomodation_prof_serializer = AccomodationProformaSerializer(accomodation_prof, many=True)
        return Response(accomodation_prof_serializer.data)
    elif request.method == 'POST':
        accomodation_prof_data=JSONParser().parse(request)
        accomodation_prof_serializer = AccomodationProformaSerializer(data=accomodation_prof_data) 
        if accomodation_prof_serializer.is_valid():
            accomodation_prof_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        accomodation_prof_data=JSONParser().parse(request)
        accomodation_prof=AccomodationProforma.objects.get(ac_id=accomodation_prof_data['ac_id'])
        accomodation_prof_serializer = AccomodationProformaSerializer(accomodation_prof,data=accomodation_prof_data) 
        if accomodation_prof_serializer.is_valid():
            accomodation_prof_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        accomodation_prof=AccomodationProforma.objects.get(ac_id=id)
        accomodation_prof.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
# End here Accomodation Proforma API
  

# Accomodation Type API
@api_view(['GET', 'POST','PUT','DELETE'])
def AccomodationTypeApi(request,id=0):
    if request.method=="GET":
        accomodation_type = AccomodationType.objects.all()
        accomodation_type_serializer = AccomodationTypeSerializer(accomodation_type, many=True)
        return Response(accomodation_type_serializer.data)
    elif request.method == 'POST':
        accomodation_type_data=JSONParser().parse(request)
        accomodation_type_serializer = AccomodationTypeSerializer(data=accomodation_type_data) 
        if accomodation_type_serializer.is_valid():
            accomodation_type_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        accomodation_type_data=JSONParser().parse(request)
        accomodation_type=AccomodationType.objects.get(ac_id=accomodation_type_data['ac_id'])
        accomodation_type_serializer = AccomodationTypeSerializer(accomodation_type,data=accomodation_type_data) 
        if accomodation_type_serializer.is_valid():
            accomodation_type_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        accomodation_type=AccomodationType.objects.get(ac_id=id)
        accomodation_type.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#End


# Caad Accomodation Verification
@api_view(['GET', 'POST','PUT','DELETE'])
def CaadAccomodationApi(request,id=0):
    if request.method=="GET":
        ncpChk_accomodation = CaadAccomodationVerification.objects.all()
        ncpChk_accomodation_serializer = CaadAccomodationVerificationSerializer(ncpChk_accomodation, many=True)
        return Response(ncpChk_accomodation_serializer.data)
    elif request.method == 'POST':
        ncpChk_accomodation_data=JSONParser().parse(request)
        ncpChk_accomodation_serializer = CaadAccomodationVerificationSerializer(data=ncpChk_accomodation_data) 
        if ncpChk_accomodation_serializer.is_valid():
            ncpChk_accomodation_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        ncpChk_accomodation_data=JSONParser().parse(request)
        ncpChk_accomodation=CaadAccomodationVerification.objects.get(ac_id=ncpChk_accomodation_data['ac_id'])
        ncpChk_accomodation_serializer = CaadAccomodationVerificationSerializer(ncpChk_accomodation,data=ncpChk_accomodation_data) 
        if ncpChk_accomodation_serializer.is_valid():
            ncpChk_accomodation_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        ncpChk_accomodation=CaadAccomodationVerification.objects.get(ac_id=id)
        ncpChk_accomodation.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#End

#NCP check accomodation
@api_view(['GET', 'POST','PUT','DELETE'])
def NcpCheckAccApi(request,id=0):
    if request.method=="GET":
        caad_accomodation = NcpAccomodationCheck.objects.all()
        caad_accomodation_serializer = NcpAccomodationCheckSerializer(caad_accomodation, many=True)
        return Response(caad_accomodation_serializer.data)
    elif request.method == 'POST':
        caad_accomodation_data=JSONParser().parse(request)
        caad_accomodation_serializer = NcpAccomodationCheckSerializer(data=caad_accomodation_data) 
        if caad_accomodation_serializer.is_valid():
            caad_accomodation_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        caad_accomodation_data=JSONParser().parse(request)
        caad_accomodation=NcpAccomodationCheck.objects.get(ac_id=caad_accomodation_data['ac_id'])
        caad_accomodation_serializer = NcpAccomodationCheckSerializer(caad_accomodation,data=caad_accomodation_data) 
        if caad_accomodation_serializer.is_valid():
            caad_accomodation_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        caad_accomodation=NcpAccomodationCheck.objects.get(ac_id=id)
        caad_accomodation.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END

#NCP check accomodation
@api_view(['GET', 'POST','PUT','DELETE'])
def NcpApprovalAccApi(request,id=0):
    if request.method=="GET":
        ncpAppr_accomodation = NcpAccomodationApproval.objects.all()
        ncpAppr_accomodation_serializer = NcpAccomodationApprovalSerializer(ncpAppr_accomodation, many=True)
        return Response(ncpAppr_accomodation_serializer.data)
    elif request.method == 'POST':
        ncpAppr_accomodation_data=JSONParser().parse(request)
        ncpAppr_accomodation_serializer = NcpAccomodationApprovalSerializer(data=ncpAppr_accomodation_data) 
        if ncpAppr_accomodation_serializer.is_valid():
            ncpAppr_accomodation_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        ncpAppr_accomodation_data=JSONParser().parse(request)
        ncpAppr_accomodation=NcpAccomodationApproval.objects.get(ac_id=ncpAppr_accomodation_data['ac_id'])
        ncpAppr_accomodation_serializer = NcpAccomodationApprovalSerializer(ncpAppr_accomodation,data=ncpAppr_accomodation_data) 
        if ncpAppr_accomodation_serializer.is_valid():
            ncpAppr_accomodation_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        ncpAppr_accomodation=NcpAccomodationApproval.objects.get(ac_id=id)
        ncpAppr_accomodation.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END