#! /usr/bin/env python3
'''
Implementation of the "Preprocessing" module where sequences are given safe names (non-letters/digits --> underscore)
'''
from Preprocessing import Preprocessing
import ViReport_GlobalContext as GC
from os.path import isfile

class Preprocessing_SafeNames(Preprocessing):
    def init():
        pass

    def finalize():
        pass

    def cite():
        return GC.CITATION_VIREPORT

    def blurb():
        return "The input dataset was preprocessed such that sequences were given safe names: non-letters/digits in sequence IDs were converted to underscores."

    def preprocess(seqs_filename, ref_id, sample_times_filename, outgroups_filename, categories_filename):
        # set things up
        if not isfile(seqs_filename):
            raise ValueError("Invalid sequence file: %s" % seqs_filename)
        if not isfile(sample_times_filename):
            raise ValueError("Invalid sample times file: %s" % sample_times_filename)
        out_seqs_filename = '%s/sequences_safe.fas' % GC.OUT_DIR_OUTFILES
        out_times_filename = '%s/times_safe.txt' % GC.OUT_DIR_OUTFILES
        if outgroups_filename is None:
            out_outgroups_filename = None
        else:
            if not isfile(outgroups_filename):
                raise ValueError("Invalid outgroups list file: %s" % outgroups_filename)
            out_outgroups_filename = '%s/outgroups_safe.txt' % GC.OUT_DIR_OUTFILES
        if categories_filename is None:
            out_categories_filename is None
        else:
            if not isfile(categories_filename):
                raise ValueError("Invalid sample categories file: %s" % categories_filename)
            out_categories_filename = '%s/categories_safe.txt' % GC.OUT_DIR_OUTFILES

        # output safe sequences
        if isfile(out_seqs_filename):
            GC.SELECTED['Logging'].writeln("Safename sequences exist. Skipping recomputation.")
        else:
            f = open(out_seqs_filename, 'w')
            for line in open(seqs_filename):
                l = line.strip()
                if len(l) == 0:
                    continue
                elif l[0] == '>':
                    f.write('>'); f.write(GC.safe(l[1:]))
                else:
                    f.write(l)
                f.write('\n')
            f.close()
        if ref_id is None:
            out_ref_id = None
        else:
            out_ref_id = GC.safe(ref_id)

        # output safe sample times
        if isfile(out_times_filename):
            GC.SELECTED['Logging'].writeln("Safename sample times exist. Skipping recomputation.")
        else:
            f = open(out_times_filename, 'w')
            for line in open(sample_times_filename):
                parts = [v.strip() for v in line.strip().split('\t')]
                if len(parts) == 2:
                    f.write(GC.safe(parts[0])); f.write('\t'); f.write(parts[1]); f.write('\n')
                else:
                    raise ValueError("Invalid sample times file: %s" % sample_times_filename)
            f.close()

        # output safe outgroup names
        if outgroups_filename is not None:
            if isfile(out_outgroups_filename):
                GC.SELECTED['Logging'].writeln("Safename outgroups exist. Skipping recomputation.")
            else:
                f = open(out_outgroups_filename, 'w')
                for line in open(outgroups_filename):
                    f.write(GC.safe(line.strip())); f.write('\n')
                f.close()

        # output safe categories
        if categories_filename is not None:
            if isfile(out_categories_filename):
                GC.SELECTED['Logging'].writeln("Safename sample categories exist. Skipping recomputation.")
            else:
                f = open(out_categories_filename, 'w')
                for line in open(categories_filename):
                    parts = [v.strip() for v in line.strip().split('\t')]
                    if len(parts) == 2:
                        f.write(GC.safe(parts[0])); f.write('\t'); f.write(parts[1]); f.write('\n')
                    else:
                        raise ValueError("Invalid sample categories file: %s" % categories_filename)
                f.close()

        # return output filenames
        return out_seqs_filename, out_ref_id, out_times_filename, out_outgroups_filename, out_categories_filename
