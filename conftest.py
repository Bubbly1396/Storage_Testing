import pytest
from utils.ssh_connect import SSHClient as s
from utils.json_reader import load_json

config = load_json("config/server_config.json")

server = config['server']

        
@pytest.fixture()
def ssh_connection():
    
    ssh = s.ssh_connect(server["host"],
        server["username"],
        server["password"])
    print("ssh is connected")
    
    if ssh is None:
        pytest.skip("connection failed")
        
    yield ssh
    s.close()
    
@pytest.fixture(scope="session")
def test_data():
    return config
    
    
    