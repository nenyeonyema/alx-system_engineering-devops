# Define Nginx package and service

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

# Define Nginx configuration file

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => service['nginx'],
}
# define index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => package['nginx'],
}

# Define redirect configuration file
file { '/etc/nginx/sites-available/redirect':
  ensure  => file,
  content => template('nginx/redirect.erb'),
  require => Package('nginx']
  notify  => Service['nginx'],
}

# Enable the redirect site
file { '/etc/nginx/sites-enabled/redirect':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect',
  require => File['/etc/nginx/sites-available/redirect'],
  notify => Service['nginx'],
}
