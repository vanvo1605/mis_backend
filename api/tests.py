from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Student  # Adjust import path as per your project
from .serializers import StudentSerializer

# Create your tests here.
class StudentViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create sample data for testing
        self.student1 = Student.objects.create(name='Alice', email='CQqoN@example.com', created_at='2022-01-01', updated_at='2022-01-01')
        self.student2 = Student.objects.create(name='Bob', email='5dJi7@example.com', created_at='2022-01-02', updated_at='2022-01-02')

    def test_list_students(self):
        # Test GET request to list all students
        response = self.client.get('/api/student/')  # Adjust URL as per your project's URL configuration
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_student(self):
        # Test GET request to retrieve a single student
        url = f'/api/student/{self.student1.id}/'  # Adjust URL as per your project's URL configuration
        response = self.client.get(url)
        student = Student.objects.get(id=self.student1.id)
        serializer = StudentSerializer(student)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_student(self):
        # Test POST request to create a new student
        new_student_data = {'username': 'vanvo001', 'password': '123123', 'name': 'Eve', 'email': 'JkQoN@example.com', 'created_at': '2022-01-01', 'updated_at': '2022-01-01'}
        response = self.client.post('/api/student/', new_student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 3)  # Assuming you had 2 students created in setUp

    def test_update_student(self):
        # Test PUT request to update an existing student
        updated_data = {'name': 'Alice Updated', 'email': 'CQqoN@example.com', 'created_at': '2022-01-01', 'updated_at': '2022-01-01'}
        url = f'/api/student/{self.student1.id}/'  # Adjust URL as per your project's URL configuration
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.name, 'Alice Updated')

    def test_delete_student(self):
        # Test DELETE request to delete an existing student
        url = f'/api/student/{self.student1.id}/'  # Adjust URL as per your project's URL configuration
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 1)