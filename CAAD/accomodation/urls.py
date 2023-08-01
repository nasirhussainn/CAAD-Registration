from django.urls import path
from accomodation import views

urlpatterns = [
    path('accomodationproformaapi', views.AccomodationProformaApi, name="AccomodationProformaApi"),
    path('accomodationproformaapi/<int:ac_id>', views.AccomodationProformaApi),

    path('accomodationtypeapi', views.AccomodationTypeApi, name="AccomodationTypeApi"),
    path('accomodationtypeapi/<int:ac_id>', views.AccomodationTypeApi),
   
    path('caadaccomodationapi', views.CaadAccomodationApi, name="CaadAccomodationApi"),
    path('caadaccomodationapi/<int:ac_id>', views.CaadAccomodationApi),

    path('ncpaccomodationchkapi', views.NcpCheckAccApi, name="NcpCheckAccApi"),
    path('ncpaccomodationchkapi/<int:ac_id>', views.NcpCheckAccApi),

    path('ncpaccomodationappapi', views.NcpApprovalAccApi, name="NcpApprovalAccApi"),
    path('ncpaccomodationappapi/<int:ac_id>', views.NcpApprovalAccApi),





]