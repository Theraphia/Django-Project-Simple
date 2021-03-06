from django.db.models.query import QuerySet
from django.http import HttpResponse

from mainpage.models import Article, Comment, LikeList
from login.models import NumCounter, MyUser
from login.token import check_token


def user_authentication(request) -> dict:
    """
    用于检验用户的身份
    :param request:
    :return: {
        返回验证的结果和用户名
    }
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    if (token is None) or (len(str(token)) < 5):
        return {
            "result": False,
            "username": None
        }
    res = check_token(token)
    return {
        "result": res[0],
        "username": res[1]
    }
