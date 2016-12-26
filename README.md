Quick django project to serve images to users that are logged in. It uses the django framework to serve everything except the files.

#Depends
- Django
- apache2
- apache2-dev
- mod xsendfile
- Python3
- python-dev
- mod wsgi


#Setting Up New Server (No automation yet):
1. Install Depends
2. Pull Source
3. Cofigure Apache to point to wsgi instances.
4. Define a path for your files that need to be served. 
5. Change security key in django settings. 
6. Make database. 
7. Restart apache2. Off to the races.

#External Resources
Guide to install wsgi
1.https://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html

Xmod sendfile
2.https://tn123.org/mod_xsendfile/

Wsgi releases
3.https://github.com/GrahamDumpleton/mod_wsgi/releases

-Bootstrap
4.https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css

-Get Django setup with apache:
5.https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/modwsgi/

#Scratchlist To-Do
-Don't hardcode image URL into html. 
--> Reference Django Settings
-Change Passwords Link Added
- Custom Authentication (remove that PW) - Dual factor
- Find a system for image thumbnails / video hosting. 
- Fix get_object_or_404 - return an error to list_file.html
- Get static files defined and on commit. 

