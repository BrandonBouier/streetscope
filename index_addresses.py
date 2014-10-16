import sys
import csv
import re
import os
from urlparse import urlparse
from elasticsearch import Elasticsearch

if os.environ.get('BONSAI_URL'):
  url = urlparse(os.environ['BONSAI_URL'])
  bonsai_tuple = url.netloc.partition('@')
  ELASTICSEARCH_HOST = bonsai_tuple[2]
  ELASTICSEARCH_AUTH = bonsai_tuple[0]
  es = Elasticsearch([{'host': ELASTICSEARCH_HOST}], http_auth=ELASTICSEARCH_AUTH)
else:
  es = Elasticsearch()

files_given = sys.argv
for file_name in files_given:
  if file_name = 'index_addresses.py':
    continue
  else:
    file_path = file_name
    print 'adding ' + file_path

    with open(file_path, 'r') as csvfile:
      print "open file"
      csv_reader = csv.DictReader(csvfile, fieldnames=[], restkey='undefined-fieldnames', delimiter=',')

      current_row = 0
      for row in csv_reader:
        current_row += 1
        if current_row == 1:
          csv_reader.fieldnames = row['undefined-fieldnames']
          continue
        address = row
        es.index(index='addresses', doc_type='address', id=current_row-1, body={'NUMBER': address[' NUMBER'], 'STREET': address[' STREET'], 'ADDRESS': address[' NUMBER'] + ' ' + address[' STREET'], 'X': address['LON'], 'Y': address[' LAT']})

    csvfile.close()
