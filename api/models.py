from django.db import models
import time

# Create your models here.
class AlertNotice(models.Model):
    '''
    报警通知模型
    '''
    alert_type=models.SmallIntegerField(choices=((1, "email"), (2, "webhook")),default=2)
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128,unique=True)
    
    class Meta:
        db_table='alert_notices'

class AlertEvent(models.Model):
    '''
    事件模型
    '''
    name = models.CharField(max_length=128)
    describe = models.CharField(max_length=256)
    create_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M', time.localtime()))
    
    class Meta:
        db_table = 'alert_event'

class AlertPrometheus(models.Model):
    '''
    prometheus 报警模型
    '''
    name = models.CharField(max_length=128)
    interface=models.CharField(max_length=128)
    condition=models.CharField(max_length=512)
    receiver=models.CharField(max_length=32)
    alert_medium=models.ForeignKey(AlertNotice,on_delete=models.CASCADE)
    class Meta:
        db_table = 'alert_Prometheus'

class AlertLogapp(models.Model):
    '''
    日志模型
    '''
    name = models.CharField(max_length=128)
    describe = models.CharField(max_length=256)
    es_address=models.CharField(max_length=128)
    class Meta:
        db_table = 'alert_log_app'

class AlertLogrule(models.Model):
    '''
    日志报警规则模型
    '''
    app=models.ForeignKey(AlertLogapp,on_delete=models.CASCADE,related_name='app')
    name = models.CharField(max_length=128)
    es_index_prefix = models.CharField(max_length=128)
    es_query = models.CharField(max_length=128)
    log_count = models.IntegerField()
    in_minutes = models.IntegerField()
    trigger = models.IntegerField(blank=True, null=True)
    product = models.CharField(max_length=128)
    priority = models.IntegerField()
    no_deal = models.IntegerField()
    owner = models.CharField(max_length=128)
    create_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M', time.localtime()))
    class Meta:
        db_table = 'alert_log_rules'
