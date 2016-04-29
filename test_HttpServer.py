import HttpServer
import json


class TestHttpServer:

    def setup_method(self, method):
        self.app = HttpServer.app
        self.app.config['TESTING'] = True
        server_name = "127.0.0.1:7000"
        self.URL = "http://" + server_name
        self.app.config['SERVER_NAME'] = server_name


    def test_app_is_running(self):
        client = self.app.test_client()

        assert client.get(self.URL + "/").status_code == 200

    def test_register_team(self):
        client = self.app.test_client()

        assert client.post(self.URL + "/robots/team1").status_code == 200
        response = client.post(self.URL + "/robots/team1")
        assert response.status_code == 200
        assert response.data == "SORRY"


    def test_register_hex(self):
        client = self.app.test_client()
        assert client.post(self.URL + "/robots/team3", data="0xdede12").data == "OK"
        # assert client.post(self.URL + "/robots/team2", data="0xde123").data == "OK"

