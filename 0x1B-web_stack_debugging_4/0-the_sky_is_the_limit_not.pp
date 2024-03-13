# Puppet manifest to optimize Nginx configuration

# Ensure Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Define Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Define Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}
