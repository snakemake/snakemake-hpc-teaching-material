#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import glob
import os
import sys
import subprocess
import re

PATH = os.path.split(os.path.realpath(__file__))[0]

from jinja2 import Environment, FileSystemLoader

options = { 'block_start_string': r'\Block<',
            'block_end_string': '>',
            'variable_start_string': r'\Var<',
            'variable_end_string': '>',
            'autoescape': True,
          }

jinja_env = Environment(loader = FileSystemLoader(PATH), **options)

class Login(dict):
    def __init__(self,
                 login  = None,
                 passwd = None,
                 index  = None):
        self['login']   = login 
        self['passwd']  = passwd
        self['index']   = index
    def __repr__(self):
        return '%s_%s' % (self['login'], self['passwd'])

def get_numeric_index(name):
    """Extract numeric index from a login name (e.g., 'csc-course1' -> 1, 'mpi_ws_01' -> 1)"""
    match = re.search(r'(\d+)$', name)
    if match:
        return int(match.group(1))
    return None

def render_people(env, template):
    #template=template.encode('utf-8')
    tpl = jinja_env.get_template(template)
    x = tpl.render(env) #.encode('utf-8')
    print(type(x))
    #sys.exit()
    return x

def to_file(tex, fname='out.tex', path='.'):
    with open(os.path.join(path, fname), 'w') as f:
        f.write(tex)

def run_pdflatex(fname='out.tex', path='.'):
    return subprocess.call(['pdflatex', '-interaction=nonstopmode', fname], cwd=path, 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def concatenate_pdfs():
    fnames = sorted(glob.glob('login_*.pdf'))
    if not fnames:
        return
    items  = ['pdfunite'] + fnames + ['all_logins.pdf']
    print(items)
    subprocess.call(items)

def parse_logins(infile):
    # skip header
    infile.readline()
    logins = list()
    for line in infile:
        if ',' in line:
            items = line.split(',')
        elif ';' in line:
            items = line.split(';')
        else:
            items = line.split()
        if '"' in line:
           login = Login(items[0].strip('"'), items[-1].strip('"'))
        else:
            login = Login(items[0], items[-1])
        logins.append(login)
    return logins

def parse_pc_logins(filename):
    """Parse PC accounts from Snakemake_Kurs_Nov2026_CSC.csv or meesters_list.csv
    Handles both CSV format (comma-separated) and whitespace-separated format
    """
    logins = {}
    with open(filename, 'r') as f:
        first_line = f.readline()  # skip header
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Try CSV format first
            if ',' in line:
                items = line.split(',')
                if len(items) >= 2:
                    pc_login = items[0].strip().strip('"')
                    pc_passwd = items[1].strip().strip('"')
                    index = get_numeric_index(pc_login)
                    logins[index] = Login(pc_login, pc_passwd, index)
            else:
                # Handle whitespace-separated format (like meesters_list.csv)
                # Format: login<whitespace>password<whitespace>course_pw
                # We need the 1st column (login) and 2nd column (password)
                items = line.split()
                if len(items) >= 2:
                    pc_login = items[0].strip()
                    pc_passwd = items[1].strip()
                    index = get_numeric_index(pc_login)
                    logins[index] = Login(pc_login, pc_passwd, index)
    return logins

def parse_cluster_logins(filename):
    """Parse cluster accounts from meesters_list.csv
    Format: login<whitespace>password<whitespace>course_pw
    We need the 1st column (login) and 3rd column (course_pw)
    """
    logins = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Split by whitespace, handling multiple spaces
            items = line.split()
            if len(items) >= 3:
                cluster_login = items[0].strip()
                cluster_passwd = items[2].strip()
                index = get_numeric_index(cluster_login)
                logins[index] = Login(cluster_login, cluster_passwd, index)
    return logins

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "User Login for Courses Generator")
    parser.add_argument('--pc-file', dest = 'pc_file', default='Snakemake_Kurs_Nov2026_CSC.csv',
                        help = "CSV file with PC accounts (default: Snakemake_Kurs_Nov2026_CSC.csv)")
    parser.add_argument('--cluster-file', dest = 'cluster_file', default='meesters_list.csv',
                        help = "CSV file with cluster accounts (default: meesters_list.csv)")
    parser.add_argument('--passwordfile', dest = 'passwordfile', nargs = '?', type = argparse.FileType('r'),
                        default = None, help = "Deprecated: use --pc-file instead")
    parser.add_argument('--qrdict', dest='qrdict', help='Indicates the directory where qr-code pngs are stored')
    parser.add_argument('--cleanup', dest = 'clean', action='store_true', default=False, help = 'will clean up and exit')
    args = parser.parse_args()

    if args.clean:
        for fname in glob.glob('login*pdf'):
            os.remove(fname)
        for fname in glob.glob('*aux'):
            os.remove(fname)
        for fname in glob.glob('login_hpcgst*tex'):
            if 'template' in fname: continue
            os.remove(fname)
        for fname in glob.glob('login_hpcgst*log'):
            os.remove(fname)
        sys.exit()

    # Parse both PC and cluster logins as dictionaries indexed by numeric index
    pc_logins = parse_pc_logins(args.pc_file)
    cluster_logins = parse_cluster_logins(args.cluster_file)
    
    print("PC Logins:", pc_logins)
    print("Cluster Logins:", cluster_logins)

    # a general data-dict to produce / display the environment
    data = dict()

    # Find common indices between PC and cluster logins
    common_indices = sorted(set(pc_logins.keys()) & set(cluster_logins.keys()))
    
    print(f"Common indices: {common_indices}")
    
    # Generate login sheets for matching pairs
    for idx in common_indices:
        pc_login = pc_logins[idx]
        cluster_login = cluster_logins[idx]
        
        # Escape special LaTeX characters
        pc_name = pc_login['login'].replace('_', r'\_').replace('$', r'\textdollar ')
        pc_pwd = pc_login['passwd'].replace('_', r'\_').replace('$', r'\textdollar ')
        
        cluster_name = cluster_login['login'].replace('_', r'\_')
        cluster_pwd = cluster_login['passwd'].replace('$', r'\textdollar ').replace('_', r'\_')
        
        data['member'] = {'login': pc_name, 'passwd': pc_pwd}
        data['cluster'] = {'login': cluster_name, 'passwd': cluster_pwd}
        
        if args.qrdict:
            data['member']['qr'] = os.path.join(args.qrdict, pc_login['login'])
        
        tex = render_people(data, 'login_hpcgst_template.tex')
        print(type(tex))
        
        # Use PC login name for output filename
        to_file(tex, fname='login_%s.tex' % pc_login['login'])
        run_pdflatex(fname='login_%s.tex' % pc_login['login'])
    
    if len(common_indices) > 0:
        concatenate_pdfs()


