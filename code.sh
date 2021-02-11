fastqc -t 32 -o fastqc ..*gz

quast.py -t 32 -s ../hg19.fasta

bwa mem -t 30 -M -R "@RG\tID:510-7-BRCA\tLB:PairedEnd\tPL:Illumina\tPU:000000000-A442D\tSM:510-7-BRCA" ../reference/hg19.fasta ../raw_data/510-7-BRCA_S8_L001_R1_001.fastq.gz ../raw_data/510-7-BRCA_S8_L001_R2_001.fastq.gz > 510-7-BRCA.sam

samtools view -bT ../reference/hg19.fasta 510-7-BRCA.sam > 510-7-BRCA.bam

samtools sort 510-7-BRCA.bam > 510-7-BRCA_sorted.bam

/home/labbe-x/labbex/Programas/freebayes/bin/freebayes --target ../reference/BRCA.bed --bam 510-7-BRCA_sorted.bam --ploidy 2 --fasta-reference ../reference/hg19.fasta --vcf 510-7-BRCA.vcf

samtools view 510-7-BRCA_sorted.bam "chr17:41197694-41197819" > chr17.bam

samtools view -c -f 77 510-7-BRCA_sorted.bam

java -jar $/snpEff.jar hg19 510-7-BRCA.vcf > 510-7-BRCA.vcf.ann