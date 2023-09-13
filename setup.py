from distutils.core import setup


setup(
    console=['main.py'],  # Replace with the name of your main Python script
    options={
        'py2exe': {
            'packages': ['MyApp', 'MyApp.Backend', 'MyApp.DataBase', 'MyApp.GUI'],
            'includes': [],  # List any additional modules you want to include
        }
    },
    zipfile=None,
)
