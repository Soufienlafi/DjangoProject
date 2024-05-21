from .models import TransportRequest, Post

def transport_requests_processor(request):
    transport_requests = []
    post_id = None
    if request.user.is_authenticated:
        transport_requests = TransportRequest.objects.filter(post__user=request.user)
        post = Post.objects.filter(user=request.user).first()
        if post:
            post_id = post.id

    return {'transport_requests': transport_requests, 'post_id': post_id}
