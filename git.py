import shlex
import argparse 
import subprocess

def bash(command):
    subprocess.run(['bash', '-c', command])

def git_init():
    bash('git init')

def git_clone():
    bash('git clone')

def git_add():
    bash('git add --all')

def git_commit(args):
    bash('git commit -m ' + f'{args.commit}')

def git_branch(args):
    bash('git branch -M ' + f'{args.branch}')

def git_remote():
    bash('git remote add origin https://github.com/catarinaferrei/projeto-ito.git')

def git_pull():
    bash('git pull https://github.com/catarinaferrei/projeto-ito.git')

def git_push(args):
    bash('git push -u origin ' + f'{args.branch}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--commit', help='Commit message',required=True)
    parser.add_argument('--branch', help='Name of the branch',required=False)
    args = parser.parse_args()
    git_init()
    #git_clone()
    git_add()
    git_commit(args)
    git_branch(args)
    #git_remote()
    git_pull()
    git_push(args)

if __name__ == '__main__':
    main()