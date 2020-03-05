from distutils.core import setup
setup(
    name='pytops',         # How you named your package folder (MyLib)
    packages=['pytops'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='An easy to use Python library for pricing options using the Black-Scholes model',
    author='Swapnil Joshi',                   # Type in your name
    author_email='work.swaps@gmail.com',      # Type in your E-Mail
    url='https://hiswapnil.me',
    download_url='https://github.com/hiswaps/pytops/archive/v0.2.1.tar.gz',
    # Keywords that define your package best
    keywords=['options', 'trading', 'python', 'data',
              'finance', 'pricing', 'black-scholes', 'derivatives'],
    install_requires=[            # I get to this in a second
        'numpy',
        'scipy',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',

        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
