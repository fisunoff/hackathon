class UserDataMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            if profile.is_manager:
                return qs
            return qs.filter(author=profile)
        return qs.none()
