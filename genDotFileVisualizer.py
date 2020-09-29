#specific to extracting information from word documents
import docx
import re
import os

specialization = {
    1:"Programming",
    2:"Mathematics",
    3:"Algorithms",
    4:"Computer Architecture and Digital Design",
    5:"Software Engineering",
    6:"Network and Security",
    7:"Data Science and Computational Intelligence"
}
color = ("salmon2", "greenyellow", "goldenrod2", "salmon1", "dodgerblue1", "coral", "darkseagreen", "crimson")
count = 0
#course_dict ={coursecode:{title:sometitle, area:somearea, prereq:{coursecode:title}}}
course_dict ={}
for dir in specialization:
    count=count + 1
    path = "./courses/"+str(dir)+". "+specialization[dir]+"/"
    files = os.listdir(path)
    for file in files:
        doc = docx.Document(path+file)
        for para in doc.paragraphs:
            p = re.compile(r'(.*)Course Title(.*):(.*)')  # for course title
            s = para.text
            m =  p.search(s)
            if m:
                result1 = m.group(3)
                result1 = result1.strip()
            p = re.compile(r'(.*)Course Code(.*):(.*)')  # for course title
            s = para.text
            m =  p.search(s)
            if m:
                result2 = m.group(3)
                result2 = result2.strip()
            p = re.compile(r'(.*)Prerequisite(.*):(.*)')
            s = para.text
            m =  p.search(s)
            if m:
                result3 = m.group(3)
                result3 = result3.strip()
                if result3 == "None":
                    result3 = "DCS Program"
                    course_dict[result2]={}
                    course_dict[result2]={'title':result1,'area':dir,'prereq':{'0':result3}}
                x = result3.split(",")
                course_dict[result2] = {}
                h={}
                if len(x)>1:
                    count = 0
                    for y in x:
                        result3 = y.strip()
                        z = result3.split(" ")
                        course_code = " ".join(z[0:2])
                        course_title = " ".join(z[2:])
                        if count==0:
                            course_dict[result2]={'title':result1,'area':dir,'prereq':{course_code:course_title}}
                            count=count+1
                        else:
                            course_dict[result2]['prereq'][course_code] = course_title
                            #print course_dict
                else:
                    z = result3.split(" ")
                    course_code = " ".join(z[0:2])
                    course_title = " ".join(z[2:])
                    course_dict[result2] = {}
                    course_dict[result2]={'title':result1,'area':dir,'prereq':{course_code:course_title}}
print ("digraph G {")
print ("rankdir=LR")
print ("node [style=filled height=0.55 fontname=\"Verdana\" fontsize=10];")
print ("subgraph cluster_key {")
print (" label=\"Specializations\";")
for s in specialization:
    print ("\""+specialization[s]+"\" [shape=rectangle fillcolor=\""+color[s]+"\"];")
prev = 1;
print ("\"Non DCS Course\";")
for s in specialization:
    if s==1 or s==5:
        prev=s
    else:
        print ("\"" + specialization[prev] + "\" -> \"" + specialization[s] + "\"[style=invis];")
        prev = s
    if s==7:
        print ("\"" + specialization[s] + "\" -> \"Non DCS Courses\"[style=invis];")

print ("}")        

print ("{ node [margin=0.1 shape=rectangle style=filled]")
for cc in sorted(course_dict):
    print ("\""+cc+ "\\n"+course_dict[cc]['title']+"\" [fillcolor=\""+color[course_dict[cc]['area']]+"\"]")
print ("}")
#for the rank 2000 below
print ("{ rank=same; ")
for cc in sorted(course_dict):
    test = cc.split(" ")
    if int(test[1])<2000:
        print ("\""+cc+ "\\n"+course_dict[cc]['title']+"\";")
print ("}")
#for the rank 3000 below
print ("{ rank=same; ")
for cc in sorted(course_dict):
    test = cc.split(" ")
    if 2000<int(test[1])<3000:
        print ("\""+cc+ "\\n"+course_dict[cc]['title']+"\";")
print ("}")
#for the rank 4000 above
print ("{ rank=same; ")
for cc in sorted(course_dict):
    test = cc.split(" ")
    if 3000<int(test[1])<4000:
        print ("\""+cc+ "\\n"+course_dict[cc]['title']+"\";")            
print ("}")
#for the rank 4000 above
print ("{ rank=same; ")
for cc in sorted(course_dict):
    test = cc.split(" ")
    if int(test[1])>4000:
        print ("\""+cc+ "\\n"+course_dict[cc]['title']+"\";")            
print ("}")

for cc in sorted(course_dict):
    for prereqcc in sorted(course_dict[cc]['prereq']):
        print ("    \""+prereqcc+"\\n"+course_dict[cc]['prereq'][prereqcc]+"\" -> " + " \"" +cc+ "\\n" +course_dict[cc]['title']+"\";")

print ("}")
