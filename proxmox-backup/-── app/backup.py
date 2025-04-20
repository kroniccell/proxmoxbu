import time
from proxmoxer import ProxmoxAPI

def get_vm_uptime(vmid):
    try:
        proxmox = ProxmoxAPI(CONFIG["PROXMOX_HOST"], user=CONFIG["USERNAME"], 
                            password=CONFIG["PASSWORD"], verify_ssl=False)
        vm = proxmox.nodes(CONFIG["NODE"]).qemu(vmid).status().current.get()
        return time.strftime('%H:%M:%S', time.gmtime(vm['uptime']))
    except Exception as e:
        return f"Error: {str(e)}"