import sublime
import sublime_plugin
import re

class SqlTabTableToMarkdownCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    #self.view.insert(edit, 0, "Hello, World!")

    region = sublime.Region(0, self.view.size())

    # lines_as_regions = self.view.split_by_newlines(region)
    # lines_as_text = (self.view.substr(r)
    #         for r in self.view.split_by_newlines(region))


    # For each line in window:
    #   Get string
    #   Convert column separator (|) to _
    #   Convert ^|\t|$ to column separator (|)
    #
    # Duplicate first line
    # Convert anything not a column separator to a -

    # Do this backwards, so that the next region acted upon
    #   is correct as the lines get modified
    # i.e., given regions [(0,10)(11,20)]
    #   If you modify the length if region[0] to (0,12), region[1] is no longer accurate.
    #   If you go backwards, you avoid this without having to recalc the regions
    for line in reversed(self.view.split_by_newlines(region)):
      text = self.view.substr(line)
      text = re.sub(re.escape("|"), "_", text)
      text = re.sub(r"(^|\t|$)", "|", text)
      self.view.replace(edit, line, text)

    # For anything that's not a pipe (col_seperator), turn to '-', and ensure at
    #   least "---" is present.
    # Remove the first and last elements, because each row starts and ends
    #   with |, and the blank string fits the < 3 rule
    column_names = self.view.substr(self.view.split_by_newlines(region)[0])
    seperator_row = "|" + "|".join(map(lambda name: "-" * len(name) if len(name) >= 3 else "---", column_names.split("|")[1:-1])) + "|"

    self.view.insert(edit, self.view.split_by_newlines(region)[1].begin(), seperator_row + "\n")
