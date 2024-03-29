# Puppet nginx configuration

# puppet class
class nginx_server {
    package { 'nginx':
        ensure => installed,
    }

    file { '/usr/share/nginx/html/index.html':
        ensure  => present,
        content => "Hello World!\n",
    }

    file { '/usr/share/nginx/html/404.html':
        ensure  => present,
        content => "<!DOCTYPE html>
                    <html>
                    <head>
                        <title>404 Not Found</title>
                    </head>
                    <body>
                        <h1>Ceci n'est pas une page</h1>
                    </body>
                    </html>",
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => present,
        content => "
            server {
                listen 80 default_server;
                listen [::]:80 default_server;
                server_name _;

                root /usr/share/nginx/html;
                index index.html;

                location / {
                    try_files $uri $uri/ =404;
                    add_header Content-Type text/html;
                    return 200 'Hello World!';
                }

                location /redirect_me {
                    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
                }

                error_page 404 /404.html;
                location = /404.html {
                    root /usr/share/nginx/html;
                    internal;
                    add_header Content-Type text/html;
                    return 404 '<!DOCTYPE html>
                                <html>
                                <head>
                                    <title>404 Not Found</title>
                                </head>
                                <body>
                                    <h1>Ceci n'\''est pas une page</h1>
                                </body>
                                </html>';
                }
            }
        ",
        require => Package['nginx'],
    }

    service { 'nginx':
        ensure  => running,
        enable  => true,
        require => File['/etc/nginx/sites-available/default'],
    }
}
