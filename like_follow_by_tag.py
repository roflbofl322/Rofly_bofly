from instapy import *
from var import *

#Лайкать и фолловить людей с определенным тегом

#Не тогай
session = InstaPy(username=inst_log, password=inst_pass)
session.login()

#Взаимодействовать только с пользователями которые подходят по количество подписок/фоловеров
session.set_relationship_bounds(enabled=True,potency_ratio=None,delimit_by_numbers=True,max_followers=None,max_following=None,min_followers=150,min_following=50)

#Взаимодействовать только с пользователями которые подходят по количеству постов
session.set_relationship_bounds(min_posts=10, max_posts=None)


#Процент того как часто будут ставится лайки.
session.set_do_like(True, percentage=70 )

#Фоловится ли
session.set_do_follow(enabled=True, percentage=100 , times=1)

#Лайкать юзеров по оппределенному хештегу
session.like_by_tags(tag_list, amount= 10 , skip_top_posts= False , randomize= True)

