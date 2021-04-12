from setuptools import setup


setup(
    name='Flask-Logging',
    version='1.0.0',
    url='https://github.com/sylver11/flask-logging/',
    license='BSD',
    author='Justus Voigt',
    author_email='connectmaeuse@gmail.com',
    description='Simple logging extension for Flask',
    py_modules=['flask_logging'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
        ],
)
