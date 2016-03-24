#!/usr/bin/env python
import boto.ec2

try:
  conn = boto.ec2.connect_to_region("us-east-1")
  currentSgs = conn.get_all_security_groups()
 except boto.exception.BotoServerError, e:
  log.error(e.error_message)
 conn.close()
 
 for sg in currentSgs
  print "id: ", sg.id