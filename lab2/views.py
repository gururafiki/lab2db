from django.shortcuts import render, redirect
import MySQLdb
import csv
import codecs

def lab2(request):
    table_name = 'tasks'
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="projects")
    cur = db.cursor()
    cur.execute("SELECT * FROM " + table_name)
    rows = cur.fetchall()
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '" + table_name + "' AND `TABLE_SCHEMA` = 'projects'")
    cols = cur.fetchall()
    cur.execute("SELECT * FROM languages")
    languages = cur.fetchall()
    cur.execute("SELECT * FROM employers")
    employers = cur.fetchall()
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    cur.execute("SELECT * FROM projects")
    projects = cur.fetchall()
    db.close()
    return render(request,'./templates/lab1db/show.html',locals())

def show(request):
    if request.method == "POST":
        table_name = request.POST['table_name']
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="" , db="projects")
        cur = db.cursor()
        cur.execute("SELECT * FROM "+table_name)
        rows = cur.fetchall()
        cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '"+table_name+"' AND `TABLE_SCHEMA` = 'projects'")
        cols = cur.fetchall()
        cur.execute("SELECT * FROM languages")
        languages = cur.fetchall()
        cur.execute("SELECT * FROM employers")
        employers = cur.fetchall()
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
        cur.execute("SELECT * FROM projects")
        projects = cur.fetchall()
        db.close()
    return render(request,'./templates/lab1db/show.html',locals())

def delete(request):
    if request.method == "POST":
        row_id = request.POST['row_id']
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="" , db="projects")
        cur = db.cursor()
        cur.execute("DELETE FROM `projects`.`tasks` WHERE `id` = "+row_id)
        db.commit()
        db.close()
    return redirect('/lab2')


def confirm_update(request):
    if request.method == "POST":
        row_id = request.POST['row_id']
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="" , db="projects")
        cur = db.cursor()
        cur.execute("UPDATE `projects`.`tasks` SET `name`='"+request.POST['name']+"', `project_id`='"+request.POST['project_id']+"', `employee_id`='"+request.POST['employee_id']+"', `employer_id`='"+request.POST['employer_id']+"', `language_id`='"+request.POST['language_id']+"', `difficulty`='"+request.POST['difficulty']+"', `date`='"+request.POST['date']+"', `description`='"+request.POST['description']+"' WHERE `id`='"+request.POST['row_id']+"'")
        db.commit()
        db.close()
    return redirect('/lab2')


def update(request):
    if request.method == "POST":
        row_id = request.POST['row_id']
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="" , db="projects")
        cur = db.cursor()
        table_name = 'tasks'
        cur.execute("SELECT * FROM " + table_name)
        rows = cur.fetchall()
        cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '" + table_name + "' AND `TABLE_SCHEMA` = 'projects'")
        cols = cur.fetchall()
        cur.execute("SELECT * FROM languages")
        languages = cur.fetchall()
        cur.execute("SELECT * FROM employers")
        employers = cur.fetchall()
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
        cur.execute("SELECT * FROM projects")
        projects = cur.fetchall()
        db.close()
    return render(request, './templates/lab1db/show.html', locals())

def searchword(request):
    if request.method == "POST":
        table_name=request.POST['tablename']
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="projects")
        cur = db.cursor()
        if request.POST['type']=='with':
            cur.execute("SELECT * FROM `projects`.`" + table_name + "` WHERE MATCH (name,description) AGAINST ('+"+request.POST['searched']+"' IN BOOLEAN MODE)")
        else:
            cur.execute("SELECT * FROM `projects`.`" + table_name + "` WHERE MATCH (name,description) AGAINST ('+added -"+request.POST['searched'] + "' IN BOOLEAN MODE)")
        rows = cur.fetchall()
        cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '" + table_name + "' AND `TABLE_SCHEMA` = 'projects'")
        cols = cur.fetchall()
        db.close()
        return render(request,'./templates/lab1db/show.html',locals())
    else:
        return redirect('/lab2')

def searchvarchars(request):
    if request.method == "POST":
        table_name=request.POST['tablename']
    else:
        table_name='projects'
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="projects")
    cur = db.cursor()
    cur.execute("SELECT * FROM `projects`.`" + table_name + "` WHERE MATCH (name,description) AGAINST ('" + request.POST['cells'] + "' IN BOOLEAN MODE)")
    rows = cur.fetchall()
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '" + table_name + "' AND `TABLE_SCHEMA` = 'projects'")
    cols = cur.fetchall()
    db.close()
    return render(request,'./templates/lab1db/show.html',locals())

def searchdigit(request):
    if request.method == "POST":
        table_name=request.POST['tablename']
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="projects")
        cur = db.cursor()
        cur.execute("SELECT * FROM " + table_name + " WHERE `id` >= '" + request.POST['start'] + "' AND `id` <= '" + request.POST['end'] +"'")
        rows = cur.fetchall()
        cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '" + table_name + "' AND `TABLE_SCHEMA` = 'projects'")
        cols = cur.fetchall()
        db.close()
        return render(request,'./templates/lab1db/show.html',locals())
    else:
        return redirect('/lab2')


def create(request):
    if request.method == "POST":
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="" , db="projects")
        cur = db.cursor()
        if request.POST['project_name']:
            cur.execute("INSERT INTO `projects`.`projects` (`name`, `description`) VALUES ( '"+request.POST['project_name']+"','added by user')")
            project_id = request.POST['project_name']
        else:
            project_id = request.POST['project_id']
        if request.POST['language_name']:
            cur.execute("INSERT INTO `projects`.`languages` (`name`, `description`) VALUES ( '"+request.POST['language_name']+"','added by user')")
            language_id = request.POST['language_name']
        else:
            language_id = request.POST['language_id']
        if request.POST['employee_name']:
            cur.execute("INSERT INTO `projects`.`employees` (`name`, `description`) VALUES ( '"+request.POST['employee_name']+"','added by user')")
            employee_id = request.POST['employee_name']
        else:
            employee_id = request.POST['employee_id']
        if request.POST['employer_name']:
            cur.execute("INSERT INTO `projects`.`employers` (`name`, `description`) VALUES ( '"+request.POST['employer_name']+"','added by user')")
            employer_id = request.POST['employer_name']
        else:
            employer_id = request.POST['employer_id']
        cur.execute("INSERT INTO `projects`.`tasks` (`name`, `project_id`, `employee_id`, `employer_id`, `language_id`, `difficulty`, `date`, `description`) VALUES ( '"+request.POST['name']+"', '"+project_id+"', '"+employee_id+"', '"+employer_id+"', '"+language_id+"', '"+request.POST['difficulty']+"', '"+request.POST['date']+"', '"+request.POST['description']+"')")
        db.commit()
        db.close()
    return redirect('/lab2')

def upload(request):
    if request.POST and request.FILES:
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="" , db="projects")
        cur = db.cursor()
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        i = 0
        for row in reader:
            if i == 0:
                i = 1
                continue
            cur.execute("SELECT * FROM `projects`.`languages` WHERE `name` = '"+row[5]+"'")
            languages = cur.fetchall()
            if not languages:
                cur.execute("INSERT INTO `projects`.`languages` (`name`, `description`) VALUES ( '" + row[5] + "','added from file')")
            cur.execute("SELECT * FROM `projects`.`projects` WHERE `name` = '" + row[2] +"'")
            projects = cur.fetchall()
            if not projects:
                cur.execute("INSERT INTO `projects`.`projects` (`name`, `description`) VALUES ( '" + row[2] + "','added from file')")
            cur.execute("SELECT * FROM `projects`.`employees` WHERE `name` = '" + row[3]+"'")
            employees = cur.fetchall()
            if not employees:
                cur.execute("INSERT INTO `projects`.`employees` (`name`, `description`) VALUES ( '" + row[3] + "','added from file')")
            cur.execute("SELECT * FROM `projects`.`employers` WHERE `name` = '" + row[4]+"'")
            employers = cur.fetchall()
            if not employers:
                cur.execute("INSERT INTO `projects`.`employers` (`name`, `description`) VALUES ( '" + row[4] + "','added from file')")
            cur.execute("INSERT INTO `projects`.`tasks` (`name`, `project_id`, `employee_id`, `employer_id`, `language_id`, `difficulty`, `date`, `description`) VALUES ( '" +row[1] + "', '" + row[2] + "', '" + row[3] + "', '" + row[4] + "', '" + row[5] + "', '" + row[6] + "', '" + row[7] + "', '" + row[8] + "')")
            db.commit()
        csvfile.close()
        db.close()
    return redirect('/lab2')

