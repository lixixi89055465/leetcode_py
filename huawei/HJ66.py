import re


def func(us=''):
    ml_dict = {
        'reset': 'reset what',
        'reset board': 'board fault',
        'board add': 'where to add',
        'board delete': 'no board at all',
        'reboot backplane': 'impossible',
        'backplane abort': 'install first'
    }
    default_comm = 'unknown command'
    if ' ' in us:
        us_list = us.split()
        ret = [i for i in ml_dict.keys() if ' ' in i and re.match(us_list[0], i) and re.search(' ' + us_list[1], i)]
        if len(ret) == 1:
            print(ml_dict.get(ret[0]))
        else:
            print(default_comm)
    else:
        ret = [i for i in ml_dict.keys() if ' ' not in i and re.match(us, i)]
        if len(ret) == 1:
            print(ml_dict.get(ret[0]))
        else:
            print(default_comm)


while True:
    try:
        func(input())
    except:
        break
