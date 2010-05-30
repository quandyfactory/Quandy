#!/usr/bin/env python

__title__ = 'Gitiot, the one-button git commit GUI'
__version__ = 0.12
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/49/gitiot"
__copyright__ = "(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

"""
Gitiot is a really simple cross-platform GUI wrapper for the most minimal useful subset of git's awesome power - i.e. one-button commit and push-to-master for people who want revision control but don't want to learn the command line.
"""

# standard libraries
import os
import subprocess
from Tkinter import *
import tkMessageBox 

global_commit_comment = 'Commit performed by gitiot v. %s' % __version__
global_config_file = 'gitiot.config'
global_repo_dir = os.path.abspath(os.curdir)
global_master = 'origin'

def make_process(command, repo_dir):
    """
    Executes a command
    """
    pipe = subprocess.Popen(command, shell=True, cwd=repo_dir)
    pipe.wait()
    return

def set_config(repo_dir=global_repo_dir, master=global_master, config_file=global_config_file):
    """
    Sets the config file with repo_dir and master
    """
    try:
        with open(config_file, 'w') as file:
            file.write('%s = %s\n' % ('repo_dir', repo_dir))
            file.write('%s = %s\n' % ('master', master))
    except:
        # fail
        print 'could not set config values'
    
    # try to add config_file to the git exclude
    exclude_file = '%s/.git/info/exclude' % (repo_dir)
    try:
        with open(exclude_file, 'r') as file:
            contents = file.read()
        if config_file not in contents:
            with open(exclude_file, 'a') as file:
                file.write('%s\n' % config_file)
    except:
        # hey, it was worth a shot
        pass
    
    return
    

def get_config(config_file=global_config_file):
    """
    Returns a config dictionary with repo_dir and master
    """
    config = {} # initialize config dict

    try:
        with open(config_file, 'r') as file:
            contents = file.read()
            print 'contents:\n%s' % contents
            lines = [line for line in contents.split('\n') if line.strip() != '' and '=' in line and line.strip()[0] != '#']
            print 'lines:\n%s' % lines
            for line in lines:
                print line
                key, val = line.split('=')
                config[key.strip()] = val.strip()
            
    except:
        config['repo_dir'] = global_repo_dir.strip()
        config['master'] = global_master.strip()
        set_config()

    return config

def git_add(repo_dir):
    """
    Recursively adds all the files that have changed
    """
    return make_process('git add .', repo_dir)

def git_commit(repo_dir, comment=global_commit_comment):
    """
    Commits changed files to the repository
    """
    return make_process('git commit -m \'%s\'' % (comment.replace("'", "\'")), repo_dir)

def git_push_master(repo_dir, master):
    """
    Pushes a commit to a remote master
    """
    return make_process('git push %s master' % (master), repo_dir)

class App:
    def __init__(self,parent):

        f = Frame(parent)
        f.pack(padx=15, pady=15)

        self.comment_label = Label(f, text="Comment")
        self.comment_label.pack(side=TOP, padx=10, pady=0)
        
        self.comment = Text(f, width=60, height=6)
        self.comment.pack(side=TOP, padx=10, pady=0)
        self.comment.insert(1.0, global_commit_comment)
        self.comment.bind("<Tab>", self.focus_next_window)
        
        self.button = Button(f, text="Commit", command=self.execute_commit)
        self.button.pack(side=BOTTOM, padx=20, pady=20)
    
    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    def execute_commit(self):
        """
        Commits the changes to the repository
        """
        config = get_config()
        repo_dir = config['repo_dir']
        master = config['master']
        git_add(repo_dir)
        git_commit(repo_dir, comment=self.comment.get(1.0, END))
        extra_message = ''
        if master != '':
            git_push_master(repo_dir, master)
            extra_message = ' and pushed to the remote master repository'
            
        tkMessageBox.showinfo('Changes Committed', 'Your changes were committed%s.' % (extra_message))

if __name__ == '__main__':
    root = Tk()
    root.title(__title__)
    try:
        root.wm_iconbitmap('%s/%s' % (os.path.abspath(os.curdir), 'git_icon.bmp'))
    except:
        pass
    app = App(root)
    root.mainloop()
    
