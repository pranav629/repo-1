import subprocess
import os

node_process = None

def start_node_server():
    global node_process
    node_path = os.path.join(os.path.dirname(__file__), '..', 'email_service', 'server.js')
    node_process = subprocess.Popen(['node', node_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

start_node_server()

