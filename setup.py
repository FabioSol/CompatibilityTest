from setuptools import setup

APP = ['main.py']  # Replace 'main.py' with the entry point of your application
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['MyApp'],  # Adjust this to include your package(s)
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
