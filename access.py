RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^\.]+)$ $1.html [NC,L]

# FOR PHP

RewriteRule ^([^\.]+)$ $1.php [NC,L]


# Adding a trailing slash at the end  yoursite.com/page/

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^/]+)/$ $1.php
RewriteRule ^([^/]+)/([^/]+)/$ /$1/$2.php
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !(\.[a-zA-Z0-9]{1,5}|/)$
RewriteRule (.*)$ /$1/ [R=301,L]
