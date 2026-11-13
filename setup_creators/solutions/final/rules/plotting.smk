rule plot_positions:
    input:
        rules.bcftools_call.output,
    output:
        report(
            "calls/positions.png",
            caption="report/positions.rst",
            category="Variant visualizations",
        ),
    script:
        "../scripts/plot-positions.py"


rule plot_quals:
    input:
        "calls/all.vcf",
    output:
        report(
            "calls/quals.svg",
            caption="report/qualities.rst",
            category="Variant visualizations",
        ),
    script:
        "../scripts/plot-quals.py"


rule plot_gatk_snps:
    input:
        "calls/gatk/snps.vcf.gz",
    output:
        report(
            "calls/gatk/snps.png",
            caption="report/gatk-snp-positions.rst",
            category="GATK variant calls",
        ),
    log:
        "logs/gatk/plot_snps.log",
    conda:
        "../envs/plotting.yaml"
    script:
        "../scripts/plot-gatk-snps.py"
