Command line for the win. Connecting through SFTP

A. To connect to a remote machine through SFTP:
We use the following commands:
1. sftp remoteusername@hostname
OR
sftp remoteusername@remoteipaddress
2. type 'yes' when asked to oauthorize the connection
3. Input the remote machine password

Congratulations, you have connected to your remote machine.

You can now transfer files from your local machine to your remote machine.
B. To upload files to remote from local machine we use the 'put' command.
1. put 0-first_9_.png
2. put 1-next_9_.png
3. put 2-next_9_.png

Note: To download from remote to local machine the command is 'get'.
