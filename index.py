import redis

if __name__ == '__main__':
    try:
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set('foo', 'bar')
        print(r.get('foo'))
    except Exception as e:
        print(e)