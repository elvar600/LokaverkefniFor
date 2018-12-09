#Elvar Halldór Hróarr Sigurðsson
#24.10.18
#Verkefni5

from bottle import*
import pymysql

@route("/")
def index():
    u = request.forms.get("uname")
    p = request.forms.get("psw")

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2303012980', passwd='mypassword', db='2303012980_vef2_loaverkefni')
    c = conn.cursor()
    c.execute("SELECT user FROM 2303012980_vef2_loaverkefni.users")
    result = c.fetchall()
    print(result)
    if result[0]==1:
        cur.execute("INSERT INTO 2303012980_vef2_loaverkefni Values(%s,%s,%s)",(u,p))
    return template("index.tpl",u=u,p=p)
    c.close()
    return template("about.tpl")

@route("/nyfrett")
def index():
    return template("")

@route("/about")
def index():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2303012980', passwd='mypassword', db='2303012980_vef2_loaverkefni')
    c = conn.cursor()
    c.execute("SELECT user FROM 2303012980_vef2_loaverkefni.users")
    result = c.fetchall()
    u = request.query.get("unsme")
    e = request.query.get("email")
    t = request.query.get("titil")
    te = request.query.get("text")
    return template("nyfrett.tpl",u=u,e=e,t=t,te=te)

@post("/data")
def gogn():
    n = request.forms.get("nafn")
    e = request.forms.get("email")
    t = request.forms.get("titil")
    te = request.forms.get("text")
    nam = request.forms.getall("namsk")

    return template("namskeid",n=n,e=e,t=t,te=te,nam=nam)

######################################################
@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

@error(404)
def villa(error):
    return "<h1 style = color:red>Þessi síða finnst ekki</h1>"

try:
    run(host="0.0.0.0", port=os.environ.get('POST'))
except:
    run(debug=True)
