# CourseVisualizer
A personal *python 2* project to generate a directed graph of data retrieved from docx files. The doc files is the course outlines, and have interdependencies with other courses. 

![Screenshot](https://github.com/joeynor/CourseVisualizer/blob/master/sample/mygraph.png)

## How it works

Basically, there is a folder called courses, with 7 specializations. Each specialization has its own folder. 
Each folder contains several course outlines in .docx format. The code will look into these folders for course files, and search for specific keywords, like Course Code, Course Title, and Prerequisites. Data of these keywords is used to generate a graphviz dot format file. This file can then be use to generate the graph as shown below.

## How to run

1. You will definitely need python 2. I didnt use python 3 due to instability of the python-docx library in python3 for now. I will figure it out later, and will upgrade in the future

2. Instaling the third party python-docx module, not the docx. I use pip
```
sudo pip install python-docx
```

3. You may then copy your course outlines into the folders. This is of course assuming that you have a similar or identical keywords used in our course outlines. You can fork and modify the code if you wish to fit your requirements. Please include acknowledgement.

4. run the code
```
python genDotFileVisualizer.py > outputfile.txt
```

5. Visualizing 

copy paste the dot text from outputfile.txt into online graphviz visualizers like
[Graphviz Online](https://dreampuf.github.io/GraphvizOnline) or
[Webgraphviz](http://www.webgraphviz.com/) 

## Future work

1. Need to be more robust in my regex to get data, since documents are made by people and they tend to forget commas "," or prerequisites sometimes does not include course title which will course error in the generated dot file. 
2. Specialization should be automatic from folder structure, right now its hardcoded
3. Does not cater other useful information, like credit points, required courses and etc, will intend to support that somehow in the future
4. Need a build in visualizer instead of using the online version. This will take time, so right now i just generate the dot file. 
