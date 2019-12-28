import simplejson

states_name = ["Acre","Alagoas","Amapá" , "Amazonas" , "Bahia", "Ceará", "Distrito Federal","Espírito Santo","Goiás","Maranhão",
"Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná","Pernambuco","Piauí","Rio de Janeiro","Rio Grande do Norte",
"Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina","São Paulo","Sergipe","Tocantins"]

states = []

for i in range(0,len(states_name)):
    file = open(states_name[i]+".txt",'r')
    texto = file.readlines()
    states.append({states_name[i]:texto})
    file.close()
print(states)
file = open('estadosUniversidades.json','w+')
simplejson.dump(states,file)

file.close()
