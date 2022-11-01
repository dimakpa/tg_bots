from instapy import InstaPy
from tkinter import *
import requests
import os
from subprocess import call
root = Tk()


def button_click_autorization():
    login = loginInput.get()
    info_str = f'{str(login)}'
    f = open('login.txt', 'w')
    f.write(info_str)
    f.close()

    password = passInput.get()
    info_str = f'{str(password)}'
    fp = open('password.txt', 'w')
    fp.write(info_str)
    fp.close()

def button_click_comments():
    coment = comentInput.get()
    info_str = f'{str(coment)}'
    f = open('coments.txt', 'a')
    f.write(info_str + '\n')
    f.close()

def button_click_comments_del():
    with open('coments.txt', 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]

    with open('coments.txt', 'w') as f:
        f.writelines(lines)
    f.close()

def button_click_comments_show():
    os.startfile(r'coments.txt')

def button_click_users():
    acc = usersInput.get()
    info_str = f'{str(acc)}'
    f = open('znam_prov.txt', 'a')
    f.write(info_str + '\n')
    f.close()

def button_click_users_del():
    with open('znam_prov.txt', 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]

    with open('znam_prov.txt', 'w') as f:
        f.writelines(lines)
    f.close()

def button_click_users_show():
    os.startfile(r'znam_prov.txt')

def button_click_hashtags():
    hashtags = hashtagInput.get()
    info_str = f'{str(hashtags)}'
    f = open('hashtags.txt', 'a')
    f.write(info_str + '\n')
    f.close()

def button_click_hashtags_show():
    os.startfile(r'hashtags.txt')

def button_click_hashtags_del():
    with open('hashtags.txt', 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]

    with open('hashtags.txt', 'w') as f:
        f.writelines(lines)
    f.close()

def start():


    f = open('login.txt', 'r')
    login = f.read()
    f.close()

    fp = open('password.txt', 'r')
    password = fp.read()
    fp.close()

    session = InstaPy(username=login, password=password).login()
    session.login()
    session.set_action_delays(enabled=True,
                           like=3,
                           comment=5,
                           follow=100,
                           unfollow=100,
                           story=10)
    nunu = 1
    while nunu < 10:

        hashtags = session.target_list("hashtags.txt")
        users = session.target_list("znam_prov.txt")
        comments = session.target_list("coments.txt")

        session.follow_by_list(users, times=6, sleep_delay=600, interact=False)

        session.like_by_tags(hashtags, amount=200)
        session.set_delimit_liking(True, 200, 20)

        session.set_do_comment(enabled=True, percentage=50)
        session.set_do_like(enabled=True, percentage=90)

        session.set_comments(comments)

        users_unf = session.target_list("znam_prov.txt")
        session.unfollow_users(amount=84, custom_list_enabled=True, custom_list=users_unf, custom_list_param="all",
                           style="RANDOM", unfollow_after=55 * 60 * 60, sleep_delay=600)



        session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21, peak_likes_daily=300, peak_likes_hourly=50, peak_unfollows_daily=30)#КВОТЫ ДЛЯ БОТА


    session.end()

# Указываем фоновый цвет
root['bg'] = 'floral white'
# Указываем название окна
root.title('Instabot')
# Указываем размеры окна
root.geometry('500x700')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)


# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_autorization = Frame(root, bg='coral1', bd=5)
frame_autorization.place(relx=0.15, rely=0.01, relwidth=0.7, relheight=0.15)

frame_users = Frame(root, bg='coral1', bd=5)
frame_users.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.15)

frame_coments = Frame(root, bg='coral1', bd=5)
frame_coments.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.15)

frame_hashtag = Frame(root, bg='coral1', bd=5)
frame_hashtag.place(relx=0.15, rely=0.6, relwidth=0.7, relheight=0.15)

frame_start = Frame(root, bg='coral1', bd=5)
frame_start.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)



# Создаем текстовое поле для получения данных от пользователя
# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack()
# Размещение этого объекта, всегда нужно прописывать

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
#info = Label(frame_top, text='comments', bg='#ffb700', font=40)
#info.pack()

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_autorization, text='Write login and pass', command=button_click_autorization)
btn.pack()

loginInput = Entry(frame_autorization, bg="grey")
loginInput.pack()

passInput = Entry(frame_autorization, bg="grey", show='*')
passInput.pack()



btn = Button(frame_coments, text='Write down comment', command=button_click_comments)
btn.pack()

comentInput = Entry(frame_coments, bg="white")
comentInput.pack()

btn = Button(frame_coments, text='delete comment', command=button_click_comments_del)
btn.pack()

btn = Button(frame_coments, text='show coments', command=button_click_comments_show)
btn.pack()


btn = Button(frame_users, text='Write down celebrities', command=button_click_users)
btn.pack()

usersInput = Entry(frame_users, bg="white")
usersInput.pack()

btn = Button(frame_users, text='delete users', command=button_click_users_del)
btn.pack()

btn = Button(frame_users, text='show users', command=button_click_users_show)
btn.pack()



btn = Button(frame_hashtag, text='Write down hashtag', command=button_click_hashtags)
btn.pack()

hashtagInput = Entry(frame_hashtag, bg="white")
hashtagInput.pack()

btn = Button(frame_hashtag, text='delete hashtag', command=button_click_hashtags_del)
btn.pack()

btn = Button(frame_hashtag, text='show hashtag', command=button_click_hashtags_show)
btn.pack()


btn = Button(frame_start, text='Start', command=start)
btn.pack()



root.mainloop()
