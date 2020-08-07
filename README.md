# alert
### 模型结构
```
报警通知模型
事件模型
prometheus 报警模型
日志模型
日志报警规则模型
```
### 功能
```
1、 报警服务 -  单独运行在本系统之外的一个独立进程 webhook
2、 事件上报 -  通过webhook将每次接收到的报警信息写入数据库
3、 指标监控 -  通过调用prometheus 接口，将配置的指标同步到prometheus系统中
4、 日志监控 -  通过定义好的查询语句，查询特定的es，将结果返回
```
// 后续扩展功能： api监控、第三方监控对接



### 技术点：
```
前后端分离
nginx
py3
django
django-freamwork
mysql
es
prometheus
alertmanager
k8s 
```
### 设计原型思路
![图1]
()
