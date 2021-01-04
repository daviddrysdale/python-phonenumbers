all
rule 'MD013', :line_length => 120
rule 'MD007', :indent => 4
exclude_rule 'MD010' # Go code samples have tabs
exclude_rule 'MD031' # embedmd markers are next to fenced code blocks
exclude_rule 'MD033' # allow inline HTML, esp. <sup>
