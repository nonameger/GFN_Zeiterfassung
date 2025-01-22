from Log import log_pre, logout
from data import get_browser, get_login

def m_logout():
    data = get_login()
    bw = get_browser()

    logout(log_pre(data[0], data[1], bw))