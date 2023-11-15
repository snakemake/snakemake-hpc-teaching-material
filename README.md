# The Snakemake Teaching Alliance

## Purpose

This repository contains (better: will contain) teaching material to teach for

- workflow creators
- workflow users
- administrators

all tailored for HPC systems.

## Getting started

If you want to participate in the development: Just notify us (issue) and we will add your github account.

For every issue:

- create a branch `"<shortname>_<issue_number>"`
- do a pull (request) 

## Progress

Currently, the LaTeX code contains TODO and FIXME items. They should all be removed and become githug issues. In order to list TODO items, run the `todo` script, e.g.

```bash
$ todo slides/
``` 

Otherwise, create issue reports. 

## LaTeX specialities

This repo contains some unique commands:

- `altverb` to include in-line listings code, e.g. `\altverb{filename}` or `\altverb{--flag}`. Use `\texttt{Name}` for project names, so: `\texttt{Snakemake}`, but `\altverb{snakemake --slurm}` to distinguish the project from the software.
- to include parameters from the config file, use the `\configparam{<name>}` command
