import os

HEADER_TEMPLATE_DIRECTORY = "templates/"
BACKBONE_TEMPLATE_DIRECTORY = "templates/underscore-templates/"


def format_underscore_template(name, content):
    """
    Format the template as an Underscore.js template.
    """
    return '\n<script type="text/template" id="{0}">\n{1}\n</script>\n'.format(name, content)


def assemble_templates(backbone_template_formatter):
    """
    Assemble the header, the footer, and all backbone templates into one string.
    """
    # Grab the header content
    output = open(os.path.join(HEADER_TEMPLATE_DIRECTORY, "base.html")).read()

    # Attach the backbone templates
    templates = ""
    for f in os.listdir(BACKBONE_TEMPLATE_DIRECTORY):
        if f.endswith(".html"):
            name = f.rstrip(".html")
            content = open(os.path.join(BACKBONE_TEMPLATE_DIRECTORY, f), "r").read()
            # It is a template, so add it
            templates += backbone_template_formatter(name, content)
    return output.format(templates=templates)


def build_underscore_templates(builddir):
    # Open the file to build
    if not os.path.exists(builddir):
        os.mkdir(builddir)

    output_file = open(os.path.join(builddir, "index.html"), "w+")
    # Get and write it's content
    output_file.write(assemble_templates(format_underscore_template))
    output_file.close()

# Execute
if __name__ == "__main__":
    import sys
    builddir = sys.argv[1]
    build_underscore_templates(builddir)

    print("Templates built successfully!")
