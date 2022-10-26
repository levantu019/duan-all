from rest_framework.permissions import BasePermission
from quanlytaikhoan.utils import choices
from quanlytaikhoan.models import NhomTaiKhoan, NguoiDung
from quanlytbkt.models import TrangBiKhiTai
from quanlydonvi.models import DonVi

# get roles of user from NhomTaiKhoan
def checkRoleUser(role, user):
    group_user = user.groups.all()
    role_user = [NhomTaiKhoan.objects.get(group=item).role for item in group_user]

    return role in role_user


# Superuser 
class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        user = request.user
        checkRole = checkRoleUser(choices.ADMIN, user)

        if user.is_authenticated:
            return user.is_superuser | checkRole
        return False


# AdminData 
class IsAdminData(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        checkRole = checkRoleUser(choices.ADMIN_DATA, user)

        if user.is_authenticated:
            return checkRole
        return False

# User level 1
class IsUserLevel1(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        checkRole = checkRoleUser(choices.USER_LEVEL_1)

        if user.is_authenticated:
            return checkRole
        return False

# User level 2
class IsUserLevel2(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        checkRole = checkRoleUser(choices.USER_LEVEL_2)

        if user.is_authenticated:
            return checkRole
        return False

# User level 3
class IsuserLevel3(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        checkRole = checkRoleUser(choices.USER_LEVEL_3)

        if user.is_authenticated:
            return checkRole
        return False


# 
class HasUserTBKT(BasePermission):
    """
        Hiện tại Trang bị khí tài không được kiểm soát đến từng User
        Sử dụng: TBKT thuộc Đơn vị nào thì User trong Đơn vị đó có quyền với nó
    """
    def has_permission(self, request, view):
        user = request.user
        