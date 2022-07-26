from flask import request


#from constants import ENDPOINT_FILTER_BY_NAME


from uow import UserUOW

uow = UserUOW('sqlite:///:memory:')

print(uow.user.get_all())