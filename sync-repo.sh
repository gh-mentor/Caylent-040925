# This bash script uses git to synchronize changes between the local and remote GitHub repository.

# It performs the following steps:
# 1. stage all changes
# 2. commit changes with message 'Updated'
# 3. pull changes from remote repository
# 4. push changes to remote repository on branch 'main'.

# Usage: ./sync-repo.sh


# stage all changes
git add .

# commit changes with message 'Updated'
git commit -m 'Updated'

# pull changes from remote repository
git pull origin main

# push changes to remote repository on branch 'main'
git push origin main

# Echo a message indicating that the synchronization is complete
echo "Synchronization with remote repository complete."