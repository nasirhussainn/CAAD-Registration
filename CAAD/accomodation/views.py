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
        accomodation_prof_data = JSONParser().parse(request)
        try:
            std_cnic = accomodation_prof_data['std_cnic']
        except KeyError:
            return JsonResponse({"message": "Missing std_cnic"}, status=400)

        try:
            student_registration = StudentRegistration.objects.get(std_cnic=std_cnic)
        except StudentRegistration.DoesNotExist:
            return JsonResponse({"message": "Missing student record"}, status=404)

        try:
            internship = Internships.objects.get(registration_no=student_registration.reg_form_id)
        except Internships.DoesNotExist:
            return JsonResponse({"message": "Missing internship record"}, status=404)

        accomodation_prof_data['internship'] = internship.internship_id

        identity = accomodation_prof_data['internship']
        try:
            identity_performa_id = IdentitycardProforma.objects.get(internship=identity)
        except IdentitycardProforma.DoesNotExist:
            return JsonResponse({"message": "Missing student card record"}, status=404)

        accomodation_prof_data['identity_card'] = identity_performa_id.identity_performa_id

        accomodation_prof_serializer = AccomodationProformaSerializer(data=accomodation_prof_data)
        if accomodation_prof_serializer.is_valid():
            accomodation = accomodation_prof_serializer.save()

            caad_accomodation_verification_data = {
                'accomodation_form': accomodation.ac_id,
            }
            caad_accomodation_verification_serializer = CaadAccomodationVerificationSerializer(
                data=caad_accomodation_verification_data
            )
            if caad_accomodation_verification_serializer.is_valid():
                caad_accomodation_verification_serializer.save()

            return Response({"message": "Insert successfully"})
        return JsonResponse(accomodation_prof_serializer.errors, status=400)
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
        accomodation_type=AccomodationType.objects.get(accomodation_id=accomodation_type_data['accomodation_id'])
        accomodation_type_serializer = AccomodationTypeSerializer(accomodation_type,data=accomodation_type_data) 
        if accomodation_type_serializer.is_valid():
            accomodation_type_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        accomodation_type=AccomodationType.objects.get(accomodation_id=id)
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
        ncpChk_accomodation=CaadAccomodationVerification.objects.get(caad_hr3_id=ncpChk_accomodation_data['caad_hr3_id'])
        ncpChk_accomodation_serializer = CaadAccomodationVerificationSerializer(ncpChk_accomodation,data=ncpChk_accomodation_data) 
        if ncpChk_accomodation_serializer.is_valid():
            ncpChk_accomodation_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        ncpChk_accomodation=CaadAccomodationVerification.objects.get(caad_hr3_id=id)
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
        caad_accomodation=NcpAccomodationCheck.objects.get(ncp_chk_id=caad_accomodation_data['ncp_chk_id'])
        caad_accomodation_serializer = NcpAccomodationCheckSerializer(caad_accomodation,data=caad_accomodation_data) 
        if caad_accomodation_serializer.is_valid():
            caad_accomodation_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        caad_accomodation=NcpAccomodationCheck.objects.get(ncp_chk_id=id)
        caad_accomodation.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END

#NCP approval accomodation
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
        ncpAppr_accomodation=NcpAccomodationApproval.objects.get(ncp_allotted_id=ncpAppr_accomodation_data['ncp_allotted_id'])
        ncpAppr_accomodation_serializer = NcpAccomodationApprovalSerializer(ncpAppr_accomodation,data=ncpAppr_accomodation_data) 
        if ncpAppr_accomodation_serializer.is_valid():
            ncpAppr_accomodation_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        ncpAppr_accomodation=NcpAccomodationApproval.objects.get(ncp_allotted_id=id)
        ncpAppr_accomodation.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END

#Extension Proforma
@api_view(['GET', 'POST','PUT','DELETE'])
def ExtensionProformaApi(request,id=0):
    if request.method=="GET":
        extension_prof = ExtensionProforma.objects.all()
        extension_prof_serializer = ExtensionProformaSerializer(extension_prof, many=True)
        return Response(extension_prof_serializer.data)
    elif request.method == 'POST':
        extension_prof_data=JSONParser().parse(request)
        try:
            std_cnic=extension_prof_data['std_cnic']
        except KeyError:
            return JsonResponse({"message":"Missing std_cnic"},status=404)
        try:
            student_registration=StudentRegistration.objects.get(std_cnic=std_cnic)
        except StudentRegistration.DoesNotExist:
             return JsonResponse({"message":"Missing student record"},status=404)
        try:
            internship=Internships.objects.get(registration_no=student_registration.reg_form_id)
        except Internships.DoesNotExist:
             return JsonResponse({"message":"Missing internship record"},status=404)
        extension_prof_data['internship']=internship.internship_id
        extension_prof_serializer = ExtensionProformaSerializer(data=extension_prof_data) 
        if extension_prof_serializer.is_valid():
            extension=extension_prof_serializer.save()
            caad_extension_verification_data={
                'extension_form':extension.extension_form_id,
            }
            caad_extension_verification_serializer=CaadExtensionVerificationSerializer(
                data=caad_extension_verification_data
            )
            if caad_extension_verification_serializer.is_valid():
                caad_extension_verification_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        extension_prof_data=JSONParser().parse(request)
        extension_prof=ExtensionProforma.objects.get(extension_form_id=extension_prof_data['extension_form_id'])
        extension_prof_serializer = ExtensionProformaSerializer(extension_prof,data=extension_prof_data) 
        if extension_prof_serializer.is_valid():
            extension_prof_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        extension_prof=ExtensionProforma.objects.get(extension_form_id=id)
        extension_prof.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END

#CAAD Extension Proforma Verification
@api_view(['GET', 'POST','PUT','DELETE'])
def CaadExtensionVerificationApi(request,id=0):
    if request.method=="GET":
        caad_extension_prof = CaadExtensionVerification.objects.all()
        caad_extension_prof_serializer = CaadExtensionVerificationSerializer(caad_extension_prof, many=True)
        return Response(caad_extension_prof_serializer.data)
    elif request.method == 'POST':
        caad_extension_prof_data=JSONParser().parse(request)
        caad_extension_prof_serializer = CaadExtensionVerificationSerializer(data=caad_extension_prof_data) 
        if caad_extension_prof_serializer.is_valid():
            caad_extension_prof_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        caad_extension_prof_data=JSONParser().parse(request)
        caad_extension_prof=ExtensionProforma.objects.get(caad_extension_id=caad_extension_prof_data['caad_extension_id'])
        caad_extension_prof_serializer = CaadExtensionVerificationSerializer(caad_extension_prof,data=caad_extension_prof_data) 
        if caad_extension_prof_serializer.is_valid():
            caad_extension_prof_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        caad_extension_prof=CaadExtensionVerification.objects.get(caad_extension_id=id)
        caad_extension_prof.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END

#Login Proforma
@api_view(['GET', 'POST','PUT','DELETE'])
def LoginProformaApi(request,id=0):
    if request.method=="GET":
        login_prof = LoginProforma.objects.all()
        login_prof_serializer = LoginProformaSerializer(login_prof, many=True)
        return Response(login_prof_serializer.data)
    elif request.method == 'POST':
        login_prof_data=JSONParser().parse(request)
        try:
            std_cnic=login_prof_data['std_cnic']
        except KeyError:
            return JsonResponse({"message":"Missing std_cnic"},status=404)
        try:
            student_registration=StudentRegistration.objects.get(std_cnic=std_cnic)
        except StudentRegistration.DoesNotExist:
             return JsonResponse({"message":"Missing student record"},status=404)
        try:
            internship=Internships.objects.get(registration_no=student_registration.reg_form_id)
        except Internships.DoesNotExist:
             return JsonResponse({"message":"Missing internship record"},status=404)
        login_prof_data['internship']=internship.internship_id
        login_prof_serializer = LoginProformaSerializer(data=login_prof_data) 
        if login_prof_serializer.is_valid():
            login=login_prof_serializer.save()
            it_dept_data={
                'login_form':login.login_form_id,
            }
            it_dept_serializer=ItDeptLoginSerializer(
                data=it_dept_data
            )
            if it_dept_serializer.is_valid():
                it_dept_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        login_prof_data=JSONParser().parse(request)
        login_prof=ExtensionProforma.objects.get(login_form_id=login_prof_data['login_form_id'])
        login_prof_serializer = LoginProformaSerializer(login_prof,data=login_prof_data) 
        if login_prof_serializer.is_valid():
            login_prof_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        login_prof=LoginProforma.objects.get(login_form_id=id)
        login_prof.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END

#Login Proforma
@api_view(['GET', 'POST','PUT','DELETE'])
def ItDeptLoginApi(request,id=0):
    if request.method=="GET":
        it_login = ItDeptLogin.objects.all()
        it_login_serializer = ItDeptLoginSerializer(it_login, many=True)
        return Response(it_login_serializer.data)
    elif request.method == 'POST':
        it_login_data=JSONParser().parse(request)
        it_login_serializer = ItDeptLoginSerializer(data=it_login_data) 
        if it_login_serializer.is_valid():
            it_login_serializer.save()
            return Response({"message": "Insert successfully"})
        return JsonResponse("Failed to Insert",safe=False)
    elif request.method == 'PUT':
        it_login_data=JSONParser().parse(request)
        it_login=ItDeptLogin.objects.get(user_id=it_login_data['user_id'])
        it_login_serializer = ItDeptLoginSerializer(it_login,data=it_login_data) 
        if it_login_serializer.is_valid():
            it_login_serializer.save()
            return Response({"message": "Updated successfully"})
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        it_login=ItDeptLogin.objects.get(user_id=id)
        it_login.delete()
        return JsonResponse("Deleted sucessfully",safe=False)
#END