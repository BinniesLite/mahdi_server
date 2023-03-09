from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from members.models import Member, Project, Image
from .serializers import MemberSerializer, ProjectSerializer, ImageSerializer


class MemberListAPI(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    

class MemberDetailAPI(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberProjectAPI(APIView):
    def get(self, request, member_id):
        member = Member.objects.get(pk=member_id)
        projects = member.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        
        return_data = []
        
        for item in serializer.data:
            # ignore the members field
            if 'members' in item:
                del item['members']
            return_data.append(item)    
            
        return Response(return_data, status=status.HTTP_200_OK)
    
class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

                                                     
class ProjectDetailAPI(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ImageAPI(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
# get all the images for a project
class ImageProjectRetrieveAPI(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'project_id'
    lookup_url_kwarg = 'project_id'
    
    def get(self, request, project_id):
        images = Image.objects.filter(project_id=project_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)