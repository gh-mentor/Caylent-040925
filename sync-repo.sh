# This bash script uses git to synchronize changes between the local and remote GitHub repository.

# steps:
# 1. stage all changes
# 2. commit changes with message 'Updated'
# 3. pull changes from remote repository
# 4. push changes to remote repository on branch 'main'.

# step 1: stage all changes
git stage .

# step 2: commit changes with message 'Updated'
git commit -m "Updated"

# step 3: pull changes from remote repository
git pull origin main

# step 4: push changes to remote repository on branch 'main'
git push origin main

# echo a message indicating that the script has finished running
