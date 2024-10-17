def user_type(request):
    user_type = None
    if request.user.is_authenticated:
        user_type = request.user.type
    return {'user_type': user_type}
