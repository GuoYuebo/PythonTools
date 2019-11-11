# batch_file_rename_extension.py
# Created: 2019-11-11

"""
批量修改某个文件夹下同一扩展名文件的扩展名到另一个扩展名
"""

__author__ = 'GuoYuebo'
__version__ = '1.0'

import argparse
import os


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        if split_file[1] == old_ext:
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, split_file[0] + new_ext))
    print('rename is done.')
    print(os.listdir(work_dir))


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():
    args = vars(get_parser().parse_args())
    batch_rename(args['work_dir'][0], args['old_ext'][0], args['new_ext'][0])


if __name__ == '__main__':
    main()
