# Install nginx package

package { 'nginx':
  ensure => installed,
}

# Define a custom file for the nginx configuration
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      server_name _;

      location / {
        add_header X-Served-By $hostname;
        root /var/www/html;
        index index.html index.htm;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Create a symlink to enable the site
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
  notify => Service['nginx'],
}

# Ensure nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
