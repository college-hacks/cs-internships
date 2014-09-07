import time

readme = open('README.md', 'w')
readme.write('cs-internships\n')
readme.write('=============\n\n')
readme.write('> In vain have you acquired knowledge, if you have not imparted it to others. **- Deuteronomy Rabbah**\n\n\n')
readme.write('##How can I get better at interviews?\n')
readme.write('Practice makes perfect. Critical thinking and problem solving skills do not appear overnight. Check out these great resources that review basic data structures and then give you a whole bunch of problem sets for you to solve!\n\n')

#append interview practice problems here
practice = open('src/practice.txt')
readme.write("##Practice\n\n")
for line in practice:
  readme.write(line)

readme.write('\n\n')


readme.write('##Books\n\n')
# append resource links here
resources = open('src/resources.txt')
resource_info = []
for line in resources:
	if line != "\n":
		resource_info.append(line)
	else:
		resource_name = resource_info.pop(0)[:-1]
		resource_link = resource_info.pop(0)[:-1]
		resource_description = resource_info.pop(0)[:-1]
		readme.write('[' + resource_name + '](' + resource_link + ') - ' + resource_description + '\n\n')


time = time.strftime("%c")
readme.write('##Companies\n\n')
readme.write('**Last updated - ' + time + '**\n\n')

# append company links here
internships = open('src/internships.txt')
company_info = []
for line in internships:
  if line != "\n":
     company_info.append(line)
  else:
  	company_name = company_info.pop(0)[:-1]
  	company_link = company_info.pop(0)[:-1]
  	company_description = company_info.pop(0)[:-1]
  	company_deadline = company_info.pop(0)[:-1]
  	readme.write('[' + company_name + '](' + company_link + ') - ' + company_description + ' - ' + company_deadline + '\n\n')
   