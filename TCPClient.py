from socket import *

host_name = "192.168.168.129" #机器人IP
port_num = 29999            #Dashborad服务端口
ClientSocket = socket(AF_INET,SOCK_STREAM) 
ClientSocket.connect((host_name,port_num))
upperMessage = ClientSocket.recv(1024).decode() #第一次接收连接29999端口状态返回值
print("The message from Server:"+upperMessage)

message ="load gripper.urp\r\n"    #参考Dashboard文档内容（此为加载名为“gripper.urp”的UR程序）
ClientSocket.send(message.encode())
upperMessage = ClientSocket.recv(1024).decode() #接收发送29999命令返回值
print("The message from Server:"+upperMessage)

message ="play\r\n"    #运行程序
ClientSocket.send(message.encode())
upperMessage = ClientSocket.recv(1024).decode() 
print("The message from Server:"+upperMessage)

ClientSocket.close()
