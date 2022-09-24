from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # permissions
        user_permissions = user.get_user_permissions()
        group_permissions = user.get_group_permissions()

        # Add custom claims
        try:
            token['avatar'] = user.anhdaidien.url
        except:
            pass

        return token
