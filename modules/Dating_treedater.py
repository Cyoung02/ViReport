#! /usr/bin/env python3
'''
Implementation of the "Dating" module using treedater
'''
from Dating import Dating
import ViReport_GlobalContext as GC
from glob import glob
from os import makedirs
from os.path import isfile
from shutil import move
from subprocess import call

class Dating_treedater(Dating):
    def init():
        pass

    def finalize():
        pass

    def cite():
        return GC.CITATION_TREEDATER

    def date(rooted_tree_filename, sample_times_filename):
        if not isfile(rooted_tree_filename):
            raise ValueError("Invalid tree file: %s" % rooted_tree_filename)
        if not isfile(sample_times_filename):
            raise ValueError("Invalid sample times file: %s" % sample_times_filename)
        treedater_dir = '%s/treedater' % GC.OUT_DIR_TMPFILES
        makedirs(treedater_dir, exist_ok=True)
        out_filename = '%s/dated.tre' % GC.OUT_DIR_OUTFILES
        log_file = open('%s/log.txt' % treedater_dir, 'w')
        treedater_times_filename = '%s/times_treedater.txt' % treedater_dir
        f = open(treedater_times_filename, 'w'); f.write(GC.convert_dates_treedater(sample_times_filename)); f.close()
        aln_length = len(''.join(open(GC.ALIGNMENT).read().split('>')[1].splitlines()[1:]))
        command = ['tdcl', '-t', rooted_tree_filename, '-s', treedater_times_filename, '-l', str(aln_length), '-o', out_filename]
        f = open('%s/command.txt' % treedater_dir, 'w'); f.write('%s\n' % ' '.join(command)); f.close()
        call(command, stdout=log_file)
        log_file.close()
        return out_filename