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
			board = url[24:26]
			threadnumber = url[34:41]

			direccion = 'http://a.4cdn.org/'+board+'/thread/'+threadnumber+'.json'

			try: 
				post = requests.get(direccion).json()
				largo = len(post['posts'])

				print('\nDescargando desde: ' + direccion)
				print('Descargando '+str(largo)+' items...\n')

				os.system('mkdir "'+post['posts'][0]['sub']+'"')

				for i in post['posts']:
					try:
						os.system('wget http://i.4cdn.org/'+board+'/'+str(i['tim'])+str(i['ext']))
						os.system('mv "'+str(i['tim'])+str(i['ext'])+'" "'+post['posts'][0]['sub']+'"')
					except:
						print("No hay imagen de esta respuesta")
			except:
				print('Ha ocurrido un error, revisa tu conexion a internet...')

if __name__ == "__main__":
	main(sys.argv[1:])
   