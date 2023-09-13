# Server_Tcp_互相聊天_一人一句話
import socket            # 匯入雙方 ip、port 溝通 專用 函式庫  

ip = "127.0.0.1"         # 在任何地方，都能用自己的電腦跑，特殊 ip 位址
# ip = "192.168.95.25"   # 自己電腦當 Server時，要輸入自己當下的 ip

port = 2500             # 設定雙方連線的 port，客戶、伺服器端 要一樣，最大數值可以到好幾萬

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((ip, port))       # 需要 雙括號  設定 連接 對方的 ip、port， bind (綁定)
s.listen(5)              # [Server 端 專屬語法]，設定幾個人 可以連線

conn, addr = s.accept()  # 等待 被誰連上，接受 客戶 端 的 連接 請求，conn代表 client
print(" addr is "+ str(addr))


# inputData = conn.recv(9999)   # ()裡面 是指 字串 限定的字數，中文 就要再約略除以 3
# sendData = "哈囉，Jennifer，恭喜你連上 Server,I'm AJ"

i = 0

while True:
    while i < 99999:                                     # 設定 聊天 來回次數
        inputData = conn.recv(999)                       # recv ()裡面 是指 字串 限定的字數，中文 就要再除以 3
        print("receive Message is "+inputData.decode())  # 接收訊息，印出 對方機台 ip 打的文字訊息 [進行解碼]
            # if inputData.decode() == "-1" :
            #    break        
            # sendData = "I'm received it"
        sendData = input()                               # 設定 手動輸入 變數  
        conn.send(sendData.encode())                     # 透過 手動輸入變數 裡面的 [文字訊息] 進行 [傳送的編碼處理]

            # sendData = "哈囉，xxx classmate，恭喜你連上 Server,I'm AJ"
            # sendData = input(str())
        if sendData == "-2":                             # 設定 當 手動輸入 變數值等於 (-2) 時，取消 與對方 機台 ip 連線
            break                                        # 跳出迴圈
            # input(str(wer))  
            # conn.send(wer.encode())
        i = i + 1
    break                                                # 跳出 聊天 來回次數 的迴圈
    #while sendData == -1 :  
    #   if conn.send(sendData.encode()):

conn.close()                                             # 關閉 本 ip 機台


