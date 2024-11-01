from .serializers import (
                            ArticleAuthorSerializer,
                            ArticleSerializer,
                            ProductSerializer,
                            ProductsellerSerializer,
                            ShirtSeializer,
                            ShirtSellerSeializer,
                            ShoseSeializer,
                            ShoseSellerSeializer,
                            PantsSeializer,
                            PantsSellerSeializer,
                            ProfileSerializer,
                            ProfileStaffSerializer
                            )
class ArticleAccessMixin():
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ArticleSerializer
        return ArticleAuthorSerializer
    # def perform_create(self, serializer):
    #     if not self.request.user.is_staff:
    #         serializer.save(author=self.request.user)
    #         # serializer.save(author=self.request.user)
    #     return super().perform_create(serializer)
class ProductAccessMixin():
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ProductSerializer
        return ProductsellerSerializer
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(seller=self.request.user)
            # serializer.save(author=self.request.user)
        return super().perform_create(serializer)
class ShirtAccessMixin():
    def get_serializer_class(self):
        # if self.request.user.is_staff:
        #     return ShirtSeializer
        # elif self.request.user.is_seller:
        #     return ShirtSellerSeializer
        # else:
        return ShirtSeializer
    # def perform_create(self, serializer):
    #     if not self.request.user.is_staff:
    #         serializer.save(seller_2=self.request.user)
    #         # serializer.save(author=self.request.user)
    #     return super().perform_create(serializer)
class ShoseAccessMixin():
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ShoseSeializer
        return ShoseSellerSeializer
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(seller_2=self.request.user)
        return super().perform_create(serializer)
class PantsAccessMixin():
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PantsSeializer
        return PantsSellerSeializer
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(seller_2=self.request.user)
        return super().perform_create(serializer)
'''
Profile
'''
class ProfileMixin():
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ProfileStaffSerializer
        if not self.request.user.is_anonymous:
            return ProfileSerializer
# class ShirtAccessMixin():
    # def get_serializer_class(self):
    #     return ShirtSeializer
    # def serializer.validated_data
    # def perform_create(self, serializer):
    #     if not self.request.user.is_staff:
    #         # serializer.save(seller=self.request.user)
    #         serializer.save()
    #         # serializer.data['product']=Product.objects.shirt().filter(seller=self.request.user)

    #     return super().perform_create(serializer)