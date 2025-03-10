[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/snakemake/snakemake-hpc-teaching-material/build.yml?label=tests)](https://github.com/snakemake/snakemake-hpc-teaching-material/actions?query=branch%3Amain++)
[![Build LaTex sources.](https://github.com/snakemake/snakemake-hpc-teaching-material/actions/workflows/build.yml/badge.svg)](https://github.com/snakemake/snakemake-hpc-teaching-material/actions/workflows/build.yml)
![Mastodon Follow](https://img.shields.io/mastodon/follow/109245696038111591?domain=https%3A%2F%2Ffediscience.org&style=flat)
![Mastodon Follow](https://img.shields.io/mastodon/follow/113407240116926289?domain=fediscience.org&style=flat)

# The Snakemake Teaching Alliance

## Our Mission

The Snakemake HPC Teaching Alliance is committed to advancing Open Science through inclusive, hands-on education in reproducible computing. By fostering accessible and collaborative learning environments, we aim to empower researchers across disciplines to build, share, and sustain reproducible workflows. Our teaching materials, openly available and community-driven, are designed to support diverse learners and promote best practices in high-performance computing (HPC).

## Getting Started

If you are a lecturer, you can use our material under the CC-BY-SA license. The material is quite complex, please contact us for an introduction into it.

[Here are some questions to address when teaching elsewhere for the first time](https://github.com/snakemake/snakemake-hpc-teaching-material/blob/main/Teaching_Elsewhere.md).

## Getting started / Onboarding

If you want to participate in the development: Just notify us (issue) and we will add your github account. Alternatively, you may fork the repo and create PRs from there.

## Purpose

This repository contains (better: will contain) teaching material to teach for

- workflow creators
- workflow users
- administrators

all tailored for HPC systems.

## Development Workflow

Workflow for pull requests:

- create or take an issue to work on (you may assign others or no one). Issues ought to be as specific as possible. We may break "big issues" into smaller ones
- create a branch `"<shortname>_<issue_number>"`. Only in rare case (closely related issues) bundle the work on issues into one branch. The parent branch should always be "main"
- commit your work to branch
- push to origin (your own fork of the snakemake-hpc-teaching-material repository)
- create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 
- assign arbitrary reviewer (or wait until someone takes on this pull reqeust)
- (s.o. else) perform review (switch to branch and try; check the quality)
- merge and delete source branch

## Rendering Slides

In order to typeset the slides you want, you can simply run

```bash
$ ./render --master-tex <tex master document> -c <configfile>
```

Three master slide sets are offered:

- `slides/Snakemake_HPC_Users.tex` - which contains a slide set tailored for users of ready-to use and non-curated workflows, their HPC parameterization and execution
- `slides/Snakemake_HPC_Creators.tex` - which contains a slide set tailored for creators of new workflows.
- `slides/Snakemake_HPC_Admins.tex'' - which contains some slides tailored to administrators to tell them some bits about Snakemake and global configurations.

A lecturer may choose to render a handout version of a slide set with the `--handout` flag. Handouts do not contain some images or slide overlays and are a little bit smaller than full course slide sets.

### Customizing Slides

Configuration files can be found in the config folder. The "generic" one is

- `config/config_Mainz_NHR.yaml`

just because it is the first. Others will follow.The file `config/config_for_github.yaml` is a reduced version intended for the GitHub CI runner and can otherwise be ignored.

In essence, every detail is configurable. Developers can be approached to add new details to be configurable. Any configuration file should be human readable and commented to make sense. 

### LaTeX specialities

This repo contains some unique commands:

- `altverb` to include in-line listings code, e.g. `\altverb{filename}` or `\altverb{--flag}`. Use `\texttt{Name}` for project names, so: `\texttt{Snakemake}`, but `\altverb{snakemake --slurm}` to distinguish the project from the software.
- to include parameters from the config file, use the `<++name++>}` expression, whre "name" can be a part of the config, e.g. `course.pathtosetup`.
