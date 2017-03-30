# Sublime Plugin to convert Tab Delimited Table to Markdown

This plugin will help you create GitLab flavored markdown tables from SQL Server
or Excel copy pasta. Any tab delimited table should be applicable.

# Installation
Right now, I don't know how to create a proper package. The whole process seems daft. For now, I'm just copying these files, and dropping them into my user packages.

- Windows: Copy the files to `%APPDATA%\Sublime Text 3\Packages`. You can use `Preferences > Browse Packages` to quickly open this folder.
- OSX (untested, from memory): Copy the files to `~/Librar/Application Support/Sublime Text 3/Packages`. You can use a Sublime menu command to quickly open this folder.

# Usage

- __Before pasting the results you wish to transform, ensure "Indent Using Spaces"
is false.__ This is a setting in the bottom right of Sublime Text. If you click
where it says "Spaces: 2 (or 4, or whatever)" you will see the option to disable
this if it's enabled.
- Paste your data from SSMS or Excel
- ctrl/cmd + shift + p to open the command pallete, and select "SQL Tabbed Table to Markdown" (I like using "sql md").
- Your final results may need to be tweaked, but 99% of the time it works 100% of the time. Sometimes. Usually. ?

# Behind the scenes
This plugin takes the current window's text buffer, and iterates each line in reverse doing the following:
- Transform any `|` characters to `_`, essentially escaping markdown's column separator
- Transform all line beginnings, endings, and tab characters to `|`

We go in reverse because we are modifying the lines in the buffer, which breaks the line position offsets. For example, given the following line offsets:

```
[
  [0,   100],
  [101, 200],
  [201, 300]
]
```
If you add two characters to the first element, making it `[0,102]` -- the second element is no longer accurate. It should now be [103, 202]. If you go in reverse, you don't break anything. Neat!

Finally, it grabs the first line, which represents your column headings (hopefully!) and use it to generate a nice looking seperator row
  - Convert each column name character to `-` so it is the same length as the actual name
  - If there are not at least 3 characters for the column name, use `---`, as GLF markdown requires that.


# Maintenance, contributing, etc.
I don't write Python code. I've never written a Sublime plugin. I found the process gruelling, and I know this isn't amazing code. I just needed a tool that worked, and this worked. If you can improve it, I'd love to accept pull/merge requests.
