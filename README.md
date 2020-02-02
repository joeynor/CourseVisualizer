# CourseVisualizer
A personal *python 2* project to generate a directed graph of data retrieved from docx files. The doc files is the course outlines, and have interdependencies with other courses. 

## How it works


## How to run

1. you will definitely need python 2. I didnt use python 3 due to instability of the python-docx library in python3 for now. Will upgrade in the future

2. Instaling the third party python-docx module, not the docx. I use pip
```
sudo pip install python-docx
```

3. run the code
```
python genDotFileVisualizer.py > outputfile.txt
```

4. Visualizing 

copy paste the dot text from outputfile.txt into online graphviz visualizers like 
[Webgraphviz](webgraphviz.com) or [Graphviz Online](https://dreampuf.github.io/GraphvizOnline)

## Future work

1. Need to be more robust in my regex to get data, since documents are made by people and they tend to forget commas "," or prerequisites sometimes does not include course title which will course error in the generated dot file. 
2. Specialization should be automatic from folder structure, right now its hardcoded
3. Does not cater other useful information, like credit points, required courses and etc, will intend to support that somehow in the future
4. Need a build in visualizer instead of using the online version. This will take time, so right now i just generate the dot file. 
