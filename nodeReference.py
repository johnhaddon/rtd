import os
import glob
import shutil
import inspect

import IECore
import Gaffer
import GafferUI

def plugs( node ) :

	def walk( parent ) :

		result = ""
		for plug in parent.children( Gaffer.Plug ) :
			result += "## %s \n\n %s \n\n" % ( plug.relativeName( node ), Gaffer.Metadata.plugValue( plug, "description" ) )

		return result

	return walk( node )

modules = []
for modulePath in glob.glob( os.path.expandvars( "$GAFFER_ROOT/python/Gaffer*" ) ) :

	try :
		module = __import__( os.path.basename( modulePath ) )
	except ImportError :
		continue

	if not modulePath.endswith( "Test" ) and not modulePath.endswith( "UI" ) :
		modules.append( module )

shutil.rmtree( "docs/autoGenerated", ignore_errors = True )
os.makedirs( "docs/autoGenerated" )

index = open( "docs/autoGenerated/index.rst", "w" )
index.write(
	"Node Reference\n"
	"==============\n\n"
	".. toctree::\n"
	"   :maxdepth: 1\n\n"
)

for module in modules :

	os.makedirs( "docs/autoGenerated/" + module.__name__ )

	index.write( "   %s/index\n" % module.__name__ )

	moduleIndex = open( "docs/autoGenerated/%s/index.rst" % module.__name__, "w" )
	moduleIndex.write( "%s\n" % module.__name__ )
	moduleIndex.write( "=" * len( module.__name__ ) + "\n\n" )
	moduleIndex.write( ".. toctree::\n" )
	moduleIndex.write( "   :maxdepth: 1\n\n" )

	for name in dir( module ) :

		cls = getattr( module, name )
		if not inspect.isclass( cls ) or not issubclass( cls, Gaffer.Node ) :
			continue

		try :
			node = cls()
		except :
			continue

		with open( "docs/autoGenerated/%s/%s.md" % ( module.__name__, name ), "w" ) as f :

			f.write( "# %s\n\n" % name )
			f.write( "%s\n\n" % Gaffer.Metadata.nodeValue( node, "description" ) )
			f.write( plugs( node ) )

		moduleIndex.write( "   %s\n" % name )
