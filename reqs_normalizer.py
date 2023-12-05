with open('requirements.txt', 'r') as f:
    reqs = f.readlines()

reqs = [req.strip() for req in reqs]

for i in range(len(reqs)):
    if reqs[i].find('==') != -1:
        x = reqs[i].split('==')
        reqs[i] = x[0] + "<=" + x[1] + "\n"

with open('requirements.txt', 'w', newline='\n') as f:
    f.writelines(reqs)