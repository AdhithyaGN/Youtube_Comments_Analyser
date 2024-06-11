from setuptools import setup,find_packages




setup(
    name='Youtube_Comments_Analyser',
    version='0.0.1',
    author='Adhithya G Nair',
    author_email='adhithyagnair97@gmail.com',
    install_requires=["pandas","langchain","streamlit","python-dotenv","PyPDF2",'matplotlib'],
    packages=find_packages()
)