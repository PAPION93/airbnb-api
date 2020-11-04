from rest_framework.decorators import api_view
from rest_framework.views import APIView

class MeView(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass

@api_view(["GET"])
def user_detail(request, pk):
    pass