import os

BUILD_DIRECTORY = "build/"
HEADER_TEMPLATE_DIRECTORY = "templates"
BACKBONE_TEMPLATE_DIRECTORY = "templates/underscore-templates/"

def format_underscore_template(name, content):
	"""
	Format the template as an Underscore.js template.
	"""
	return '<script type="text/template" id="{0}">\n{1}\n</script>'.format(name, content)


def build_underscore_templates():
	# Open the file to build
	file = open(BUILD_DIRECTORY + "index.html", "w+")
	# Get and write it's content
	file.write(assemble_templates)
	file.close()

