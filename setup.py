import setuptools

setuptools.setup(
    zip_safe=False,
    name='cloudify-occi-plugin',
    version='0.0.3',
    author='Vlastimil Holer',
    author_email='holer@ics.muni.cz',
    packages=['cloudify_occi_plugin',
              'cloudify_occi_plugin.provider'],
    license='LICENSE',
    description='Cloudify OCCI plugin',
    install_requires=[
        'cloudify-plugins-common>=3.3.1',
    ],
)
