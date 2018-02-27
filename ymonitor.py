from flask import Flask, request, jsonify, make_response, render_template

import psutil

app = Flask(__name__)


def cpu_stat():
    stat = {}

    cpu = psutil.cpu_times()
    stat['user'] = cpu.user
    stat['system'] = cpu.system
    stat['idle'] = cpu.idle

    stat['iowait'] = cpu.iowait

    stat['irq'] = cpu.irq
    stat['softirq'] = cpu.softirq

    return stat


def mem_stat():
    stat = {}

    mem = psutil.virtual_memory()

    # 总内存
    stat['total'] = mem.total

    # 总内存的组成部分
    stat['used'] = mem.used
    stat['free'] = mem.free
    stat['buffers'] = mem.buffers
    stat['cached'] = mem.cached

    stat['available'] = mem.available
    stat['used_percent'] = mem.percent

    return stat


def diskio_stat():
    stat = {}

    diskio = psutil.disk_io_counters()
    stat['read_count'] = diskio.read_count
    stat['write_count'] = diskio.write_count
    stat['read_bytes'] = diskio.read_bytes
    stat['write_bytes'] = diskio.write_bytes

    return stat


def netio_stat():
    stat = []
    netios = psutil.net_io_counters(pernic=True)

    for netcard, netio in netios.items():
        one_stat = {}
        one_stat['netcatd'] = netcard
        one_stat['bytes_sent'] = netio.bytes_sent
        one_stat['bytes_recv'] = netio.bytes_recv
        one_stat['packets_sent'] = netio.packets_sent
        one_stat['packets_recv'] = netio.packets_recv
        stat.append(one_stat)

    return stat


def connections_stat():
    stat = []

    connections = psutil.net_connections(kind='inet')

    for con in connections:
        one_stat = {}
        # one_stat['fd'] = con.fd
        one_stat['type'] = str(con.type)
        one_stat['status'] = con.status

        laddr = {}
        laddr['ip'] = con.laddr.ip if con.laddr else ''
        laddr['port'] = con.laddr.port if con.laddr else 0
        one_stat['laddr'] = laddr

        raddr = {}
        raddr['ip'] = con.raddr.ip if con.raddr else ''
        raddr['port'] = con.raddr.port if con.raddr else 0
        one_stat['raddr'] = raddr

        stat.append(one_stat)

    return stat


@app.route('/api/cpu')
def get_cpu_stat():
    stat = cpu_stat()
    return jsonify({'stat': stat})


@app.route('/api/mem')
def get_mem_stat():
    stat = mem_stat()
    return jsonify({'stat': stat})


@app.route('/api/diskio')
def get_diskio_stat():
    stat = diskio_stat()
    return jsonify({'stat': stat})


@app.route('/api/netio')
def get_netio_stat():
    stat = netio_stat()
    return jsonify({'stat': stat})


@app.route('/api/connections')
def get_connections_stat():
    stat = connections_stat()
    return jsonify({'stat': stat})

@app.route('/')
def index():
    return make_response(open('templates/index.html').read())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
