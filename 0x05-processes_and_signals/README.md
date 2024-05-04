# 0x05. Processes and signals
`DevOps`
`Shell`
`Bash`
`Syscall`
`Scripting`

## Resources
**Read or watch:**
  * [Linux PID](https://www.linfo.org/pid.html)
  * [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
  * [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
  * [Prcess management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)
  * [Computer Signal](https://www.computerhope.com/unix/signals.htm)

**man or help:**
  * `ps`
  * `pgrep`
  * `pkill`
  * `kill`
  * `exit`
  * `trap`

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:
### General Objective
  * What is a PID
  * What is a process
  * How to find a process’ PID
  * How to kill a process
  * What is a signal
  * What are the 2 signals that cannot be ignored

## Requirements
### General
  * Allowed editors: `vi`, `vim`, `emacs`
  * All your files will be interpreted on Ubuntu 20.04 LTS
  * All your files should end with a new line
  * A `README.md` file, at the root of the folder of the project, is mandatory
  * All your Bash script files must be executable
  * Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
  * The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
  * The second line of all your Bash scripts should be a comment explaining what is the script doing

# Tasks
## 0. What is my PID
Write a Bash script that displays its own PID.
```
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```
**Repo**:
  * GitHub repository: `alx-system_engineering-devops`
  * Directory: `0x05-processes_and_signals`
  * File: `0-what-is-my-pid`