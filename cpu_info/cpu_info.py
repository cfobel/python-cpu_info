import re
from subprocess import check_output
from collections import OrderedDict


def cpu_info():
    data = check_output(['/bin/cat', '/proc/cpuinfo'])
    processor_section_matches = [m
            for m in re.finditer(r'^processor.*:', data, re.MULTILINE)]
    p = processor_section_matches
    processor_section_ranges = [(p[i].start(), p[i + 1].start())
            for i in range(len(p) - 1)] + [(p[-1].start(), -1)]
    processor_sections = [data[r[0]:r[1]] for r in processor_section_ranges]
    processor_infos = OrderedDict()
    for s in processor_sections:
        cpu_info = OrderedDict([map(str.strip, line.split(':')) for line in s.splitlines() if line.strip()])
        processor_infos[cpu_info['processor']] = cpu_info
    return processor_infos


def cpu_summary(keys=None):
    if keys is None:
        keys = ['model name', 'cpu MHz', 'cache size', 'bogomips']
    info = cpu_info()
    format_str = '%%%ds: %%s' % (max([len(k) for k in keys]) + 2)
    message = '\n'.join([format_str % item
            for item in [(k.title(), info['0'][k]) for k in keys]])
    return message
