import json



data=[{"email":"bushubekele@gmail.com","password":"transport"},
        {"email":"beimdegefu@gmail.com","password":"transportnotvalid"},
        {"email":"beimdegefu@gmail.com","password":""},
        {"email":"beimdegefunotxxist@gmail.com","password":"transport"},
         ]

def test_login(client):

        response=client.post('api/login',data=data[0])
        token=json.loads(response.data)
        assert response.status_code == 201
        assert token['email'] == data[0]['email']



def test_login_invalid_credentials(client):
        response=client.post('api/login',data=data[1])
        
        assert response.status_code == 401
        
def test_login_invalid_form(client):
        response=client.post('api/login',data=data[2])
        
        assert response.status_code == 403
def test_invalid_user(client):
        response=client.post('api/login',data=data[3])
        assert response.status_code == 404

def test_refresh(client):
        response=client.post('api/login',data=data[0])
        token=json.loads(response.data)
        headers={"X-APP-KEY":f"{token['token']}"} 
        wrheaders={"X-APP-KEY":"whateveriwanttoputinhere"} 
        refnohead=client.get('/api/refresh')
        refresponse=client.get('/api/refresh',headers=headers)
        wrresponse=client.get('/api/refresh',headers=wrheaders)
        assert refnohead.status_code == 401
        assert refresponse.status_code == 201
        assert wrresponse.status_code == 500

def test_resetpassword_route(client):
      resend_data=[{"email":"beimdegefu@gmail.com"},{"email":"beimdegefuasdfasdfasdf@gmail.com"},{"email":"beimdegefu"}]
      valid_resoponse=client.post('/api/resetpassword',data=resend_data[0])
      invalid_email_resoponse=client.post('/api/resetpassword',data=resend_data[1])
      invalid_form_response=client.post('/api/resetpassword',data=resend_data[2])
      token=json.loads(valid_resoponse.data)
      assert valid_resoponse.status_code == 201
      assert invalid_email_resoponse.status_code == 500
      assert invalid_form_response.status_code == 403

def test_change_resetpassword_route(client):
      ###################################################################
      #this is getting token before reset post request
      singledata={"email":"beimdegefu@gmail.com"}
      valid_resoponse=client.post('/api/resetpassword',data=singledata)
      #print(valid_resoponse.data)
      token=json.loads(valid_resoponse.data)
      
      ####################################################################################
      mheader={'X-APP-KEY' : f'{token["token"]}' }
      #headers={"X-APP-KEY":"whateveriwant" } 
      json.dumps(mheader)
      wrheaders={"X-APP-KEY":"whateveriwanttoputinhere"} 
      
      change_data=[{"password":"somethingnew","confirm":"somethingnew"},{"password":"","confirm":""}]
      no_token_valid=client.post('/api/change',data=change_data[0])
      

      token_invalid_1=client.post('/api/change',data=change_data[0], headers=wrheaders)
      token_invalid_2=client.post('/api/change',data=change_data[1], headers=wrheaders)
      

      token_valid_1=client.post('/api/change',data=change_data[0], headers=mheader)
      token_valid_2=client.post('/api/change',data=change_data[1],headers=mheader)
      
      
      #############################################################################
      
      assert no_token_valid.status_code == 401
      assert token_invalid_1.status_code == 500
      assert token_invalid_2.status_code == 403
      assert token_valid_1.status_code == 201 
      assert token_valid_2.status_code == 403

##this is dropping all database at the end of the tests
