# with open('h.txt','r') as f:
#     x=f.readlines()[-1]
#     if x!="m":
#         print('yes')
#     f.close()


from time import sleep
import urllib.request

def connect():
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False

# def work():
#     sleep(3)
#     print("working")

# # try:
# #     # while True:
# #         work()
# except:
#     while True:
#         if connect():
#             work()
#         # else

    
    
    # test
#     # print( "connected" if connect() else "no internet!" )
# def work():
#     try: 
#         while connect():
#             sleep(3)
#             print("working")
#     except:
#         sleep(3)
#         work()


# work()

# import urllib 
# import requests

# def wait_for_internet_connection():
#     while True:
#         try:
#             response = urllib.request.urlopen('http://8.8.8.8',timeout=1)
#             return
#         except urllib.request.URLError:
#             pass

# def main():
#     sleep(3)
#     print("tom")

# wait_for_internet_connection()
# main()



# def x():
#     while True:
        
#         return connect()

# if x()=='False':



# def pause():
#     try:
#         while connect()=='False':
#             print("oooooooooo")
#     except:
#      play() 


# def play():
#        try:
#         while connect():

#          print("aaaaaaaaa")
#        except:
#         pause()


# play()



def x():
    try:
        while connect():
            sleep(3)
            print("yes")
    except:
        sleep(3)
        print('noo0')
        x()

x()