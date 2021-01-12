from flask import Flask, render_template, session
from flask_session import Session
import random

app = Flask(__name__)
app.debug = False
app.secret_key = 'cvhslv slv sv svh s.hsdv hsh'

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def hod_kostkou():
    hod_p = random.randint(1,6)    
    hod_vy = random.randint(1,6)
    if hod_p < hod_vy:
        vitez = "jste vyhrál vy."
        if not 'skore_ja' in session:
            session['skore_ja'] = 0 
        session['skore_ja'] = session['skore_ja'] + 1                              
    elif hod_vy < hod_p:
        vitez = "vyhrál počítač." 
        if not 'skore_pc' in session:
            session['skore_pc'] = 0 
        session['skore_pc'] = session['skore_pc'] + 1                           
    else:
        vitez = "skončil remízou."                         

    skore_ja = session['skore_ja']              
    skore_pc = session['skore_pc']
    return render_template('index.html', hod_p=hod_p, hod_vy=hod_vy, vitez=vitez, skore_ja=skore_ja, skore_pc=skore_pc)      
    
if __name__ == '__main__':
    app.run()