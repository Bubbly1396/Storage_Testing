import paramiko

class SSHClient:
    
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client = None
        
    def ssh_connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname, username=self.username, password= self.password)
            print("ssh is connected to remote server")
            return self.client
        except Exception as e:
            print(f"ssh connection failed : {e}")
            return None
            
    def execute_cmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode(), stderr.read().decode()
        
    def close(self):
        if self.client:
            self.client.close()
            

if __name__ == "__main__":          
    obj = SSHClient('192.168.0.180', 'root', 'winteck@2026')

    # obj.ssh_connect()
    if obj.ssh_connect():
        out, err = obj.execute_cmd(echo > 'fio --name=test --filename=/dev/sdb --runtime=1m --bs=4k --rw=read --ioengine=libaio')  
        print(out)
        print(err)
        obj.close()
