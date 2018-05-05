#coding:utf8
#qpy:2
#qpy:console
import sys
from androidhelper import Andoid
reload(sys)
sys.setdefaultencoding('utf-8')
text = raw_input("Text: ")
def pesan(t):
    droid = Android()
    p = "\u200e\u200f" * 1000
    droid.setClipboard(t.replace(" "," "+p))
if __name__ == "__main__":
    pesan(text)
