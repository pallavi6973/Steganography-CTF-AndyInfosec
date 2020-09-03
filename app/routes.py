from app import app
from flask import render_template, flash, redirect, send_file,url_for
import requests
from app.forms import SubmitForm

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', title='Steganography CTF')



@app.route('/Challenges/', methods=['GET', 'POST'])
def challenges():
    
    return render_template('challenges.html', title='Steganography CTF')

@app.route('/Challenges/files/enquete.pdf/', methods=['GET', 'POST'])
def file1():
	return send_file('templates/files/enquete.pdf', attachment_filename='enquete.pdf')

@app.route('/Challenges/files/dig.png/', methods=['GET', 'POST'])
def file2():
	return send_file('templates/files/dig.png', attachment_filename='dig.png')

@app.route('/Challenges/files/find.zip/', methods=['GET', 'POST'])
def file3():
	return send_file('templates/files/find.zip', attachment_filename='find.zip')

@app.route('/Challenges/files/akaij.tar/', methods=['GET', 'POST'])
def file4():
	return send_file('templates/files/akaij.tar', attachment_filename='akaij.tar')

@app.route('/Challenges/files/file.wav/', methods=['GET', 'POST'])
def file5():
	return send_file('templates/files/file.wav', attachment_filename='file.wav')

@app.route('/Challenges/files/QR Code.png/', methods=['GET', 'POST'])
def file6():
	return send_file('templates/files/QR Code.png', attachment_filename='QR Code.png')

@app.route('/Challenges/files/see me.mp4/', methods=['GET', 'POST'])
def file7():
	return send_file('templates/files/see me.mp4', attachment_filename='see me.mp4')

@app.route('/Challenges/files/Research.zip/', methods=['GET', 'POST'])
def file8():
	return send_file('templates/files/Research.zip', attachment_filename='Research.zip')
@app.route('/Challenges/files/README.txt/', methods=['GET', 'POST'])
def file9():
	return send_file('templates/files/README.txt', attachment_filename='README.txt')
	
@app.route('/submit/', methods=['GET','POST'])
def submit():
	form = SubmitForm()
	if form.validate_on_submit():
		if form.flag.data == "steg{wh1t3 Is c0Ol}":
			flash("Congrats!You Completed Your Challenge")
		elif form.flag.data == "steg{g_o_t_y_o_u_r_f_l_a_g}":
			flash("Congrats!You Completed Your Challenge")
		elif form.flag.data == "steg{h1ng3d It}":
			flash("Congrats!You Completed Your Challenge")
		elif form.flag.data == "steg{p13sa'nt s0und m'ak3s a' dAy}":
			flash("Congrats!You Completed Your Challenge")
		elif form.flag.data == "steg{H3R3_15_y0ur_fl4g}":
			flash("Congrtas!You Completed Your Challenge")
		elif form.flag.data == "steg{StrAnGe Idea}":
			flash("Congrtas!You Completed Your Challenge")
		elif form.flag.data == "steg{C0OL_Y0U_4R3_1337}":
			flash("Congrats!You Completed Your Challenge")
		elif form.flag.data == "steg{3NCRYPTI0N5_4R3_C00L}":
			flash("Congrats!You Completed Your Challenge")							
		else :
			flash("Try Again!Better Luck")	

	app.logger.debug(app.config.get("ENV"))	        
	return render_template('submit.html', title='Steganography CTF', form=form)


if __name__=='__main__':
	app.run(debug=True,use_reloader=True)    
