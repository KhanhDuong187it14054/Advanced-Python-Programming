from flask import Flask
from flask import render_template

ungdung = Flask(__name__,  static_folder='.\\templates\\static')

@ungdung.route('/')
def hello():
    tentruong = 'Đại học Văn Lang!'
    lienket = '<a href="http://www.vanlanguni.edu.vn">'+tentruong+'</a><br>'
    chuoi = lienket
    import datetime
    nam = datetime.date.today().year
    chuoi = chuoi + '<b>Xin <i>chào</i> Tân sinh viên năm '+str(nam)+'!</b><br>'
    return chuoi

@ungdung.route('/monhoc/')
def learn():
    chuoi = "Đây là trang môn học !"
    return chuoi

@ungdung.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Đây là trang môn học "
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi+" "+monhoc
    return chuoi

@ungdung.route('/sinhvien/')
def students():
    chuoi = "Đây là trang các khóa học !"
    return chuoi

@ungdung.route('/sinhvien/<int:namhoc>')
def school_year(namhoc): 
    chuoi = "Đây là năm học "
    nam = str(namhoc).upper()
    if nam == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + nam
    return chuoi

@ungdung.route('/index')
@ungdung.route('/index/<name>')
def index(name=None):
    return render_template('index.html',name=name)

languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
languages.append({'STT':4, 'ten': ".NET" })
languages.append({'STT':5, 'ten': "Matlab" })
@ungdung.route('/abc')
def abc(name=None):
   return render_template('abc.html', ngon_ngu = languages)

@ungdung.route('/duong')
def duong(name=None):
   return render_template('duong.html')

if __name__ == '__main__':
    ungdung.run(port=5050)