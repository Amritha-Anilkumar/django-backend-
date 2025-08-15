from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from .serializers import RegisterSerializer,TeacherSerializer,GalleryImageSerializer
from .models import Register,Teacher,GalleryImage
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.http import HttpResponse



@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

       
        name = serializer.validated_data['fname']
        sname=serializer.validated_data['lname']
        email = serializer.validated_data['email']
        preference=serializer.validated_data['preference']

        
        html_message = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px;">
        <h1 style="color: #8e24aa;">
        Welcome <span style="color: #d81b60;">{name}</span> to <span style="color: #6a1b9a;">Vyasa Yoga Center</span>!
        </h1>
        <p style="font-size: 16px; color: #333;">
        We have received your form and noted that you are interested in <strong>{preference}</strong>. 
        We will contact you as soon as possible.<br/>
        Thank you for joining our yoga community!
        </p>
        <hr style="margin-top: 20px;" />
        <p style="font-size: 12px; color: gray;">
        This is an automated message from Vyasa Yoga Center.
        </p>
        </div>

        """

        plain_message = strip_tags(html_message)

       
        send_mail(
            subject='Thanks for Registering!', 
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
            html_message=html_message,
        )

        return Response({'message': 'Registered successfully!'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def showall(request):
    user=Register.objects.all()
    serializer=RegisterSerializer(user,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single(request,pk):
    user=Register.objects.get(id=pk)
    serializer=RegisterSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_teachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_galleryimages(request):
    images = GalleryImage.objects.all()
    serializer = GalleryImageSerializer(images, many=True)
    return Response(serializer.data)


def create_superuser(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "password123")
        return HttpResponse("Superuser created")
    return HttpResponse("Superuser already exists")