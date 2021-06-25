from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ImageModel, MusicModel, VideoModel, FileModel, BlogModel
from .serializers import ImageSerializer, MusicSerializer, VideoSerializer, FileSerializer,  BlogSerializer

class ImageView(APIView):
  def get(self, request):
    images = ImageModel.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicView(APIView):
  def get(self, request):
    musics = MusicModel.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoView(APIView):
  def get(self, request):
    video = VideoModel.objects.all()
    serializer = VideoSerializer(video, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileView(APIView):
  def get(self, request):
    files = FileModel.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogView(APIView):
  def get(self, request):
    blogs = BlogModel.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
