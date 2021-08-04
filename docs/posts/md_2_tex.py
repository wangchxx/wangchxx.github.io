#%%
import numpy as np
import re 




#%%
def titles(line):
    if line[0:2] == '# ':
        newline = r'\chapter{%s}'%(line[2:-1])+ '\n'
    elif line[0:2] == '##':
        newline = r'\section{%s}'%(line[2:-1])+ '\n'
    else:
        newline = line 
    return newline

def theorem(line):
    mod = ['definition','theorem','lemma','corollary','example','proposition','exercise','proof']
    line_15 = line[0:15].lower()
    count = 0
    for mod_name in mod:
        if mod_name in line_15:
            count+=1
            ind_name_1 = line.find('(')
            ind_name_2 = line.find(')')
            ind_label_0 = line.find('span id')
            ind_label_1 = line.find('"',ind_label_0)
            ind_label_2 = line.find('"',ind_label_1+1)
            if ind_name_1 > -1:
                name = line[ind_name_1+1: ind_name_2]
            else:
                name = ''
            
            if ind_label_0 > -1:
                label = r'\label{%s}'%(line[ind_label_1:ind_label_2+1])
            else:
                label = ''
            
            newline = r'\begin{%s} [%s] %s '%(mod_name,name,label) + '\n' + r'\end{%s}'%mod_name + '\n'
        

    if count==0:
        newline = line 
    return newline
    
  
def isproof(line):
    line_15 = line[0:15].lower()
    return 'proof' in line_15
    

def emph(line):
    if '`' in line:
        newline = re.sub('\`(.*?)\`', '\\\\emph{\\1}',line)
    else:
        newline = line
    return newline

def mathR(line):
    if '$' in line:
        newline = re.sub('(\$.*?)\\\\R(\W.*?\$)', '\\1 \\\\RR \\2',line)
    else:
        newline = line
    return newline


# %%
r'\chapter{a}'
# %%
l1 = data[0]
b = r'\chapter{%s}'%(l1[2:-1]) + '\n'
b
# %%
l2 = data[18]
i1 = l2.find('afc')
# i2 = l2.find(')')
data
# %%
test_re=r'a ' + r'Let $(M,d)$ be a metric space. A set $A\subset M\in\Re F\in\R, A$ is `compact` if every sequence $\{x_n\}$ in $A$ contains a subsequence that converges to an element of $A$. The set $A$ is `relatively compact` if the closure $\bar{A}$ is compact. If he set $M''$ itself is compact, then we say that $(M,d)$ is a compact metric space. $\R$, $\R_i$, $\mathcal{R}$'
import re 
# r'\emph{}'
# re.sub('\`(.*?)\`', '\\\\emph{\\1}',test_re)
# re.sub('(\$.*?)\\\\R(\W.*?\$)', '\\1 \\\\RR \\2',test_re)
# '$' in test_re
# %%
'##' in data[16]
data[16][0:100].lower()
# %%

def md_2_tex(file_name):

    data = []
    f = open("%s.md"%file_name,'r')
    data = f.readlines()
    f.close()

    with open("%s.tex"%file_name,"w") as g:
        for i in data:
            line = titles(i)
            line = emph(line)
            line = mathR(line)
            line = theorem(line)
            g.writelines(line)
    
functional = "functional_"
fun_num = [i for i in range(6)]
math_ana = "math_analysis_"
if __name__ == "__main__":
    for num in fun_num:
        file_name = functional + str(num)
        md_2_tex(file_name)


