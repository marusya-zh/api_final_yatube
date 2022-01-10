from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')


    def create(self, validated_data):
        user = validated_data.get('user')
        following = validated_data.get('following')

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                {
                    'following': 'Недопустимое значение поля. '
                                 'Такая подписка уже существует.'
                }
            )
        elif user == following:
            raise serializers.ValidationError(
                {
                    'following': 'Недопустимое значение поля. '
                                 'Подписка на себя запрещена.'
                }
            )

        return Follow.objects.create(user=user, following=following)
