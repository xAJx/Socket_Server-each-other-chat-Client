# Client_Tcp_互相聊天_一人一句話
import socket               # 匯入雙方 ip、port 溝通 專用 函示庫  

ip = "127.0.0.1"            # 在任何地方，都能用自己的電腦跑，特殊 ip 位址
# ip = "192.168.95.176"     # 自己電腦 當 client 時，要輸入 欲連線 的 對方 Server ip

port = 9456                 # 設定雙方連線的 port，客戶、伺服器端 要一樣，最大數值可以到好幾萬

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))        # [客戶端 專屬語法]，需要 雙括號  設定 連接 對方的 ip、port

while True:
    data = input("please enter message")            # 設定 手動輸入 變數、指定文字訊息 印出  
    s.send(data.encode())                           # 透過 手動輸入變數 裡面的 [文字訊息] 進行 [傳送的編碼處理]

    if data == "-1":                                # 設定 當 手動輸入 變數值等於 (-1) 時，取消 與對方 機台 ip 連線
        break
    receiveData = s.recv(999)                       # recv ()裡面 是指 字串 限定的字數，中文 就要再除以 3
    print("receive data is "+receiveData.decode())  # 接收訊息，印出 對方機台 ip 打的文字訊息 [進行解碼]

s.close()                                           # 關閉 本 ip 機台
