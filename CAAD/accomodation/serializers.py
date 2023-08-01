from rest_framework import serializers
from .models import *

class AccomodationProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccomodationProforma
        fields = '__all__'


class AccomodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccomodationType
        fields = '__all__'


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'


class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'


class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'


class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'


class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'


class CaadAccomodationVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadAccomodationVerification
        fields = '__all__'


class CaadExtensionVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadExtensionVerification
        fields = '__all__'


class CaadIdentityVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadIdentityVerification
        fields = '__all__'


class CaadRegistrationVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadRegistrationVerification
        fields = '__all__'


class ClearancePerformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearancePerforma
        fields = '__all__'


class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'


class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'


class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'


class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class DocumentsUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsUpload
        fields = '__all__'


class EvaluationProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationProforma
        fields = '__all__'


class ExtensionProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionProforma
        fields = '__all__'


class HostedresearcherCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HostedresearcherCategory
        fields = '__all__'


class IdentitycardProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentitycardProforma
        fields = '__all__'

class InternshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internships
        fields = '__all__'


class ItDeptLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItDeptLogin
        fields = '__all__'


class LateSittingProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LateSittingProforma
        fields = '__all__'


class LoginProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginProforma
        fields = '__all__'
class NcpAccomodationApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpAccomodationApproval
        fields = '__all__'


class NcpAccomodationCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpAccomodationCheck
        fields = '__all__'


class NcpDuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpDues
        fields = '__all__'


class NcpPublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpPublications
        fields = '__all__'


class PublicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationsList
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPictures
        fields = '__all__'


class StudentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegistration
        fields = '__all__'


class SysdiagramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sysdiagrams
        fields = '__all__'


class TransportMemberProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMemberProforma
        fields = '__all__'


class TransportSectionConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportSectionConfirmation
        fields = '__all__'

class UniversitySupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySupervisor
        fields = '__all__'