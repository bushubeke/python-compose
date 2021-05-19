import json


data=[{ "email": "beimdegefu@gmail.com", "username": "Beimnet", "first_name": "Beimnet", "middle_name": "Bekele", "last_name": "Degefu",  "password": "transport", 
  "confirm": "transport"
},{"email": "bushubekele@gmail.com","username": "Amlakawit","first_name": "Amlakawit","middle_name": "Bekele","last_name": "Degefu","password": "transport",  "confirm": "transport"
},{ "email": "beimnetdegefu@yahoo.com", "username": "Essey", "first_name": "Essey", "middle_name": "Bekele", "last_name": "Degefu",  "password": "transport",
  "confirm": "transport"
}
,{"email": "bushubekele@yahoo.com","username": "Hiwot","first_name": "Hiwot","middle_name": "Bekele","last_name": "Degefu","password": "transport",
  "confirm": "transport"
}]

def test_register_user_and_confirm (client):

    for x in data:
        #print(x)
        #y=requests.post('http://192.168.10.7:5000/api/register',data=x)
        response=client.post('/api/register',data=x)
        #print(y.status_code)
        token=json.loads(response.data)
        z=client.get(f'/api/confirm/{token["message"]}')
        w=client.get(f'/api/confirm/{token["message"]}')
        withouttoken=client.get('/api/confirm/somejibrishhere')
        assert response.status_code == 201
        assert z.status_code == 201
        assert w.status_code == 204
        assert withouttoken.status_code == 403
        

def test_register_double_entry (client):
    for x in data:
        response=client.post('/api/register',data=x)
        #print(y.status_code)
        assert response.status_code == 400

def test_resend_confirm_route(client):
      resend_data=[{"email":"beimdegefu@gmail.com"},{"email":"beimdegefuasdfasdfasdf@gmail.com"},{"email":"beimdegefu"}]
      
      valid_resoponse=client.post('/api/resend',data=resend_data[0])
      invalid_email_resoponse=client.post('/api/resend',data=resend_data[1])
      invalid_form_response=client.post('/api/resend',data=resend_data[2])
      print(json.loads(valid_resoponse.data))
      assert valid_resoponse.status_code == 201
      assert invalid_email_resoponse.status_code == 500
      assert invalid_form_response.status_code == 403