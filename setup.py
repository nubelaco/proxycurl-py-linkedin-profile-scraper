try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='proxycurl-py',
    version='0.0.13',
    python_requires='==3.*,>=3.7.0',
    author='Nubela',
    author_email='tech@nubela.co',
    packages=['proxycurl-py.asyncio', 'proxycurl-py.gevent', 'proxycurl-py.twisted'],
    package_dir={"": "."},
    package_data={},
    install_requires=[],
    extras_require={"asyncio": ["aiohttp==3.*,>=3.7.4", "asyncio==3.*,>=3.4.3"], "dev": ["jinja2==3.*,>=3.0.1"], "gevent": ["gevent==21.*,>=21.1.1", "requests==2.*,>=2.25.0"], "twisted": ["treq==21.*,>=21.5.0", "twisted==21.*,>=21.7.0"]},
)
