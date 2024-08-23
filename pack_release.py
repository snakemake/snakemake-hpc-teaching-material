#!/usr/bin/env python3

import argparse
import sys
import os
import shutil
import subprocess
import shlex
import zipfile

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required = True,
                        help = "indicate the handout version, e.g. edition")
    parser.add_argument('--pdf', required = True,
                        help = "indicate a PDF document")
    parser.add_argument('--sample-directory', required = True,
                        help = "path to directory with script files (cloze and solution")
    args = parser.parse_args()

    pdf = args.pdf

    handout_version = os.path.splitext(pdf)[0] + '.pdf'
    final_place     = os.path.basename(handout_version)

    file_list=[(handout_version, final_place),
               ('handout/README.txt', 'README.txt')]
    opj         = os.path.join
    for root, dirs, files in os.walk(args.sample_directory):
        for fname in files:
            # restrict to sample files, no helper files
            if 'copy' in fname or 'README' in fname: continue
            file_list.append((opj(root,fname), opj(*root.split('/')[1:],fname)))

    buildzipfname = 'snakemake_intro_%s.zip' % args.version
    z = zipfile.ZipFile(buildzipfname, 'w', compression = zipfile.ZIP_DEFLATED)
    for item in file_list:
        z.write(item[0], item[1])
    z.close()

