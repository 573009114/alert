from rest_framework import serializers
from api.models import (AlertNotice,AlertEvent,
                        AlertPrometheus,AlertLogapp,
                        AlertLogrule,
                       )

class NoticeSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(required=False, allow_blank=True, max_length=100)
    alert_type=serializers.ChoiceField(choices=((1, "email"), (2, "webhook")))
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self,validated_data):
        return AlertNotice.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.url = validated_data.get('url', instance.url)
        instance.name = validated_data.get('name', instance.name)
        instance.alert_type = validated_data.get('alert_type', instance.alert_type)
        instance.save()
        return instance


class EventSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=128)
    describe = serializers.CharField(required=False, allow_blank=True, max_length=256)

    def create(self,validated_data):
        return AlertEvent.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.describe = validated_data.get('describe',instance.describe)
        instance.save()
        return instance
    

class PrometheusSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlertPrometheus
        fields = ('id','name','interface','condition','receiver','alert_medium')


class AppSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = AlertLogapp
        fields = '__all__'

class AlertLogruleSerializers(serializers.ModelSerializer):
#    app_id = serializers.CharField(source='app.id')
#    app_name = serializers.CharField(source='app.name')
#    app_describe=serializers.CharField(source='app.describe')
#    app_es_address=serializers.CharField(source='app.es_address')
    class Meta:
        model = AlertLogrule
        fields = '__all__'


class AppRuleSerializers(serializers.ModelSerializer):
    app_id = serializers.CharField(source='app.id')
    app_name = serializers.CharField(source='app.name')
    app_describe=serializers.CharField(source='app.describe')
    app_es_address=serializers.CharField(source='app.es_address')
    class Meta:
        model = AlertLogrule
        fields = '__all__'
