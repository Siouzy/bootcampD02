import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='ai42',  
     version='1.0.0',
     scripts=['ai42'] ,
     author="srepelli",
     author_email="srepelli@student.42lyon.com",
     description="A simple progressbar and logger",
     long_description=long_description,
   long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     setup_requires=['wheel']
 )