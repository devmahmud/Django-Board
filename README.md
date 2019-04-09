# Django-Board
Django Board App with full authentication system motivated by Vitor Freitas(simple is better than complex). In this project i tried to implement all this feature in my own way.
In this project i have used ckEditor As a TextField Editor. To count view i have used session so that multiple time can not be count from same user.

<h2>Requirements</h2>
<pre>open requirements.txt file to see requirements</pre>
<pre>To install requirements type</pre>
<code>pip install -r requirements.txt</code><br><br>

<h2>Installing</h2>
<pre>open terminal and type</pre>
<code>https://github.com/devmahmud/Django-Board.git</code><br><br>

<h4>or simply download using the url below</h4>
<code>https://github.com/devmahmud/Django-Board.git</code><br>

<h2>To migrate the database open terminal in project directory and type</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>Static files collection</h2>
<pre>open terminal and type</pre>
<code>python manage.py collectstatic</code>

<h2>Creating Dummy data open use populate script</h2>
<pre>For example to create dummy post in python shell type</pre>
<code>from populate script import create_post</code><br>
<code>create_post(30)</code>
<h4>30 post will be created automatically</h4><br>

<h2>Creating Superuser</h2>
<pre>To create superuser open terminal and type</pre>
<code>python manage.py createsuperuser</code>

<h2> For password Reset functionality by email fill up the information in Your Project setting </h2>
<code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code><br>
<code>EMAIL_HOST = 'smtp.gmail.com'</code><br>
<code>EMAIL_PORT = 587</code><br>
<code>EMAIL_USE_TLS = True</code><br>
<code>EMAIL_HOST_USER = 'your email'</code><br>
<code>EMAIL_HOST_PASSWORD = 'your email password'</code><br>

<h2> To run the program in local server use the following command </h2>
<code>python manage.py runserver</code>

<p>Then go to http://127.0.0.1:8000 in your browser</p>

<h2>Project snapshot</h2>
<h3>Home Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821079-74e7b700-5b1e-11e9-8be9-eabd3879d50b.png" width="100%"</img> 
</div>

<h3>Board Topics Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821153-9cd71a80-5b1e-11e9-8aac-fec94d4de6f8.png" width="100%"</img> 
</div>

<h3>Topics Messages page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821336-0e16cd80-5b1f-11e9-91e7-4c240de05e27.png" width="100%"</img> 
</div>

<h3>Reply Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821396-3bfc1200-5b1f-11e9-973e-4291fbca2389.png" width="100%"</img> 
</div>

<h3>Login Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821459-60f08500-5b1f-11e9-99c0-d51b87dbfda8.png" width="100%"</img> 
</div>

<h3>SignUp Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821513-7f568080-5b1f-11e9-9fe1-b0ab3a577a4b.png" width="100%"</img> 
</div>

<h3>Profile Edit Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/55821580-a4e38a00-5b1f-11e9-81e4-bfbc452347e5.png" width="100%"</img> 
</div>

<h2>Author</h2>
<blockquote>
  Mahmudul alam<br>
  Email: expelmahmud@gmail.com
</blockquote>

<div align="center">
    <h3>========Thank You !!!=========</h3>
</div>

