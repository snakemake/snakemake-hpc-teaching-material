rule bcftools_call:
    input:
        fa="data/genome.fa",
        bam=expand("sorted_reads/{sample}.bam", sample=config["samples"]),
        bai=expand("sorted_reads/{sample}.bam.bai", sample=config["samples"]),
    output:
        report(
            "calls/all.vcf",
            caption="report/bcftools-calls.rst",
            category="Variant calls",
        ),
    log:
        "logs/bcftools_call/bcftools.log",
    shell:
        "(bcftools mpileup -f {input.fa} {input.bam} | "
        "bcftools call -mv - > {output}) 2> {log}"


rule gatk_reference_files:
    input:
        ref="data/genome.fa",
    output:
        fai="data/genome.fa.fai",
        dict="data/genome.dict",
    log:
        "logs/gatk/reference.log",
    conda:
        "../envs/gatk.yaml"
    shell:
        "samtools faidx {input.ref:q} && "
        "gatk CreateSequenceDictionary -R {input.ref:q} -O {output.dict:q} "
        "> {log:q} 2>&1"


rule gatk_haplotypecaller:
    input:
        ref="data/genome.fa",
        fai="data/genome.fa.fai",
        dict="data/genome.dict",
        bam="sorted_reads/{sample}.bam",
        bai="sorted_reads/{sample}.bam.bai",
    output:
        gvcf="calls/gatk/gvcfs/{sample}.g.vcf.gz",
    log:
        "logs/gatk/haplotypecaller/{sample}.log",
    params:
        extra="",
        java_opts="",
    threads: 4
    resources:
        mem_mb=1024,
    wrapper:
        "v3.1.0/bio/gatk/haplotypecaller"


rule gatk_combinegvcfs:
    input:
        ref="data/genome.fa",
        fai="data/genome.fa.fai",
        dict="data/genome.dict",
        gvcfs=expand(
            "calls/gatk/gvcfs/{sample}.g.vcf.gz",
            sample=config["samples"],
        ),
    output:
        gvcf="calls/gatk/cohort.g.vcf.gz",
    log:
        "logs/gatk/combinegvcfs.log",
    params:
        extra="",
        java_opts="",
    resources:
        mem_mb=1024,
    wrapper:
        "v3.1.0/bio/gatk/combinegvcfs"


rule gatk_genotypegvcfs:
    input:
        ref="data/genome.fa",
        fai="data/genome.fa.fai",
        dict="data/genome.dict",
        gvcf=rules.gatk_combinegvcfs.output.gvcf,
    output:
        vcf="calls/gatk/all.vcf.gz",
    log:
        "logs/gatk/genotypegvcfs.log",
    params:
        extra="",
        java_opts="",
    resources:
        mem_mb=1024,
    wrapper:
        "v3.1.0/bio/gatk/genotypegvcfs"


rule gatk_select_snps:
    input:
        ref="data/genome.fa",
        fai="data/genome.fa.fai",
        dict="data/genome.dict",
        vcf=rules.gatk_genotypegvcfs.output.vcf,
    output:
        vcf=report(
            "calls/gatk/snps.vcf.gz",
            caption="report/gatk-snps.rst",
            category="GATK variant calls",
        ),
    log:
        "logs/gatk/select_snps.log",
    params:
        extra="--select-type-to-include SNP",
        java_opts="",
    resources:
        mem_mb=1024,
    wrapper:
        "v3.1.0/bio/gatk/selectvariants"
