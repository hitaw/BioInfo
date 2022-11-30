#On crée une fonction d'ouverture de fichier pour éviter d'avoir à répéter ces opérations à chaque fois durant les tests

def ouvrir_fichier(nom):
	""" 
	Récupère les valeurs x et y d'un fichier d'instance

	Entrée :

	nom : str
	nom -> nom de fichier valide et existant 

	Sortie :
	
	x : str
	n : int
	y : str
	m : int 
	"""

	f = open(nom, "r") 						# On ouvre le fichier en mode lecture

	if f is None: 							#On s'assure que le fichier existe bien et a bien été ouvert
		raise Exception("Erreur lors de l'ouverture du fichier")
		return None

	lines = f.readlines()					#On récupère le contenu du fichier puis on le ferme
	f.close()

	n = lines[0]							#On supprime tous les espaces et les retours à la ligne présents dans le fichier qui viendraient perturber le bon déroulement du reste du programme
	n = n.replace(" ","")
	n = n.replace("\n","")

	m = lines[1]
	m = m.replace(" ","")
	m = m.replace("\n","")

	x = lines[2]
	x = x.replace(" ","")
	x = x.replace("\n","")

	y = lines[3]
	y = y.replace(" ","")
	y = y.replace("\n","")

	return (x,int(n),y,int(m))				#On retourne x, la taille de x, y et la taille de y