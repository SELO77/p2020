import time



ms_now = lambda :int(time.time() * 1000)


def counter(fnc):
    def wrapper(*args, **kwargs):
        st = ms_now()
        fnc(*args, **kwargs)
        print(ms_now() - st)
    return wrapper


@counter
def test_loads(parser, data):
    parser.loads(data)


def main():
    import json
    import simplejson
    import ujson
    with open('sample.json', 'r') as f:
        f = f.read()

        # test_loads(json, f) # 70 ~ 71
        # test_loads(simplejson, f) # 65 ~ 67
        # test_loads(ujson, f) # 70 ~ 74


if __name__ == '__main__':
    main()

