if __name__ == '__main__':
    import systemd.daemon, initio, redis

    print('Startup')
    initio.init(Servos=True)
    initio.setServo(0, 0)
    initio.setServo(1, 0)
    r = redis.Redis(host='192.168.0.1', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('jaxx')
    print('Startup complete')
    systemd.daemon.notify('READY=1')

    try:
        for message in p.listen():
            cmd = message["data"]
            angles = cmd.split(',')
            initio.setServo(0, int(angles[0]))
            initio.setServo(1, int(angles[1]))
    except:
        p.close()
        initio.setServo(0, 0)
        initio.setServo(1, 0)
        initio.cleanup()
        print("Goodbye")