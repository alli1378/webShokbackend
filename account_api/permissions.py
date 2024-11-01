from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsStaff(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
            
        )

class IsSuperUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_superuser)
class IsAuthor(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS and not request.user.is_anonymous:
        #     return True
        
        return bool(
            (not request.user.is_anonymous and
            request.user.is_superuser) or
           ( not request.user.is_anonymous and
            obj.author == request.user 
           )
        )
class IsAuthorCreate(BasePermission):
    
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS and not request.user.is_anonymous:
        #     return True
        
        return bool(
            (not request.user.is_anonymous and
            request.user.is_superuser) or
             (not request.user.is_anonymous and
            request.user.is_author) 
           
            # request.user.is_author 
            
        )
class IsSeller(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS and not request.user.is_anonymous:
        #     return True
        
        return bool(
            (not request.user.is_anonymous and
            request.user.is_superuser) or
            obj.seller == request.user 
            
        )

class IsSellerCreate(BasePermission):
    
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS and not request.user.is_anonymous:
        #     return True
        
        return bool(
            request.user.is_superuser or
            request.user.is_seller
           
            # request.user.is_author 
            
        )

class IsSpecial(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (not request.user.is_anonymous and
            request.user.is_author)or
            (request.user and
            request.user.is_superuser)or
            (not request.user.is_anonymous and
            request.user.is_seller)
            
        )

class IsSuperUserOrStaffReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and not request.user.is_anonymous and request.user.is_staff:
            return True
        if request.user.is_anonymous:
            return False
        
        return bool(
            not request.user.is_anonymous and
            request.user.is_superuser
            
        )
