import psutil

def get_process_info_by_ip_port(dst_ip=None, dst_port=None):
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            ip, port = conn.raddr
            if ip == dst_ip or port == dst_port:
                pid = conn.pid
                if pid:
                    try:
                        p = psutil.Process(pid)
                        return {
                            "pid": pid,
                            "process_name": p.name()
                        }
                    except:
                        return {"pid": pid}
    return None
