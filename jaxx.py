import systemd.daemon
import initio
import redis


def execute():
    print('Startup')

    x = {'init': 0, 'max': 80, 'min': -80}
    y = {'init': 10, 'max': 80, 'min': -25}

    initio.init(Servos=True)
    initio.setServo(0, x['init'])
    initio.setServo(1, y['init'])

    r = redis.Redis(host='192.168.0.1', port=6379,
                    db=0, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('jaxx')

    r.publish('services', 'jaxx.on')
    systemd.daemon.notify('READY=1')
    print('Startup complete')

    try:
        for message in p.listen():
            cmd = message['data']

            if cmd == '0':
                x_angle = x['init']
                y_angle = y['init']
            else:
                angles = cmd.split(',')
                x_angle = int(angles[0])
                y_angle = int(angles[1])

            # Make sure it's valid
            if x_angle > x['max']:
                x_angle = x['max']
            if x_angle < x['min']:
                x_angle = x['min']
            if y_angle > y['max']:
                y_angle = y['max']
            if y_angle < y['min']:
                y_angle = y['min']

            initio.setServo(0, x_angle)
            initio.setServo(1, y_angle)
    except:
        p.close()

        initio.setServo(0, x['init'])
        initio.setServo(1, y['init'])
        initio.cleanup()

        r.publish('services', 'jaxx.off')
        print('Goodbye')


if __name__ == '__main__':
    execute()
