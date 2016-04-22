from rest_framework import serializers
from .models import Post, Subject, Thread


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'thread', 'subject', 'user')


class SubjectSerializer(serializers.ModelSerializer):
    posts = ThreadSerializer(many=True)
    total_posts =serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ('id', 'name', 'posts', 'total_posts')

    def get_total_posts(self, subject):
        return subject.posts.count()


class PostSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = ('id', 'thread','subjects', 'user_has_posted')

    def get_user_has_posted(self, poll):
        has_posted = False
        request = self.context.get('request', None)
        if not request:
            return False
        post = Thread.posts.filter(user_id=request.user.id).first()
        if post:
            has_posted = True
        return has_posted
