from rest_framework import serializers
from .models import JobDescription, Application


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ["id", "title", "company", "raw_text", "parsed_requirements", "created_at"]
        read_only_fields = ["parsed_requirements", "created_at"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "job_description", "status", "match_score", "applied_at", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]