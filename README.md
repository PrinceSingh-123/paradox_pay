# paradox_payment 
# Payment with esewa 
### Functionalities
#### Inbuilt product model for adding product
#### Inbuilt subscription model for adding and manage subscription like trial, weekly, monthly, yearly, non recurance etc
#### social auth like github, facebook, twitter and google  are already implemented 


## To use esewa for django

#### first of all list these below urls in the urls.py file of your root directory
##### path("",include("esewa.urls")),
##### path('login/', auth_views.LoginView.as_view(), name='login'),
##### path('logout/', auth_views.LogoutView.as_view(), name='logout'),
##### path('oauth/', include('social_django.urls', namespace='social')),

## for social auth and some login,logout and redirect urls  list the following stuff in the setting.py file

#### LOGIN_URL = 'login'
#### LOGOUT_URL = 'logout'
#### LOGIN_REDIRECT_URL = '/'

### For Social Authentication

#### SOCIAL_AUTH_GITHUB_KEY = 'your key'
#### SOCIAL_AUTH_GITHUB_SECRET = 'your secret key'
 
#### SOCIAL_AUTH_TWITTER_KEY = 'your key'
#### SOCIAL_AUTH_TWITTER_SECRET = 'your secret key'
 
#### SOCIAL_AUTH_FACEBOOK_KEY = 'your key' # Facebook App ID
#### SOCIAL_AUTH_FACEBOOK_SECRET = 'your secret key'  # Facebook App Secret
#### SOCIAL_AUTH_FACEBOOK_SCOPE = ['']


#### SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your key'
#### SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your secret key'  # Google Consumer Secret



### Note: In this package we provide the test merchant key for esewa, to use for the production please update the merchant key in your esewa model of the admin panel. 

## After listing all the configuration 
### command: python manage.py makemigrations esewa
### command: python manage.py migrate

### after that please create  Product and Subscription from Admin panel


