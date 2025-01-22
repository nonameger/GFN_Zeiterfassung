from Log import log_pre, login
from data import get_login, get_browser

def m_login():
    data = get_login()
    bw = get_browser()

    login(log_pre(data[0], data[1], bw))