import smtplib
from django.conf import settings
from django.shortcuts import redirect, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Organization
from .serializers import OrganizationSerializer

class OrganizationRegisterView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        organization = serializer.save()
        organization.generate_otp()
        
        email_sent = send_test_email(
            to_email=organization.email,
            subject='Your OTP Code',
            message_body=f'Your OTP code is {organization.otp}'
        )
        
        if not email_sent:
            print('Failed to send OTP email.')
        
        # Store the organization ID in session for the OTP verification step
        self.request.session['organization_id'] = organization.id

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return redirect('verify-otp')  # Redirect to the OTP verification page

def send_test_email(to_email, subject, message_body):
    try:
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, message_body)
        server.sendmail(settings.EMAIL_HOST_USER, to_email, message)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

class VerifyOTPView(APIView):
    def get(self, request, *args, **kwargs):
        organization_id = request.session.get('organization_id')
        if organization_id:
            try:
                organization = Organization.objects.get(id=organization_id)
                return render(request, 'verify_otp.html', {'email': organization.email})
            except Organization.DoesNotExist:
                return Response({'message': 'Organization not found'}, status=status.HTTP_404_NOT_FOUND)
        return render(request, 'verify_otp.html')

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        try:
            organization = Organization.objects.get(email=email)
            if organization.is_otp_valid(otp):
                organization.email_verified = True
                organization.save()
                return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except Organization.DoesNotExist:
            return Response({'message': 'Organization not found'}, status=status.HTTP_404_NOT_FOUND)
