## Setting up SSH Password

Run the following command in your machine from ansible-setup/ directory 

- ansible-vault encrypt_string --vault-password-file vault_password "<your_su_password>" --name "ssh_password"

This will store your su password in the vault to be used by the devices while logging in
