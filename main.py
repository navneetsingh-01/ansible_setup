import time
import sys
import ansible_runner

out, err, rc = ansible_runner.run_command(
    executable_cmd='ansible-playbook',
    cmdline_args=['/home/singhnavneet.su/ansible_setup/project/device_updates.yaml',
                  '-i', 'inventory', '-vvvv', '--vault-pass', '/home/singhnavneet.su/ansible_setup/vault_password'],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr,
)
print("rc: {}".format(out))
print("out: {}".format(err))
print("err: {}".format(rc))
