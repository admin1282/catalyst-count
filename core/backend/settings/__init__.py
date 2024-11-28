from split_settings.tools import optional, include
import  os


include('components/common.py')
print(os.environ.get('DJANGO_ENV'))
if 'development' == os.environ.get('DJANGO_ENV'):
    include('environment/development.py')
elif 'production' == os.environ.get('DJANGO_ENV'):
    include('environment/production.py')



