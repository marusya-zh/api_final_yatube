from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


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
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        # Указываем конкретные поля, поскольку вывод id для подписок
        # не требуется (в отличие от, например, постов и комментариев),
        # и «Explicit is better than implicit». )
        fields = ('user', 'following')

    def create(self, validated_data):
        user = validated_data.get('user')
        following = validated_data.get('following')

        if user == following:
            raise serializers.ValidationError(
                {
                    "following": [
                        "Недопустимое значение поля. "
                        "Подписка на себя запрещена."
                    ]
                }
            )
        elif Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                {
                    "following": [
                        "Недопустимое значение поля. "
                        "Такая подписка уже существует."
                    ]
                }
            )

        return Follow.objects.create(**validated_data)
