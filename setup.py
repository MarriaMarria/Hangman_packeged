import setuptools

setuptools.setup(
    name ='mygame_Maria2', 
    version ='1.6.0', 
    author ='Maria', 
    author_email ='maria.kononevs@gmail.com', 
    url ='blablabla2mongithub', 
    description ='blablabla3', 
    # long_description = long_description, 
    long_description_content_type ="text/markdown", 
    packages = setuptools.find_packages(),
    entry_points ={ 
        'console_scripts': [ 
            'hangman2 = My_game2.hangman:main',
        ], 
    }, 
    classifiers =( 
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
    ), 
    python_requires='>=3.6'
) 