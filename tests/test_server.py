import pytest

def test_drives(ssh_connection, test_data):
    out, err = ssh_connection.execute_cmd('free -h')
    assert 'Mem:' in out
    
# def test_pci(ssh_client):
    # out, err = ssh_client.execute_cmd('lspci')
    # assert 'PCI' in out
    
# def test_cpu_info(ssh_client):
    # out, err = ssh_client.execute_cmd('lscpu')
    # assert 'CPU(s):' in out
    # assert "Architecture" in out
    
# def test_memory(ssh_client):
    # out, err = ssh_client.execute_cmd('free -h')
    # assert 'Mem:' in out
    