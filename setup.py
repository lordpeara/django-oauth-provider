from setuptools import setup, find_packages


setup(
    name='django-oauth-provider',
    version='0.0.1dev0',
    packages=find_packages(exclude=['*.tests']),
    scripts=[],

    install_requires=[
        'Django<2.2,>=1.11.21',
    ],

    author='lordpeara',
    author_email='lordpeara@gmail.com',
    description='Be a oauth provider.',
    license='MIT',
    keywords='django oauth oauth2 django-oauth2',
    url='http://github.com/lordpeara/django-oauth-provider',

    zip_safe=False,
    include_package_data=True,

    classifiers=[
        # 'Framework :: Django',
        # 'Intended Audience :: Developers',
        # 'Intended Audience :: System Administrators',
        # 'Operating System :: OS Independent',
        # 'Topic :: Software Development'
    ],
)
