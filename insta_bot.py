import requests

ACCESS_TOKEN = '5684485588.34768f4.28c3c41a0e0d4a3daf8d8e21e6cd0e8d'

BASE_URL = 'https://api.instagram.com/v1/'





def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            print "Username: %s" %(user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["fullname"])
            print "Bio: %s" % (user_info["data"]["bio"])
            print "Website: %s" % (user_info["data"]["website"])
            print "Number of followers: %s" % (user_info["data"]["count"]["followed_by"])
            print "Number of post: s" % (user_info["data"]["count"]["media"])
            print "Number of people you are following: %s" % (user_info["data"]["count"]["follows"])
        else:
            print "User does not exist!!!"
    else:
        print "INVALID REQUEST!!!"
        print "Please check the request"




def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username,ACCESS_TOKEN)
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            return user_info["data"][0]["id"]
        else:
            return None
    else:
        print "INVALID REQUEST!!!Please try again"
        exit()




def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User doesn't exist!!!"
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id,ACCESS_TOKEN)
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            print "Username: %s" % (user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["fullname"])
            print "Bio: %s" % (user_info["data"]["bio"])
            print "Website: %s" % (user_info["data"]["website"])
            print "Number of followers: %s" % (user_info["data"]["count"]["followed_by"])
            print "Number of post: s" % (user_info["data"]["count"]["media"])
            print "Number of people you are following: %s" % (user_info["data"]["count"]["follows"])
        else:
            print "No data is available for this particular user!!!"
    else:
        print "INVALID REQUEST!!!Please try again"




def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Exit"

        choice=raw_input("Enter you choice: ")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)

        elif choice=="c":
            exit()
        else:
            print "wrong choice"

start_bot()