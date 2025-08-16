from rest_framework import serializers
from .models import Register,Teacher,GalleryImage

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)  

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'photo', 'specialization']


class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = GalleryImage
        fields = ['id', 'image']
