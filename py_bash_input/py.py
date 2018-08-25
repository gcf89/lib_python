#!/usr/bin/env python

#import subprocess
#
#output
#try:
#	res = subprocess.check_output("bash input.sh < data", stderr=subprocess.STDOUT, shell=True)
#	print res
#except subprocess.CalledProcessError:
#	print "Process exit code != 0"

from subprocess import Popen, PIPE, STDOUT


def run_cmd(cmd):
	proc = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
	proc.wait()
	stdout, stderr = proc.communicate()
	return proc.returncode, stdout, stderr


def run_cmd2(cmd):
	proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	stdout, stderr = proc.communicate()
	return proc.returncode, stdout


rt, out, err = run_cmd("bash input.sh < data")

print 'retcod:', rt
print 'stdout:', out
print 'stderr:', err

rt, out = run_cmd2("bash input.sh < data")

print 'retcod:', rt
print 'stdout:', out

