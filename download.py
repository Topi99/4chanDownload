#!/usr/bin/python3
import os, getopt, sys, requests

def main(argv):
	comando = ''
	url = ''
	direccion = ''
	board = ''
	threadnumber = ''

	try:
		opts, args = getopt.getopt(argv,"hd:",["direccion="])
	except getopt.GetoptError:
		print('Error')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('comandos.py -d <direccion> \nexample: http://boards.4chan.org/wg/thread/6683497')
			sys.exit()
		elif opt in ("-d", "--direccion"):
			url = arg
			url_split = url.split('/')
			board = url_split[3]
			threadnumber = url_split[5]

			direccion = 'http://a.4cdn.org/'+board+'/thread/'+threadnumber+'.json'

			try: 
				post = requests.get(direccion).json()
				largo = len(post['posts'])

				print('\nDescargando desde: ' + direccion)
				print('Descargando '+str(largo)+' items...\n')

				carpeta = ' '
				try:
					carpeta = post['posts'][0]['sub']+'"'
					os.system('mkdir "'+carpeta)
				except:
					carpeta = post['posts'][0]['semantic_url']+'"'
					os.system('mkdir "'+carpeta)

				for i in post['posts']:
					try:
						os.system('wget http://i.4cdn.org/'+board+'/'+str(i['tim'])+str(i['ext']))
						os.system('mv "'+str(i['tim'])+str(i['ext'])+'" "'+carpeta)
					except:
						print("No hay imagen de esta respuesta")
			except:
				print('Ha ocurrido un error, revisa tu conexion a internet...')

if __name__ == "__main__":
	main(sys.argv[1:])
   
