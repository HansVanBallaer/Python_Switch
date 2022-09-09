
import paramiko

router_ip = "192.168.1.1"
router_username = "admin"
router_password = "password"

ssh = paramiko.SSHClient()

# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to router using username/password authentication.
ssh.connect(router_ip, 
            username=router_username, 
            password=router_password,
            look_for_keys=False,
            allow_agent=False )

# Run command.
channel= ssh.invoke_shell()
channel.send("show dot1x sessions all \r")
resp = channel.recv(9999)
output = resp.decode('ascii').split(',')
print (''.join(output))

# Close connection.
ssh.close()
