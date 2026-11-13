Variant-calling workflow report
===============================

This report summarizes the outputs of the Snakemake variant-calling
workflow. It includes the bcftools call set, plots derived from that call
set, the SNP-only call set produced by GATK, and a visualization of the
GATK SNP positions.

The configured samples are:

.. code-block:: text

{% for sample, reads in snakemake.config["samples"].items() %}
   {{ sample }}: {{ reads }}
{% endfor %}

The GATK path uses HaplotypeCaller in GVCF mode for each sample, combines the
GVCFs, jointly genotypes them, and selects SNPs from the resulting cohort
VCF. Run the workflow with ``snakemake --use-conda``. After the workflow has
completed, generate this report with ``snakemake --report report.html``.
