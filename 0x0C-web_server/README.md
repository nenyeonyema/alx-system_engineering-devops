Web Server

Note: -r is used for directories.

To transfer a file from local machine to the remote machine, we use secure copy protocol (scp).
Local machine to Remote machine
scp -i /path/to/private_key /path/to/local/file username@hostname:/path/to/destination/
OR 
To transfer a directory from local machine to a remote machine
scp -r /local/directory/path username@example:/remote/directory/path

For instance
scp -i ~/.ssh/school scp.html ubuntu@54.152.245.111

To transfer a file from Remote machine to Local machine
scp username@example.com:/remote/path/to/file /local/path

To transfer a directory from remote machine to local machine.
scp -r username@example.com:/remote/path/to/directory  /local/path
