from pathlib import Path

import task_1 as t1
import task_2 as t2
import task_3 as t3
import task_4 as t4
import mass_renaming as mr



if __name__ == '__main__':
    # t1.fill_numbers(3, 'gen_bumbers.txt')
    # t2.gen_names(10, 4, 7, Path('gen_names.txt'))
    # t3.combine_files('gen_bumbers.txt', 'gen_names.txt', 'combine_files.txt')
    # t4.gen_files(extension='bin', count_files=3)
    mr.rename_file(origin_extension='.txt')
    mr.rename_file(origin_extension='.bin', target_extension='.bin', range_of_name=(0, 2))

