#! /usr/bin/env python3
'''
Implementation of the "Rooting" module using FastRoot to MinVar-root
'''
from Rooting import Rooting
import ViReport_GlobalContext as GC
from os import makedirs
from os.path import isfile
from subprocess import check_output

class Rooting_MinVar(Rooting):
    def init():
        pass

    def finalize():
        pass

    def cite():
        return GC.CITATION_MINVAR

    def blurb():
        return "The inferred phylogeny was MinVar-rooted using FastRoot (Mai et al., 2017)."

    def root(tree_filename):
        if not isfile(tree_filename):
            raise ValueError("Invalid tree file: %s" % tree_filename)
        fastroot_dir = '%s/FastRoot' % GC.OUT_DIR_TMPFILES
        out_filename = '%s/rooted.tre' % GC.OUT_DIR_OUTFILES
        if isfile(out_filename):
            GC.SELECTED['Logging'].writeln("Rooted phylogeny exists. Skipping recomputation.")
        else:
            makedirs(fastroot_dir, exist_ok=True)
            command = ['FastRoot.py', '-i', tree_filename, '-m', 'MV']
            f = open('%s/command.txt' % fastroot_dir, 'w'); f.write('%s\n' % ' '.join(command)); f.close()
            o = check_output(command).decode().replace("'",'').strip()
            f = open(out_filename, 'w'); f.write('%s\n' % o); f.close()
        return out_filename
