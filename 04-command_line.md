# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

 * `pwd` - print working directory
 * `hostname` - my computer's network name
 * `mkdir` - make directory
 * `cd` - change directory
 * `ls` - list directory
 * `rmdir` - remove directory
 * `pushd` - push directory
 * `popd` - pop directory (using pushd and popd helps you easily switch between two directories)
 * `cp` - copy directory
 * `mv` - move a file or directory
 * `less` - page through a file
 * `cat` - print the whole file
 * `xargs` - execute arguments
 * `find` - find files, EX: `find <startdir> -name <wildcard> -print`
 * `grep` - find things inside files
 * `man` - read a manual page
 * `apropos` - find which manual page is appropriate
 * `env` - look at your environment
 * `echo` - print some arguments
 * `export` - export/set a new environment variable
 * `exit` - exit the shell
 * `sudo` - **DANGER** become super user
 * `chmod` - change permission modifiers
 * `chown` - change ownership
 
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> `ls` lists all files and directories in the current directory (or in other directories given as an argument)
>
> `ls -a` include directory entries whose names begin with a dot
>
> `ls -l` list in long format. The following information is given for each file: file mode, number of links, owner name, group name, number of bytes in file, abbr month, day-of-month file was last modified, hour last modified, minute last modified, pathname.
>
> `ls -lh` use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less
>
> using `ls -la` or `ls -lha` will include directory entries that begin with a dot and list the file information in long format 

---


---

What does `xargs` do? Give an example of how to use it.

> `xargs` constructs argument lists and executes utility. By default, `xargs` executes /bin/echo over the input, but can also be combined with other commands.
>
> It is often used with the `find` command to find certain types of files and perform an action on them, such as deleting them. EX: `find . -name "*.txt" | xargs rm -rf` deletes all files with the .txt file extension. If there are spaces or new lines in the filename, the -print0 and -0 options must be used for the command to execute. EX: `find . -name "*.txt" -print0 | xargs -0 rm -rf`
>
> It can also be used with the `grep` command to filter files from the search results of a find command. EX: `find . -name "*.txt" | xargs grep "rhubarb"` will find all text files in the current directory and return only those that contain the string "rhubarb".

---
