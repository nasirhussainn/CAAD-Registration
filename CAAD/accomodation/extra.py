from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import *
from .serializers import *

# Create your views here.

@csrf_exempt
def IdentitycardProformaApi(request,id=0):
    if request.method=='GET':
        identitycard=IdentitycardProforma.objects.all()
        identitycard_serializer=IdentitycardProformaSerializer(identitycard,many=True)
        return JsonResponse(identitycard_serializer.data,safe=False)
    elif request.method=='POST':
        identitycard_data=JSONParser().parse(request)
        identitycard_serializer=IdentitycardProformaSerializer(data=identitycard_data)
        if identitycard_serializer.is_valid():
            identitycard_serializer.save()
            return JsonResponse("Added an Identity Card Successfully",safe=False)
        return JsonResponse("Failed to add the card",safe=False)
    elif request.method=='PUT':
        identitycard_data=JSONParser().parse(request)
        identitycard=IdentitycardProforma.objects.get(identity_performa_id=identitycard_data['identity_performa_id'])
        identitycard_serializer=IdentitycardProformaSerializer(identitycard,data=identitycard_data)
        if identitycard_serializer.is_valid():
            identitycard_serializer.save()
            return JsonResponse("Updated the identity card successfuly",safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        identitycard=IdentitycardProforma.objects.get(identity_performa_id=id)
        identitycard.delete()
        return JsonResponse("Deleted identity card Successfully, yay",safe=False)


@csrf_exempt
def CaadIdentityApi(request,id=0):
    if request.method=='GET':
        caadidentity=CaadIdentityVerification.objects.all()
        caadidentity_serializer=CaadIdentityVerificationSerializer(caadidentity,many=True)
        return JsonResponse(caadidentity_serializer.data,safe=False)
    elif request.method=='POST':
        caadidentity_data=JSONParser().parse(request)
        caadidentity_serializer=CaadIdentityVerificationSerializer(data=caadidentity_data)
        if caadidentity_serializer.is_valid():
            caadidentity_serializer.save()
            return JsonResponse("Added a CAAD Identity Verification Successfully",safe=False)
        return JsonResponse("Failed to add CAAD Verification",safe=False)
    elif request.method=='PUT':
        caadidentity_data=JSONParser().parse(request)
        caadidentity=CaadIdentityVerification.objects.get(caad_identity_id=caadidentity_data['caad_identity_id'])
        caadidentity_serializer=CaadIdentityVerificationSerializer(caadidentity,data=caadidentity_data)
        if caadidentity_serializer.is_valid():
            caadidentity_serializer.save()
            return JsonResponse("Updated the caad identity verification successfuly",safe=False)
        return JsonResponse("Failed to update caad identity verification")
    elif request.method=='DELETE':
        caadidentity=CaadIdentityVerification.objects.get(caad_identity_id=id)
        caadidentity.delete()
        return JsonResponse("Deleted caad identity verification Successfully, yay",safe=False)


@csrf_exempt
def LateSittingApi(request,id=0):
    if request.method=='GET':
        latesitting=LateSittingProforma.objects.all()
        latesitting_serializer=LateSittingProformaSerializer(latesitting,many=True)
        return JsonResponse(latesitting_serializer.data,safe=False)
    elif request.method=='POST':
        latesitting_data=JSONParser().parse(request)
        latesitting_serializer=LateSittingProformaSerializer(data=latesitting_data)
        if latesitting_serializer.is_valid():
            latesitting_serializer.save()
            return JsonResponse("Added a Late Sitting Form Successfully",safe=False)
        return JsonResponse("Failed to add Late Sitting Form",safe=False)
    elif request.method=='PUT':
        latesitting_data=JSONParser().parse(request)
        latesitting=LateSittingProforma.objects.get(late_form_id=latesitting_data['late_form_id'])
        latesitting_serializer=LateSittingProformaSerializer(latesitting,data=latesitting_data)
        if latesitting_serializer.is_valid():
            latesitting_serializer.save()
            return JsonResponse("Updated the late sitting form successfuly",safe=False)
        return JsonResponse("Failed to update the late sitting form")
    elif request.method=='DELETE':
        latesitting=LateSittingProforma.objects.get(late_form_id=id)
        latesitting.delete()
        return JsonResponse("Deleted the late form Successfully, yay",safe=False)


@csrf_exempt
def TransportMemFormApi(request,id=0):
    if request.method=='GET':
        transportform=TransportMemberProforma.objects.all()
        transportform_serializer=TransportMemberProformaSerializer(transportform,many=True)
        return JsonResponse(transportform_serializer.data,safe=False)
    elif request.method=='POST':
        transportform_data=JSONParser().parse(request)
        transportform_serializer=TransportMemberProformaSerializer(data=transportform_data)
        if transportform_serializer.is_valid():
            transportform_serializer.save()
            return JsonResponse("Added a Transport Membership Form Successfully",safe=False)
        return JsonResponse("Failed to add Transport Membership Form",safe=False)
    elif request.method=='PUT':
        transportform_data=JSONParser().parse(request)
        transportform=TransportMemberProforma.objects.get(transport_form_id=transportform_data['transport_form_id'])
        transportform_serializer=TransportMemberProformaSerializer(transportform,data=transportform_data)
        if transportform_serializer.is_valid():
            transportform_serializer.save()
            return JsonResponse("Updated the Transport Membership form successfuly",safe=False)
        return JsonResponse("Failed to update the Transport Membership form")
    elif request.method=='DELETE':
        transportform=TransportMemberProforma.objects.get(transport_form_id=id)
        transportform.delete()
        return JsonResponse("Deleted the Transport Form Successfully, yay",safe=False)

@csrf_exempt
def TransportSectConfirmationApi(request,id=0):
    if request.method=='GET':
        transportsect=TransportSectionConfirmation.objects.all()
        transportsect_serializer=TransportSectionConfirmationSerializer(transportsect,many=True)
        return JsonResponse(transportsect_serializer.data,safe=False)
    elif request.method=='POST':
        transportsect_data=JSONParser().parse(request)
        transportsect_serializer=TransportSectionConfirmationSerializer(data=transportsect_data)
        if transportsect_serializer.is_valid():
            transportsect_serializer.save()
            return JsonResponse("Added a Transport Section Confirmation Successfully",safe=False)
        return JsonResponse("Failed to add Transport Confirmation",safe=False)
    elif request.method=='PUT':
        transportsect_data=JSONParser().parse(request)
        transportsect=TransportSectionConfirmation.objects.get(transport_confirmation_id=transportsect_data['transport_confirmation_id'])
        transportsect_serializer=TransportSectionConfirmationSerializer(transportsect,data=transportsect_data)
        if transportsect_serializer.is_valid():
            transportsect_serializer.save()
            return JsonResponse("Updated the Transport Section Confirmation successfuly",safe=False)
        return JsonResponse("Failed to update the Transport Section Confirmation")
    elif request.method=='DELETE':
        transportsect=TransportSectionConfirmation.objects.get(transport_confirmation_id=id)
        transportsect.delete()
        return JsonResponse("Deleted the Transport Section Confirmation Successfully, yay",safe=False)
    

"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CAAD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('identityapi/model/', views.IdentitycardProformaApi, name='IdentitycardProformaApi'),  
    path('identityapi/model/<int:id>/', views.IdentitycardProformaApi, name='IdentitycardProformaApi'),
    path('caadidentityapi/model/', views.CaadIdentityApi, name='CaadIdentityApi'),  
    path('caadidentityapi/model/<int:id>/', views.CaadIdentityApi, name='CaadIdentityApi'),  
    path('latesittingapi/model/', views.LateSittingApi, name='LateSittingApi'),  
    path('latesittingapi/model/<int:id>/', views.LateSittingApi, name='LateSittingApi'), 
    path('transportformapi/model/', views.TransportMemFormApi, name='TransportMemFormApi'),  
    path('transportformapi/model/<int:id>/', views.TransportMemFormApi, name='TransportMemFormApi'),
    path('transportsectapi/model/', views.TransportSectConfirmationApi, name='TransportSectConfirmationApi'),  
    path('transportsectapi/model/<int:id>/', views.TransportSectConfirmationApi, name='TransportSectConfirmationApi'),  
]