# Puppet manifest to fix the web stack: Apache is returning a 200 and serving the correct page

# Ensure that the Apache service is running
service { 'apache2':
  ensure => 'running',
}

# Ensure that the Apache service starts on boot
service { 'apache2':
  enable => true,
}

# Fix permissions on Apache log files
file { '/var/log/apache2/error.log':
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}

# Ensure the default Apache page is served
file { '/var/www/html/index.html':
  content => "<html><head><title>Welcome to Puppet Apache Server</title></head><body><h1>It works!</h1><p>This is the default web page for Puppet Apache server.</p></body></html>",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Restart Apache service to apply changes
exec { 'restart_apache':
  command     => '/bin/systemctl restart apache2',
  refreshonly => true,
  subscribe   => File['/var/log/apache2/error.log', '/var/www/html/index.html'],
}
