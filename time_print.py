import datetime

def main():
  now = datetime.datetime.now()

  print("Current date and time: ")
  print(now.strftime('%Y-%m-%d %H:%M:%S'))
  print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
  
if __name__ == '__main__':
  main()
