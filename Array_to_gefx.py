openmatirx = open("all_effectors_versus_all_names_bit_score.tab")
#format needs to be per line: name tab name tab bitscore      e.g Rpa08528	Rpa01129	123.2
readmatrix = openmatirx.read()
splitmatrix = readmatrix.split("\n")
list_of_names = ""
node = ""
old_name = "x"
count = 0
list_of_name_with_new_id_code_pre = ""
#xxx is the min blosum score so far
xxx = 0.0

for x in range(len(splitmatrix)):
    if len(splitmatrix[x])>0:
        line = splitmatrix[x]
        splitline = line.split ("\t")
        name1 = splitline[0]
        name2 = splitline[1]
        if name1 not in old_name:
            #list_of_names = list_of_names + name1 + "\n"
            count = count + 1
            list_of_names = list_of_names + '<node id="' + str(count) + '.0" label="'+name1+'"/>' + "\n"
            list_of_name_with_new_id_code_pre = list_of_name_with_new_id_code_pre + name1 + "\t" + str(count)+ "\n"
        old_name = name1
        blosum_score = splitline[2]
        
list_of_name_with_new_id_code = list_of_name_with_new_id_code_pre.split("\n")
list_of_names = '<?xml version="1.0" encoding="UTF-8"?>\n<gexf xmlns:viz="http:///www.gexf.net/1.1draft/viz" version="1.1" xmlns="http://www.gexf.net/1.1draft">\n<meta lastmodifieddate="2010-03-03+23:44">\n<creator>Gephi 0.7</creator>\n</meta>\n<graph defaultedgetype="undirected" idtype="string" type="static">\n<nodes count="'+str (count) +'">\n' + list_of_names +'</nodes>'

     
#list_of_names_split = list_of_names.split("\n")

#print (len(list_of_names_split))
#print (list_of_names[:-1])
list_of_names_new = list_of_names[:-1]
    #print ('<node id="' + str(x) + '.0" label="'+name1+'"/>')
count_edges = 0
edges_string = ""
#ok next need to do the second half about number of nodes - so will itterate through the pairs again and then trim based on the score - and count those that pass the trim as i go
for x in range(len(splitmatrix)):
    if len(splitmatrix[x])>0:
        line = splitmatrix[x]
        splitline = line.split ("\t")
        name1 = splitline[0]
        name2 = splitline[1]
        blosum_score = float(splitline[2])
        #print (name1 + " " + name2 + " " + str(blosum_score))
        source = name1
        target = name2
        #if "Hg_C" in source:
        #print (source +"  " +target + "    " +str(blosum_score))
        for lines in list_of_name_with_new_id_code:
            if len(lines)>0:
                #print (lines)
                linessplit = lines.split("\t")
                #if name1 + "\t" in lines:
                if lines.startswith(name1+"\t"):
                    source_id = int(linessplit[1])
                if name2  + "\t" in lines:
                    target_id = int(linessplit[1])
        if blosum_score > xxx:
            if name1 not in name2:
                #if "Hg_C" in name1:
                    #print(name1 +"   "+ name2 + "   "+ str(blosum_score))
                    #print('<edge id="'+str(count_edges)+'" source="'+str(source_id)+'.0" target="'+str(target_id)+'.0" weight="'+str(blosum_score)+'.0"/>\n')
                count_edges = count_edges + 1
            #print('<edge id="'+str(count_edges)+'" source="'+str(source_id)+'.0" target="'+str(target_id)+'.0" weight="'+str(blosum_score)+'.0"/>')
                edges_string = edges_string + '<edge id="'+str(count_edges)+'.0" source="'+str(source_id)+'.0" target="'+str(target_id)+'.0" weight="'+str(blosum_score)+'.0"/>\n'
edges_string = '<edges count="'+str(count_edges)+'">\n'+edges_string +'</edges>\n</graph>\n</gexf>'

#print (edges_string)

final_out_string = list_of_names + "\n" +edges_string
openout = open("parsed_matrix_with_min_"+str(xxx)+"bitscore.gexf","w")
openout.write(final_out_string)
openout.close()
print("done")
