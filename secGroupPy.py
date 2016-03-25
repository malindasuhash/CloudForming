#!/usr/bin/env python
import boto.ec2
import hashlib

try:
  conn = boto.ec2.connect_to_region("us-west-2")
  currentSgs = conn.get_all_security_groups()
except boto.exception.BotoServerError as e:
   log.error(e.error_message)
conn.close()
 
for sg in currentSgs:
  print "="*72
  print "id:\t\t", sg.id
  print "name:\t\t", sg.name
  print "vpc:\t\t", sg.vpc_id
  print "instance:\t", sg.instances()
  for rule in sg.rules:
    ruledata = sg.id,rule.grants,rule.ip_protocol,rule.from_port,rule.to_port,"$
    rulehash = hashlib.sha256(str(ruledata)).hexdigest()
    print "\thash",rulehash
    print "\t", rule.grants, "-> instances: ", rule.from_port, " - ", rule.to_p$
  print "="*72

