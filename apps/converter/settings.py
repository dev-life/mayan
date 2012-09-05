"""Configuration options for the converter app"""

from django.utils.translation import ugettext_lazy as _

from smart_settings import SettingsNamespace, LocalScope

namespace = SettingsNamespace('converter', _(u'Converter'), module='converter.settings')

namespace.add_setting(
    name='IM_CONVERT_PATH',
    default=u'/usr/bin/convert',
    description=_(u'File path to imagemagick\'s convert program.'),
    exists=True,
    scopes=[LocalScope]
)

namespace.add_setting(
    name='IM_IDENTIFY_PATH',
    default=u'/usr/bin/identify',
    description=_(u'File path to imagemagick\'s identify program.'),
    exists=True,
    scopes=[LocalScope]
)

namespace.add_setting(
    name='GM_PATH',
    default=u'/usr/bin/gm',
    description=_(u'File path to graphicsmagick\'s program.'),
    exists=True,
    scopes=[LocalScope]
)

namespace.add_setting(
    name='GM_SETTINGS',
    default=u'',
    description=_(u'Set of configuration options to pass to the GraphicsMagick executable to fine tune it\'s functionality as explained in the GraphicsMagick documentation.'),
    scopes=[LocalScope]
)

namespace.add_setting(
    name='GRAPHICS_BACKEND',
    default=u'converter.backends.python',
    description=_(u'Graphics conversion backend to use.  Options are: converter.backends.imagemagick, converter.backends.graphicsmagick and converter.backends.python.'),
    scopes=[LocalScope]
)

namespace.add_setting(
    name='LIBREOFFICE_PATH',
    default=u'/usr/bin/libreoffice',
    description=_(u'Path to the libreoffice program.'),
    exists=True,
    scopes=[LocalScope]
)

#{'name': u'OCR_OPTIONS', 'global_name': u'CONVERTER_OCR_OPTIONS', 'default': u'-colorspace Gray -depth 8 -resample 200x200'},
#{'name': u'HIGH_QUALITY_OPTIONS', 'global_name': u'CONVERTER_HIGH_QUALITY_OPTIONS', 'default': u'-density 400'},
#{'name': u'PRINT_QUALITY_OPTIONS', 'global_name': u'CONVERTER_PRINT_QUALITY_OPTIONS', 'default': u'-density 500'},