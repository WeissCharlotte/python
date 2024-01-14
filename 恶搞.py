import os

# 打开多个命令提示符窗口
for i in range(10):
   os.system('start cmd')



import socket

def get_user_ip():
  try:
      # 获取本地计算机名称
      hostname = socket.gethostname()
      # 获取本地计算机 IP 地址
      ip_address = socket.gethostbyname(hostname)
      return ip_address
  except Exception as e:
      print("获取 IP 地址时发生错误:", e)
      return None

if __name__ == "__main__":
  user_ip = get_user_ip()
  if user_ip:
      print("您的 IP 地址是:", user_ip)
  else:
      print("无法获取 IP 地址。")

import subprocess

def computer():
    # 执行 shutdown 命令来注销电脑
    subprocess.run(['shutdown', '-l'])

if __name__ == "__main__":
     #注销电脑
   computer()
