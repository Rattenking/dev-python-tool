#!/usr/bin/env python
"""
@Author  ：Rattenking
@Date    ：2021/06/02 15:42
@CSDN	 ：https://blog.csdn.net/m0_38082783
"""
# XbQL3xjV9yBw28yJ2HEaWuzw
import time
import subprocess

def get_current_time_stamp():
  times = time.time()
  time_stamp = int(round(times * 1000))
  return time_stamp

def verify_password(pwd):
  print(f'验证的密码是：{pwd}')
  cmd = f'7z t -p{pwd} ./test.zip'
  status = subprocess.call(cmd)
  return status

def unzip_file_other_folder(pwd):
  print(f'正确的密码是：{pwd}')
  cmd = f'7z x -p{pwd} ./test.zip -y -aos -o"./all/"'
  subprocess.call(cmd)

def get_all_possible_password():
  for i in range(1000000):
    pwd = str(("%06d"%i))
    status = verify_password(pwd)
    if status == 0:
      unzip_file_other_folder(pwd)
      break

if __name__ == "__main__":
  start = get_current_time_stamp()
  get_all_possible_password()
  end = get_current_time_stamp()
  print(f"解压压缩包用时：{end - start}ms")
