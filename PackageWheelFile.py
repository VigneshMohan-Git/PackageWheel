import shutil,os
parent_dir="C:\\Users\\Poovendran\\PycharmProjects\\Package_whl\\"
destination_path = "C:\\Users\\Poovendran\\PycharmProjects\\Wheel_Files"
pythonfilepath = "C:\\Users\\Poovendran\\PycharmProjects\\Package_whl\\pythonfiles\\"

lines = [
"""
import setuptools

setuptools.setup(
name= "components",
version="0.0.1",
author="Vignesh Mohan",
author_email="vigneshmohan7275@gmail.com",
packages=setuptools.find_packages(),
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
python_requires='>=3.0',
)
"""]


    
    
onlyfiles = [f for f in os.listdir(pythonfilepath) if f.endswith('.py')]
for i in range(len(onlyfiles)):
    for onlyfile in onlyfiles:
        name = os.path.splitext(onlyfile)[0]
        directory = parent_dir + name + "_copy" + "\\" + name
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Directory Created:", name)

            #Copying files
            source=pythonfilepath+onlyfile
            destination=directory+"\\"+"__init__.py"
            shutil.copy(source, destination)

            #Replace Filenames
            replaced = [i.replace('components',name) for i in lines]
            with open(parent_dir + name + "_copy" + "\\"+"setup.py", 'w') as f:
                for line in replaced:
                    f.write(line)

            # -- Run Script
            ch = parent_dir + name
            os.chdir(ch)
            import sys
            #!{sys.executable} -m python setup.py sdist bdist_wheel
            print("Command Executing ...")
            os.system(r"""start /wait cmd /c "python setup.py sdist bdist_wheel" """)
            print("Wheel File Created!!!")
            os.system(r""" cmd exit()""")
            print("..........................................................")
    i+=1
        
def copy(parent_dir,destination_path):
    import glob, os, shutil
    
    #Creating Destination Path
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print("Directory Created")
        
    subfolders = [ f.path for f in os.scandir(parent_dir) if f.is_dir() ]
    for folders in subfolders:
        if os.path.isdir(folders+'/dist') == True:
            scr = folders+'/dist/'
            files = glob.iglob(os.path.join(scr, "*.whl"))
            for file in files:
                print(file)
                if os.path.isfile(file):
                    shutil.copy2(file, destination_path)
                    print("Wheel File Copied:")

# -- Function Call                    
copy(parent_dir, destination_path)