from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)


from .models import Snippet, Tag
from .serializers import SnippetLinkSerializer, SnippetResolveSerializer, SnippetSerializer, TagLinkSerializer, TagSerializer, TagUrlSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import HTMLFormRenderer

@api_view(['GET'])
def overview ( request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        total = snippets.count()
        
        for data in serializer.data:
            data['link'] = "http://localhost:8000/api/v1/snippet/{}".format(data['id'])

        return Response({"data":serializer.data , 'overview' : total})


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    # renderer_classes = [HTMLFormRenderer]
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)

        for data in serializer.data:
            data['link'] = "http://localhost:8000/api/v1/snippet/{}".format(data['id'])

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # renderer_classes = [HTMLFormRenderer]
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetResolveSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TagList(APIView):
    """
    List all Tags, or create a new Tag.
    """
    # renderer_classes = [HTMLFormRenderer]
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagUrlSerializer(tags, many=True)
        for data in serializer.data:
            data['link'] = "http://localhost:8000/api/v1/tag/{}".format(data['id'])

        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = TagSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetail(APIView):
    """
    Retrieve, update or delete a Tag instance.
    """
    # renderer_classes = [HTMLFormRenderer]
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
