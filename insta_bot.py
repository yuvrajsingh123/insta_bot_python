# including libraries
import requests,urllib
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from Test import get_keywords
from Clarify_Example import get_keywords_from_image

# Access Token of an application

APP_ACCESS_TOKEN = '5684485588.34768f4.28c3c41a0e0d4a3daf8d8e21e6cd0e8d'
APP_ACCESS_TOKEN_PD = 'DRmg2bz8D85xI8Tm0pSCYOITFGx1EyirLk1nhhGduJs'
BASE_URL = 'https://api.instagram.com/v1/'
BASE_URL_PD = 'https://apis.paralleldots.com/'


# Function for fetching own details
def self_info():
    # get the request url
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)

    # print the request url
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    # check if the request status is OK or not
    if user_info["meta"]["code"] == 200:
        # check if user exists or not
        if len(user_info["data"]):
            # print the details
            print 'Username: %s' % (user_info['data']['username'])
            print 'Id: %s' % (user_info['data']['id'])
            print 'Profile picture: %s' % (user_info['data']['profile_picture'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'
        # display invalid request
        print "INVALID REQUEST!!!"
        print "Please check the request"

# Function for obtaining user-id from username
def get_user_id(insta_username):
    # get request url
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)

    # print the request url
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    # check if request status is OK or not
    if user_info["meta"]["code"] == 200:
        # check if user data exists
        if len(user_info["data"]):
            # print the userid
            return user_info["data"][0]["id"]
        else:
            return None
    else:
        # display invalid request
        print "INVALID REQUEST!!!Please try again"
        exit()

# Function for getting other user's information

def get_user_info(insta_username):
    # define user id
    user_id = get_user_id(insta_username)

    # check if there is userid or not
    if user_id == None:
        print "User doesn't exist!!!"
        exit()

    # define request url
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id,APP_ACCESS_TOKEN)

    # print the request url
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    # check if request status is OK or not
    if user_info["meta"]["code"] == 200:
        # check if data exists for the user
        if len(user_info["data"]):
            # print the details of the user
            print 'Username: %s' % (user_info['data']['username'])
            print 'Id: %s' % (user_info['data']['id'])
            print 'Profile picture: %s' % (user_info['data']['profile_picture'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            # display that no data is available for the user
            print "No data is available for this particular user!!!"
    else:
            # show invalid request message
            print "INVALID REQUEST!!!Please try again"


# Function to get own recent post
def get_own_post():

    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print "GET request url: %s" % (request_url)
    own_media = requests.get(request_url).json()


    #Performing handling of different edge cases and scenarios
    #you can give extension of an image according to your requirement, it depends on the image
    #you want to download
    choice_image_extension = raw_input("Enter the format you want for an image")

        # check if request is valid
    if own_media["meta"]["code"] == 200:
                  # check if own_media has data
                  if len(own_media["data"]):
                      # define name of the image
                      image_name = own_media["data"][0]["id"] +'.'+ choice_image_extension
                      # define url of the image
                      image_url = own_media["data"][0]["images"]["standard_resolution"]["url"]
                      # retreive the image post
                      urllib.urlretrieve(image_url, image_name)
                      # print an appropriate message
                      print "Your image has been downloaded!!!"
                  else:
                    print "Post does not exist!"
    else:
        print "INVALID REQUEST!!!!Please try again"


# Function to get user recent post
def get_user_post(insta_username):
    # retrieve an user id
    user_id = get_user_id(insta_username)

    # check if userid is none
    if user_id == None:
        # print the user does not exist
        print "User does not exist!!!"
        exit()

    # define request url
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    # display request url
    print "GET request url: %s" % (request_url)

    # define a variable for media
    user_media = requests.get(request_url).json()

    # Performing handling of different edge cases and scenarios
    # you can give extension of an image according to your requirement, it depends on the image
    # you want to download


    want_image_extension= raw_input("Enter the format you want for an image")

    # check if request is valid
    if user_media["meta"]["code"] == 200:

        # check if user_media has data
        if len(user_media["data"]):

            # define the name for the image
            image_name = user_media["data"][0]["id"] +'.'+ want_image_extension
            # define the url for the image
            image_url = user_media["data"][0]["images"]["standard_resolution"]["url"]
            # retrieve the image
            urllib.urlretrieve(image_url, image_name)
            # print a suitable message
            print "The image has been downloaded!!!"
        else:
            print "No recent posts!!!"
    else:
        print "INVALID REQUEST"


# Function to get id of recent post by the user using username
def get_post_id(insta_username):
    # retreiving the user id
    user_id = get_user_id(insta_username)
    # check if user id is None
    if user_id == None:
        # display that user doesn't exist
        print "User does not exist!!!"
        exit()
    # define a request url
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    # print the get request url
    print "GET request url : %s" % (request_url)
    user_media = requests.get(request_url).json()

    # check if request status is OK
    if user_media["meta"]["code"] == 200:
        # check if user_media has data
        if len(user_media["data"]):
            # return the post id
            return user_media["data"][0]["id"]
        # if user_media doesn't has data
        else:
            # display an appropriate message
            print "There is no recent post of the user!!!"
            exit()
    # if request status is not OK
    else:
        # display invalid reuest
        print "INVALID REQUEST!!!"
        exit()


# Function to like a post by user
def like_a_post(insta_username):
    #accessing media_id
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    # if request status is OK
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:

        print 'Your like was unsuccessful. Try again!'


# Function to comment on user's post
def post_a_comment(insta_username):
    # retrieve media id
    media_id = get_post_id(insta_username)
    # accept comment text from the user
    comment_text = raw_input("Your comment: ")
    # define the payload
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    # define the request url
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    # print request url
    print "POST request url: %s" % (request_url)
    # make a comment
    make_comment = requests.post(request_url, payload).json()
    # check if make_comment status is OK
    if make_comment["meta"]["code"] == 200:
        # print comment successful
        print "Successfully added a new comment!!!"
    else:
        # print unsuccessful comment
        print "Unable to add comment. Try again!!!"


# function to get list of users who like user's media

def get_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
     #accessing list through get request
    print 'GET request url : %s' % (request_url)
    like_list = requests.get(request_url).json()
    print like_list
    # check if make_comment status is OK
    if like_list['meta']['code'] == 200:
        if len(like_list['data']):
            for i in range(0,len(like_list['data'])):
                #printing users details
                print 'Username: %s' % (like_list['data'][i]['username'])
                print 'Fullname: %s' % (like_list['data'][i]['full_name'])
        else:
            print 'There is no like for this user media!'
    else:
        print 'Query was unsuccessful!'


# function to get list of comments
def get_comment_list(insta_username):
    # retrieve the media id
    media_id = get_post_id(insta_username)
    # check if media id does not exist
    if media_id == None:
        # print suitable message
        print "No post found!!!"
        # exit the function
        exit()
    # define request url
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    # print the get request
    print "GET request url: %s" % (request_url)
    # define user media
    user_media = requests.get(request_url).json()
    # check if request status is OK
    if user_media["meta"]["code"] == 200:
        # check if user_media has data
        if len(user_media["data"]):
            # print the comments
            print "Comments: %s" % (user_media["data"][0]["text"])
        # if user_media does not have data
        else:
            # display that no comments found
            print "No comments found!!!"
    # if request status is not OK
    else:
        # display invalid request
        print "INVALID REQUEST!!!"


# function to delete negative comment

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    #accessing comment_info through get request
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    #to check if comment status is ok or not
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #loop for accessing comment_text
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                #condition for printing negative comment if any and deleting it
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()
                        #if status is ok, then comment will be deleted else not
                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

#providing offers to the pizza cutomers if found
def post_promotional_comment(insta_promotional_message, insta_username):
    media_id = get_post_id(insta_username)
    payload = {"access_token": APP_ACCESS_TOKEN, "text": insta_promotional_message}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()
#if status is ok
    if make_comment['meta']['code'] == 200:
        print "Successfully added a promotional comment!"
    #not ok
    else:

        print "Unable to add comment. Try again!"


# function to do marketing
def insta_marketing(insta_keyword,insta_promotional_message,insta_username):
    # Analyze comments
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    print comment_info
    if comment_info['meta']['code'] == 200:

        if len(comment_info['data']):
#running loop for accessing comment_words
            for index_var in range(0, len(comment_info['data'])):
                comment_text = comment_info['data'][index_var]['text']
                print comment_text
                comment_words = comment_text.split()
                #printing comment_words after splitting it
                print comment_words
                for i in range(0,comment_words.__len__()):
                    #if condition matches, then the below function will be called to send offers to the pizza customers
                    if(comment_words[i] == insta_keyword):
                        post_promotional_comment(insta_promotional_message,insta_username)
                        break
    else:
        print 'Status code other than 200 received'

    # Analyze tags and captions

    #Enter caption and tags as 'pizza' in order to execute the objective
    #Then we will give that particular user discounts that we provide
    request_url = (BASE_URL+'media/%s?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    media_data=requests.get(request_url).json()
        #if some data is there
    if(media_data) is not None:

        print media_data
#checking status is ok or not
        if (media_data['meta']['code']== 200):
#checking tags if any else it will print 'not matched'
            if len(media_data['data']['tags']):
                insta_tag = media_data['data']['tags']
                for index_var in range(0,insta_tag.__len__()):
                    if insta_tag[index_var]==insta_keyword:
                        print insta_tag[index_var]
                        post_promotional_comment(insta_promotional_message,insta_username)
                        break
                    else:
                        print 'Not matched'
            else:
                print 'No tags'
#checking caption if any else it will print 'not matched'

            if  (media_data['data']['caption']) is  not  None:
                insta_caption = media_data['data']['caption']['text']
                type(insta_caption)
                insta_caption_words = insta_caption.split()

                # using paralleldots to check keywords of caption
                c= insta_caption.encode('ascii','ignore')
                print type(c)
                op_of_func=get_keywords(c ,APP_ACCESS_TOKEN_PD)

                if(len(op_of_func) >0):
                    keywords_in_caption = op_of_func[0]

                    print op_of_func[0]
                    print type(op_of_func)
                    for p in range(0, keywords_in_caption.__len__()):
                 #if keywoord are matched then the below function will be called
                        if (keywords_in_caption[p] == insta_keyword):
                            print keywords_in_caption[p]
                            post_promotional_comment(insta_promotional_message, insta_username)
                            break
                        else:
                            print 'Not matched'

                # directly checking all words of caption
                for p in range(0, insta_caption_words.__len__()):
                    if (insta_caption_words[p] == insta_keyword):
                        print insta_caption_words[p]
                        post_promotional_comment(insta_promotional_message, insta_username)
                        break
                    else:
                        print 'Not matched'
            else:
                print 'No caption'
        else:
            'Status code other than 200 received'


        #Image processing using Clarifai
        url_of_image1 =media_data['data']['images']['standard_resolution']['url']
        print type(url_of_image1)
        url_of_image=url_of_image1.encode('ascii','ignore')
        print type(url_of_image)

        image_keywords=get_keywords_from_image(url_of_image)
        #printing image_keywords it has
        print image_keywords

        print type(image_keywords)
        arr_of_dict=image_keywords['outputs'][0]['data']['concepts']
        print type(arr_of_dict)
        print arr_of_dict
#loop for printing keyword and apply a if check on it
        for i in range(0,len(arr_of_dict)):
            keyword = arr_of_dict[i]['name']
            print keyword
            #if keyword matches then the below function will be invoked
            if (keyword == insta_keyword):
                print arr_of_dict[i]['name']
                post_promotional_comment(insta_promotional_message, insta_username)
                break
            else:
                print 'Not matched'
    else:
        print 'media doesn\'t exist'

# Function to start the bot and presenting a menu

def start_bot():
    # continue until the condition becomes false
    while True:

        print '\n'

        # greeting the user
        print 'Hey! Welcome to instaBot!'

        # displaying the menu
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get a list of people who have liked the recent post of a user\n"
        print "f.Like the recent post of a user\n"
        print "g.Get a list of comments on the recent post of a user\n"
        print "h.Make a comment on the recent post of a user\n"
        print "i.Delete negative comments from the recent post of a user\n"
        print "j.To do marketing using specific keywords"
        print "k. To exit"

        # accept user input
        choice=raw_input(colored("Enter choice: ",'red'))


        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input(colored("Enter the username of the user: ",'red'))
            get_user_info(insta_username)
        elif choice=="c":
            get_own_post()
        elif choice=="d":
            insta_username = raw_input(colored("Enter the username of the user: ",'cyan'))
            get_user_post(insta_username)
        elif choice=="e":
            insta_username = raw_input(colored("Enter the username of the user: ",'yellow'))
            get_like_list(insta_username)
        elif choice=="f":
            insta_username = raw_input(colored("Enter the username of the user: ",'grey'))
            like_a_post(insta_username)
        elif choice=="g":
            insta_username = raw_input(colored("Enter the username of the user: ",'green'))
            get_comment_list(insta_username)
        elif choice=="h":
            insta_username = raw_input(colored("Enter the username of the user: ",'cyan'))
            post_a_comment(insta_username)
        elif choice=="i":
            insta_username = raw_input(colored("Enter the username of the user: ",'yellow'))
            delete_negative_comment(insta_username)
        elif choice == "j":
            insta_keyword = raw_input("Enter the keyword to be searched :")
            insta_promotional_message = raw_input("Enter the text to be commented :")
            insta_username = raw_input(colored("Enter the username of the user: ",'magenta'))

            #all the above inputs will be sen as a parameters in the below function
            insta_marketing(insta_keyword,insta_promotional_message,insta_username)
        elif choice=="k":
            exit()
        else:
            print "wrong choice"

start_bot()





