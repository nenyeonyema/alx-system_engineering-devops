# Define package management for apt
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define the Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the index.html file content
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
