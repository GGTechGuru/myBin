#! /home/sbp366x24/Desktop/DJANGO/django_env/bin/python3

# Function: fn_dirops

# In:
#	Target directory path
#	Script to act on directory entry: Op_Script

# Out: NA


# Steps:

# Get and record current directory: CWD0

# Get permissions on current directory: P0

# Add user write permissions on current directory

# Get current list of all entries in current directory: E0[i]

# For each E0[i]:
#     Execute Op_Script on E0[i]

# Revert permissions of current directory to original: P0

# Again, get updated list of all entries in current directory: E1[i]

# For each E1[i]:
#    If E1[i] is a directory
#        Build full path for E1[i] E1FP[i]
#        Recursively call fn_dirops on E1FP[i] with OpScript
#        Change directory back to CWD0: 

# Change directory to CWD0 again at end of loop

