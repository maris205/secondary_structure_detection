def read_fasta(filename):
    """Read fasta data from the given file.  Returns a two-element list,
       the first of which is the fasta information (the first line), the
       rest of which is the sequence, represented as a string."""
    infile = open(filename)
    info = infile.readline()
    data = infile.read()
    infile.close()
    info = info.replace('\n', '')
    data = data.replace('\n', '')
    info = info.replace('\r', '')	# I hate DOS
    data = data.replace('\r', '')	# I hate DOS
    return [info,data]
