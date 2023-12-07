This repository contains a simple example of a Sphinx project that employs
a simple Sphinx extension. The extension implementation is simplified by
using a "nested parse" in which the extension code creates new
reStructuredText that is then parsed internally within the extension
processing. The implementation of the nested parse is described [in this
blog post].

The example extension is in the [_ext](_ext) directory. The
[my_sphinx_extension.py](_ext/my_sphinx_extension.py) code contains the
implementation of the simple extension. This extension uses
[sphinx_nested_parse.py](_ext/sphinx_nested_parse.py), which contains the
implementation of the nested parse functionality.

In this root directory, the [conf.py](conf.py) configuration file shows how
this extension is loaded. The
[try-basic-extension.rst](try-basic-extension.rst?plain=1) shows simple
examples of using the custom directive and role provided by the extension.

[in this blog post]: https://www.drmoron.org/posts/sphinx-nested-parse-extensions/
