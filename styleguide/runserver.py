#!/usr/bin/env python
from styleguide import app
app.debug = True
if __name__ == '__main__':
  app.run(port=5001,host='0.0.0.0')
