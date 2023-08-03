from django.urls import path
from accomodation import views

urlpatterns = [
    path('accomodationproformaapi', views.AccomodationProformaApi, name="AccomodationProformaApi"),
    path('accomodationproformaapi/<int:id>', views.AccomodationProformaApi),

    path('accomodationtypeapi', views.AccomodationTypeApi, name="AccomodationTypeApi"),
    path('accomodationtypeapi/<int:id>', views.AccomodationTypeApi),
   
    path('caadaccomodationapi', views.CaadAccomodationApi, name="CaadAccomodationApi"),
    path('caadaccomodationapi/<int:id>', views.CaadAccomodationApi),

    path('ncpaccomodationchkapi', views.NcpCheckAccApi, name="NcpCheckAccApi"),
    path('ncpaccomodationchkapi/<int:id>', views.NcpCheckAccApi),

    path('ncpaccomodationappapi', views.NcpApprovalAccApi, name="NcpApprovalAccApi"),
    path('ncpaccomodationappapi/<int:id>', views.NcpApprovalAccApi),

    path('extensionproformaapi', views.ExtensionProformaApi, name="ExtensionProformaApi"),
    path('extensionproformaapi/<int:id>', views.ExtensionProformaApi),

    path('caadextensionproformaapi', views.CaadExtensionVerificationApi, name="CaadExtensionVerificationApi"),
    path('caadextensionproformaapi/<int:id>', views.CaadExtensionVerificationApi),

    path('loginproformaapi', views.LoginProformaApi, name="LoginProformaApi"),
    path('loginproformaapi/<int:id>', views.LoginProformaApi),

    path('itloginapi', views.ItDeptLoginApi, name="ItDeptLoginApi"),
    path('itloginapi/<int:id>', views.ItDeptLoginApi),



]