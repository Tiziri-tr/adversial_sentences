import os
import xml.etree.ElementTree

custom_stopwords = {}
#punctuation="[,;:!?/."'+\-]"

directory = "dataset"

contradiction = ["real_contradiction.xml","RTE2_dev_negated_contradiction.xml","RTE2_test_negated_contradiction.xml"]
entailement = ["RTE1_dev1_3ways.xml","RTE1_dev2_3ways.xml","RTE2_dev_3ways.xml","RTE2_test_3ways.xml","RTE3_dev_3ways.xml","RTE3_test_3ways.xml"]

def pars_xml(e):
	return ""

file = open("dataset","w")	

for filename in os.listdir(directory):
	if filename.endswith(".xml") in contradiction: 
        	e = xml.etree.ElementTree.parse(filename).getroot()
		for atype in e.findall('pair'):
			print("T : ",atype.get('t'))
			print("H : ",atype.get('h'))
		continue
	else:
		continue
# t,h,{contradiction,type}



data_size = 4797
contradiction = 1030
cnt_yes = 582 # 131 + 51 + 400 
cnt_no = 448 # 0 + 51 + 397
entailement = 3767
ent_no = 470 #48 + 55 + 111 + 104 + 80 +72 
ent_unk = 1393 #97 + 85 + 289 + 296 + 308 + 318
ent_yes = 1904

