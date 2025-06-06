# You need to teach this course on an - unknown - cluster?

Then send this questionnaire to your hosting site. Ask for all questions to be answered unless a public documentation link can be provided, which answers these questions, partially.

## Questionnaire

This questionnaire helps to ask the right questions:

- Organization:
  - Who is the contact for organizing this course? 
  - If this is a topical course (e.g. for Bioinformaticians, Physicist, etc.): Does the organization employ a support scientist for the intended topic? If so, which are the contact details?

- What does the course room look like?
  - How many seats and PC-screens are available?
  - Is there a "Presenter PC"?
  - Is it possible to plug in a laptop? (HDMI and/or VGA?)
  - Please describe the "projector situation" (1 or more, need to have a key?).
  - Does the lecturer need an adaptor for the video projector?
  - Is paired programming possible during the course considering the classroom's seating?
  - Possibly: Which is the standard for power outlets? When the lecturer is teaching abroad.

- Login and Security:
  - Which is the recommended software to log in? (putty, mobaxterm, powershell or plain ssh via Linux - or a terminal on demand)
  - Is 2FA enforced? If so: How?
    If there is no 2FA: Any other security measures to consider?
  - ssh-keys - are they to be prepared? (How? By the participants? Or centrally by the hosting site?)
  - Does the site use course accounts?
  - Will the site prepare login information to be shared with the lecturer? (e.g. featuring login information on login sheets, login slides, etc.)
  - Which is the OS for participant PCs? 
  - May, or should participants bring their own device? If so:
    - Will there be information about it? 
    - Will there be wifi? 
    -  Will there be power outlets?

- Cluster Specialities
  - May the course use a shared file space for the setup to be copied to? E.g. a workspace? Which are the quota limitations?
  - Are there quotas for the HOME directory (size, file number)?
  - Which compute node scratch mount points are provided (for stage-in/out)?
  - Which editors or IDEs are provided? Is there an IDE via an OnDemand system (if so, which URL)?
  - Which applications are available to display a simple plot (png, jpeg, svg)?
  - Will the admins provide a reservation? A "magnetic" reservation for course accounts is preferred, as then no need to adapt the course material is required.
  - Which partitions does the cluster provide for SMP programs (any restrictions for such software)?
  - Which partitions does the cluster provide for software (e.g. MPI) using >=1 full nodes?
  - How does the cluster support GPU application resource requests (special partitions? special SLURM flags?)?
  - How long will the course run (number of days)? (our minimum is 2 days for the full creator course and 1 day for the user-only course)
  - Does the cluster provide a scratch file system on compute nodes? If yes: what is the path?

- Misc
  - Do colleagues on site want to be trained as trainers?
  - Should the lecturer provide a brief overview for administrators on-site?  (30 min. plus discussion and questions)

Note: References (e.g. URLs to internal documentation) are welcome and might save you from spending too much time on your feedback.

