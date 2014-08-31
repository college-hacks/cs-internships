readme = open('README.md', 'w')
readme.write('csinternships\n')
readme.write('=============\n\n')
readme.write('> In vain have you acquired knowledge, if you have not imparted it to others. **- Deuteronomy Rabbah**\n\n\n')
readme.write('##How can I get better at interviews?\n')
readme.write('Practice makes perfect. Critical thinking and problem solving skills do not appear overnight. Check out these great resources that review basic data structures and then give you a whole bunch of problem sets for you to solve!\n\n')

# append resource links here

readme.write('##Companies to apply\n\n')

# append resource links here
internships = open('src/internships.txt')
company_info = []
for line in internships:
  if line == "\n":
    company_name = company_info.pop(0)[:-1]
    company_link = company_info.pop(0)[:-1]
    company_description = company_info.pop(0)[:-1]
    company_deadline = company_info.pop(0)[:-1]
    readme.write('[' + company_name + '](' + company_link + ') - ' + company_description + ' - ' + company_deadline + '\n\n')
  else:
    company_info.append(line)





# csinternships
# =============

# > In vain have you acquired knowledge, if you have not imparted it to others. **- Deuteronomy Rabbah**


# ##How can I get better at interviews?
# Practice makes perfect. Critical thinking and problem solving skills do not appear overnight. Check out these great resources that review basic data structures and then give you a whole bunch of problem sets for you to solve!

# resource links ..

# resource links ..

# resource links ..

# ##Companies to apply

# company link - description and note about company
# **due date**

# company link - description and note about company
# **due date**

# company link - description and note about company
# **due date**



