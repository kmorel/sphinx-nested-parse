import docutils.nodes
import docutils.parsers.rst

import sphinx_nested_parse

class FunFact(docutils.parsers.rst.Directive):
    has_content = True
    def run(self):
        current_source = self.state.document.current_source
        current_line = self.lineno
        parse = sphinx_nested_parse.NestedParseNodes()
        parse.add_line('.. admonition:: Fun Fact', current_source, current_line)
        parse.add_line('', current_source, current_line)
        for line in self.content:
            parse.add_line('   ' + line, current_source, current_line)
        return parse.get_nodes(self)

def doi_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return sphinx_nested_parse.role_nested_parse(
        '`doi:%s <https://dx.doi.org/%s>`_' % (text, text), lineno, inliner)

def setup(app):
    app.add_directive('funfact', FunFact)
    app.add_role('doi', doi_role)
