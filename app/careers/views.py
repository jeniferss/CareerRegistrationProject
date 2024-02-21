from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from app.careers.models import CareerModel, CareerSerializer, CareerUpdateSerializer


class CareerAPIView(APIView):

    def get_instance(self, career_id: int):
        return get_object_or_404(CareerModel, id=career_id)

    def get(self, request, career_id: int = None):
        if career_id:
            instance = self.get_instance(career_id=career_id)
            response = CareerSerializer(instance).data
            return Response(data=response, status=status.HTTP_200_OK)

        paginator = PageNumberPagination()
        results = CareerModel.objects.all().order_by('id')
        results = paginator.paginate_queryset(queryset=results, request=request)

        response = CareerSerializer(results, many=True).data
        return paginator.get_paginated_response(response)

    def post(self, request):
        request_data = request.data
        request_data.update({'author_ip': request.META["REMOTE_ADDR"]})

        instance = CareerSerializer(data=request_data)
        instance.is_valid(raise_exception=True)
        instance.save()

        return Response(data=instance.data, status=status.HTTP_200_OK)

    def patch(self, request, career_id: int = None):
        if not career_id:
            return Response(
                data={'detail': 'The PATCH method is not allowed without providing an ID in the path.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

        instance = self.get_instance(career_id=career_id)

        data = CareerUpdateSerializer(instance, data=request.data)
        data.is_valid(raise_exception=True)
        data.save()

        return Response(data=data.data, status=status.HTTP_200_OK)

    def delete(self, request, career_id: int = None):
        if not career_id:
            return Response(
                data={'detail': 'The DELETE method is not allowed without providing an ID in the path.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

        instance = self.get_instance(career_id=career_id)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
