import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
class comsConsummer(WebsocketConsumer):
    def connect(self):
        self.t_id=self.scope["url_route"]["kwargs"]["t_id"]
        self.t_group_id="taskcom_%s"%self.t_id
        #Join channels room group
        async_to_sync(self.channel_layer.group_add)(
            self.t_group_id,self.channel_name
        )

        self.accept()

    def disconnect(self,close_code):
        #leave channels room group
        async_to_sync(self.channel_layer.group_discard)(
            self.t_group_id,self.channel_name
        )
class tasksConsumer(WebsocketConsumer):
    def connect(self):
        self.p_id=self.scope["url_route"]["kwargs"]["p_id"]
        self.p_group_id="tasksgr_%s"%self.p_id
        #Join channels room group
        async_to_sync(self.channel_layer.group_add)(
            self.p_group_id,self.channel_name
        )

        self.accept()

    def disconnect(self,close_code):
        #leave channels room group
        async_to_sync(self.channel_layer.group_discard)(
            self.p_group_id,self.channel_name
        )

    #Receive message from WebSocket
    #class Tasks(models.Model):
    #t_id=models.BigAutoField(primary_key=True)
    #t_name=models.CharField(max_length=30)
    #t_full_text=models.TextField(null=True)
    #t_file=models.TextField(null=True)
    #t_start=models.DateField()
    #t_end=models.DateField(null=True)
    #t_fact_end_time=models.DateTimeField(null=True)
    #t_creator_post_id=models.ForeignKey('Posts',on_delete=models.CASCADE)
    #false- если любой из post; true -если должны закрыть все
    #t_close_by_all=models.BooleanField(default=False)
    #true- если завершена; false - если не завершена
    #t_status=models.BooleanField(default=False)
    #o-обычная;s-срочная;d-ДСП(прямое поручение);i-информационная(ознакомительная)
    #t_type=models.CharField(max_length=2,default='o')
    #t_comments=models.ManyToManyField(to=Comments,null=True)
    #текстовые значения 
    #t_chek_list=models.ForeignKey(to=Cheklist,null=True)
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        t_id=text_data_json["t_id"]
        t_name=text_data_json["t_name"]
        t_start=text_data_json["t_start"]
        t_end=text_data_json["t_end"]
        t_whois=text_data_json["t_whois"]
        #send message to channels room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{"type":"chat_message","t_id":t_id,"t_name":t_name,"t_start":t_start,"t_end":t_end,"t_whois":t_whois}
        )
    #Receive message from channels room group
    def chat_message(self,event):
        t_id=event["t_id"]
        t_name=event["t_name"]
        t_start=event["t_start"]
        t_end=event["t_end"]
        t_whois=event["t_whois"]
        #send message to Websocket!!!!!!!
        self.send(text_data=json.dumps({"t_id":t_id,"t_name":t_name,"t_start":t_start,"t_end":t_end,"t_whois":t_whois}))