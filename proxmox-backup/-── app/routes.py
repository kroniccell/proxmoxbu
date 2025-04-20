from flask import render_template
from app.backup import get_vm_uptime

def register_routes(app):
    # ... (קוד קודם)
    
    @app.route('/uptime', methods=['GET', 'POST'])
    def vm_uptime():
        uptime = None
        if request.method == 'POST':
            vmid = request.form['vmid']
            uptime = get_vm_uptime(vmid)
        return render_template("uptime.html", uptime=uptime)