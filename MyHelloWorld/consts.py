name = 'MyHelloWorld'
version = "0.5.3"
author = 'Sathiyakugan Balakrishnan <bsathiyakugan@gmail.com>'
homepage = 'https://github.com/sathiyakugan/MyHelloWorld'
default_user_agent = '{}/{} (+{})'.format(name, version, homepage)

default_json_headers = [
    ('Content-Type', 'application/json'),
    ('Cache-Control', 'no-store'),
    ('Pragma', 'no-cache'),
]
