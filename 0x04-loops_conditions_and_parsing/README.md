# 0x04-loops_conditions_and_parsing

An introduction to:
 
* How to create SSH keys
* What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
* How to use `while`, `until` and `for` loops
* How to use `if`, `else`, `elif` and `case` condition statements
* How to use the `cut` command
* What are files and other comparison operators, and how to use them

# Requirements
* Files are interpreted on Ubuntu 20.04 LTS
* Bash script must pass `Shellcheck` (version `0.7.0`) without any error
* First line of all your Bash scripts should be exactly `#!/usr/bin/env bash`

# File Descriptions

## Mandatory tasks

[0-RSA_public_key.pub](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub) - Create a SSH RSA key pair 

[1-for_best_school](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/1-for_best_school) - A Bash script that displays `Best School` 10 times, using `for` loop.

[2-while_best_school](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/2-while_best_school) - A Bash script that displays `Best School` 10 times, using `while` loop.

[3-until_best_school](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/3-until_best_school) - A Bash script that displays `Best School` 10 times, using `until` loop.

[4-if_9_say_hi](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/4-if_9_say_hi) - A Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.
* Use a `while` and `if` statement

[5-4_bad_luck_8_is_your_chance](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance) - A Bash script that loops from 1 to 10 and: 
* displays `bad luck` for the 4th loop iteration
* displays `good luck` for the 8th loop iteration
* displays `Best School` for the other iterations
* Use a `while` loop, `if`, `elif` and `else` statements

[6-superstitious_numbers](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/6-superstitious_numbers) - A Bash script that displays numbers from 1 to 20 and:

   * displays `4` and then `bad luck from China` for the 4th loop iteration
   * displays `9` and then `bad luck from Japan` for the 9th loop iteration
   * displays `17` and then `bad luck from Italy` for the 17th loop iteration
   * Use `while` loop and `case` statement

[7-clock](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/7-clock) - A Bash script that displays the time for 12 hours and 59 minutes:

* display hours from 0 to 12
* display minutes from 1 to 59
* use a `while` loop

[8-for_ls](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/8-for_ls) - A Bash script that displays:

* The content of the current directory
* In a list format
* Where only the part of the name after the first dash is displayed
* Use a `for` loop
* Do not display hidden files

[9-to_file_or_not_to_file](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/9-to_file_or_not_to_file) - ABash script that gives you information about the `school` file.

* You must use `if` and, `else`
* Your Bash script should check if the file exists and print:
* if the file exists: `school file exists`
* if the file does not exist: `school file does not exist`
* If the file exists, print:
* if the file is empty: `school file is empty`
* if the file is not empty: `school file is not empty`
* if the file is a regular file: `school is a regular file`
* if the file is not a regular file: (nothing)

[10-fizzbuzz](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/10-fizzbuzz) -  A Bash script that displays numbers from 1 to 100.

* Displays `FizzBuzz` when the number is a multiple of 3 and 5
* Displays `Fizz` when the number is multiple of 3
* Displays `Buzz` when the number is a multiple of 5
* Otherwise, displays the number
* In a list format


# Advanced Tasks

[100-read_and_cut](https://github.com/jubriltayo/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/100-read_and_cut) - A Bash script that displays the content of the file `/etc/passwd`.
Script should only display:
    * username
    * user id
    * Home directory path for the user
    
* use the `while` loop
