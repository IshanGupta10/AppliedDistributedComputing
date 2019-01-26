from rest_framework import serializers

class StudentInfoSerialzer(serializers.Serializer):
    studentID = serializers.IntegerField()
    studentName = serializers.CharField()
    studentYear = serializers.CharField()
    courseOne = serializers.CharField()
    courseTwo = serializers.CharField()
    courseThree = serializers.CharField()