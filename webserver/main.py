from bottle import route, run, static_file

@route('/home')
def home():
    return static_file('home.html', root='/home/swannsg/development/UAS/html')

@route('/home/swannsg/development/UAS/bower_components/bootstrap/dist/css/<filename>')
def static01(filename):
    print 'static01'
    return static_file(filename,
                       root='/home/swannsg/development/UAS/bower_components/bootstrap/dist/css')

@route('/home/swannsg/development/UAS/bower_components/bootstrap/dist/js/<filename>')
def static02(filename):
    print 'static02'
    return static_file(filename,
                       root='/home/swannsg/development/UAS/bower_components/bootstrap/dist/js')

@route('/home/swannsg/development/UAS/bower_components/jquery/dist/<filename>')
def static03(filename):
    print 'static03'
    return static_file(filename,
                       root='/home/swannsg/development/UAS/bower_components/jquery/dist')


@route('/home/swannsg/development/UAS/bower_components/angular/<filename>')
def static04(filename):
    print 'static04'
    return static_file(filename,
                       root='/home/swannsg/development/UAS/bower_components/angular')

@route('/home/swannsg/development/UAS/bower_components/html5shiv/dist/<filename>')
def static05(filename):
    print 'static05'
    return static_file(filename,
                       root='/home/swannsg/development/UAS/bower_components/html5shiv/dist')

@route('/home/swannsg/development/UAS/bower_components/respond/dest/<filename>')
def static06(filename):
    print 'static06'
    return static_file(filename,
                       root='/home/swannsg/development/UAS/bower_components/respond/dest')

run(reloader=True)    
run(host='localhost', port=8080, debug=True)

