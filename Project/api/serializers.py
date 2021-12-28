from .models import Snippet, Tag
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    title = serializers.CharField(source='TagInfo.title')
    content = serializers.CharField(source='text')
    timestamp = serializers.DateTimeField(source='created')

    class Meta:
        model = Snippet
        fields = ['content', 'timestamp', 'UserInfo', 'title', 'id']


class SnippetResolveSerializer(serializers.ModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # User = serializers.CharField(source='UserInfo.username')
    title = serializers.CharField(source='TagInfo.title')
    content = serializers.CharField(source='text')
    timestamp = serializers.DateTimeField(source='created')

    class Meta:
        model = Snippet
        fields = ['title', 'content', 'timestamp']


class TagSerializer(serializers.ModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = Tag
        fields = ['title']  # ] , 'snippets']


class TagUrlSerializer(serializers.HyperlinkedModelSerializer):

    # url = serializers.SerializerMethodField(source='get_absolute_url')

    # def get_url(self,obj):
    #     return "{}".format(self)

    class Meta:
        model = Tag
        fields = ['title',]  # ] , 'snippets']


class TagLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', ]


class SnippetLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['text', 'created', 'TagInfo', 'UserInfo', ]
