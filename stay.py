from pyoembed import oEmbed, PyOembedException

try:
    # maxwidth and maxheight are optional.
  data = oEmbed('https://www.youtube.com/watch?v=dBD54EZIrZo',
                  maxwidth=640, maxheight=480)
except e:
  print ('An error was ocurred: %s' % e)

# data is a dict with keys that will depends on the media type. You should
# choose how to display the content based on the data['type'] value and
# the oEmbed spec ( http://oembed.com/ ).
# if data['type'] == 'video':
#   print data['html']
print(data['title'])

# and it goes... Someday we will provide default renderes for each media
# type.