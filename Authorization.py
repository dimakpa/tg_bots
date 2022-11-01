import tweepy

API_KEY = "YOUR_API_KEY" #жду подтверждения API разработчика
API_SECRET = "YOUR_API_SECRET"

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#####################################
api = tweepy.API(auth)

user = api.get_user('dimakpa')

print(user.screen_name, user.followers_count) #од возвращает имя пользователя и количество подписчиков
#####################################
api = tweepy.API(auth)

api.update_with_media('C:/images/boat.jpg', 'Пора в путешествие!')# загрузка поста с картинкой
#https://bablofil.com/bot-dlya-twitter/