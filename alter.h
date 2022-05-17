// # ------------- alternative remove .html version, 2020 -------------------
// #remove html file extension https://example.com/page.html 
// # to https://example.com/page 


RewriteEngine On 
RewriteCond %{REQUEST_FILENAME} !-d 
RewriteCond %{REQUEST_FILENAME} !-f 
RewriteRule ^([^\.]+)$ $1.html [NC, L] 



// The search engine may index these pages as duplicate content, 
// to overcome this add a <canonical> meta tag in the HTML file.
// Example:
// <link rel="canonical" href="https://example.com/blog/first-blog" />