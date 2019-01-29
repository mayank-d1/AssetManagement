from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from .models import Employee, Device
from utility import sendEmail
from .serializers import EmployeeSeializers


class EmployeeView(APIView):
    def post(self, request):
        try:
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            email_id = request.data["email"]
            emp, created = Employee.objects.get_or_create(first_name=first_name, last_name=last_name, email_id=email_id)
            print(EmployeeSeializers(emp).data)
            Device.objects.create(employee=emp)
            sendEmail(email_id, "Activate", "Your device is activated")
            return Response({"response": "Employee registered successfully"}, status=HTTP_200_OK)

        except Exception:
            return Response({"response": "FAIL"}, HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            emp = Employee.objects.all()
            emp_serializer = EmployeeSeializers(emp, many=True).data
            return Response(emp_serializer, HTTP_200_OK)
        except Exception:
            return Response({"response": "FAIL"}, HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        try:
            emp_id = request.data["emp_id"]
            device_id = request.data["device_id"]

            dev = Device.objects.filter(employee__employee_id=emp_id).update(device_id=device_id)

            if dev:
                return Response({"response": "Device updated successfully"}, HTTP_200_OK)
            else:
                return Response({"response": "Employee not found"}, HTTP_404_NOT_FOUND)

        except Exception:
            return Response({"response": "FAIL"}, HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            emp_id = request.data["emp_id"]
            email = list(Employee.objects.filter(employee_id=emp_id).values('email_id'))
            Employee.objects.filter(employee_id=emp_id).delete()
            sendEmail(email[0]["email_id"], "Deactivate", "Your device is deactivated")
            return Response({"response": "Employee deleted successfully"}, HTTP_200_OK)
        except Exception:
            return Response({"response": "FAIL"}, HTTP_500_INTERNAL_SERVER_ERROR)
