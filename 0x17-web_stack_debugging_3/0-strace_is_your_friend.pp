
# Other necessary functions and logic
# Othefest to automate fixing Apache 500 error

# Ensure that the Apache service is running
service { 'apache2':
  ensure => 'running',
}

# Fix permissions on Apache log files
file { '/var/log/apache2/error.log':
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}

# Restart Apache service to apply changes
exec { 'restart_apache':
  command     => '/bin/systemctl restart apache2',
  refreshonly => true,
  subscribe   => File['/var/log/apache2/error.log'],
}
