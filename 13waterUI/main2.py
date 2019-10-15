import load
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import main
token = ''
pid=-1

    def read(self):
        url = "https://api.shisanshui.rtxux.xyz/auth/register"
        payload = "{\"username\":\"" + account1+"\",\"password\":\""+password1+"\"}"
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        res = json.loads(response.text)
        status=res['status']
        print(response.text)
        if status==0:
            hope2.show()
            self.close()
        else:
            hope1.show()

class P1(QtWidgets.QDialog,load.Ui_h1):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def go_1(self):
        url = "https://api.shisanshui.rtxux.xyz/auth/login"
        headers = {
            'content-type': 'application/json'
        }
        account2 = self.lineEdit.text()
        password2 = self.lineEdit_2.text()
        data = {
            "username":account2,
            "password": password2
        }
        respond = requests.post(url, json=data).text
        print(respond)
        res = json.loads(respond)
        status = -1
        status = res['status']
        if status == 0:
            token = res['data']['token']
            pid = res['data']['user_id']
            win2.show()
            self.close()
        else:
            hope3.show()




    def go(self):
        win=P()
        win.show()
        win.read()


class P2(QtWidgets.QDialog,home.Ui_h2):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def go_2(self):
        win3.show()

    def go_3(self):
        win4.show()

    def go_4(self):
        win5.show()
    def logout(self):
        url = "https://api.shisanshui.rtxux.xyz/auth/logout"
        headers = {'x-auth-token': token}
        response = requests.request("POST", url, headers=headers)
        print(response.text)
        win2.close()

class P3(QtWidgets.QDialog,poke.Ui_h3):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

class P4(QtWidgets.QDialog,record.Ui_h4):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def httpP4(self):
        print(token)
        url = "https://api.shisanshui.rtxux.xyz/history"
        querystring = {"page": "1", "limit": "3", "player_id": pid}
        headers = {'x-auth-token': token}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        tx=json.loads(response.text)
        res=tx['data']
        print(res)
        '''self.textBrowser.setText(str(res[0]['id']))
        self.textBrowser_2.setText(str(res[0]['card']))
        self.textBrowser_3.setText(str(res[0]['score']))
        self.textBrowser_4.setText(str(res[0]['timestamp']))'''
    def renew(self):
        self.httpP4()


class P5(QtWidgets.QDialog,rank.Ui_h5):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
    def httpP5(self):
        url = "https://api.shisanshui.rtxux.xyz/rank"
        response = requests.get(url, headers={"X-Auth-Token": token}).text
        res = json.loads(response)
        self.textBrowser.setText(str(res[0]['player_id']))
        self.textBrowser_2.setText(str(res[0]['score']))
        self.textBrowser_3.setText(str(res[0]['name']))
        self.textBrowser_4.setText(str(res[1]['player_id']))
        self.textBrowser_5.setText(str(res[1]['score']))
        self.textBrowser_6.setText(str(res[1]['name']))
        self.textBrowser_7.setText(str(res[2]['player_id']))
        self.textBrowser_8.setText(str(res[2]['score']))
        self.textBrowser_9.setText(str(res[2]['name']))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    hope1=m1()
    hope2=m2()
    hope3=m3()
    win1 = P1()
    win2 = P2()
    win3 = P3()
    win5 = P5()
    win1.show()
    sys.exit(app.exec_())