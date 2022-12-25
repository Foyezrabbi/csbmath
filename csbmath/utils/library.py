from csbmath.utils.finder import google
from csbmath.utils.finder import baidu
from csbmath.utils.finder import bing


def get_emails_from_google(target):
    return google.search(target)

def get_emails_from_bing(target):
    return bing.search(target)

def get_emails_from_baidu(target):
    return baidu.search(target)