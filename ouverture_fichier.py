def ouvrir_fichier(nom):
	""" Prérequis :
	nom : str
	nom -> nom de fichier valide et existant """

	f = open(nom, "r")

	if f is None:
		raise Exception("Erreur lors de l'ouverture du fichier")
		return None

	lines = f.readlines()
	f.close()

	n = lines[0]
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

	return (x,int(n),y,int(m))