# Puppet manifest to adjust file descriptor limit for holberton user

exec { 'increase-file-descriptor-limit':
  command     => '/bin/bash -c "ulimit -n 65536 && echo \'*       hard    nofile    65536\' >> /etc/security/limits.conf"',
  path        => '/bin',
  refreshonly => true,
}

# Reload the PAM configuration to apply changes
exec { 'reload-pam-configuration':
  command     => '/bin/systemctl restart systemd-logind.service',
  path        => '/bin',
  refreshonly => true,
}

# Restart the SSH service to apply changes
service { 'ssh':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['reload-pam-configuration'],
}
