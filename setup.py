from setuptools import setup,find_packages

with open("./README.md","r") as f:
    longdesc = f.read()

setup(
    name="dialogflowpy-webhook",
    version="1.0.0",
    description="A Python module for parsing and creating Dialogflow Requests and Responses",
    url="https://github.com/vishalbala-nps/dialogflowpy-webhook",
    author="Vishal Balasubramanian",
    author_email="vishal.bala.nps@gmail.com",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3",
    keywords=["dialogflow","flask","django","fulfillment","webhook","api","python3","api.ai","python","Dialogflow Fulfillment","Dialogflow Fulfillment V2","dialogflowpy-webhook"],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)