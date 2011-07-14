
import os
from setuptools import setup

from mobile_detector import VERSION

REQUIREMENTS = [
    'django',
]


README = os.path.join(os.path.dirname(__file__), 'README.txt')
setup(
    name="django-mobile-detector",
    version=VERSION,
    author="Aaron Madison",
    author_email="aaron.l.madison@gmail.com",
    description="A small app to detect mobile browsers.",
    long_description=open(README, 'r').read(),
    url="https://github.com/madisona/django-mobile-detector",
    test_suite='runtests.runtests',
    packages=("mobile_detector",),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    zip_safe=False,
)