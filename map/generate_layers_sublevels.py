from PIL import Image
import os
import sys
import math

# ---------------------------------------------------------------------------- #

if len(sys.argv) < 2:
    print('Missing arguments. Use as such:')
    print('    python generate_sublevels.py {sublayer count} {start layer}')
    quit()

sublayer_count   = int(sys.argv[1])
start_layer      = sys.argv[2]
source_files     = len(os.listdir(start_layer + '_source/'))
source_files_arr = os.listdir(start_layer + '_source/')

# ---------------------------------------------------------------------------- #

def get_power(x, size):
    if x == 0:
        return int(size)
    elif x == 1:
        return int(size)/2
    else:
        #print(size, pow(2, x))
        return int(size)/pow(2, x)

def get_cuts(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    else:
        return pow(2, x)

def rename_file(source, rc, source_dir, offset_r = 0, offset_c = 0):
    if(source.split('-')[1] == 'a.png'):
        rc = rc/math.sqrt(source_files)
        id = int(source[slice(-0, -6)])
        row = id % int(rc) + offset_r
        column = int(id / int(rc)) + offset_c

        out_string = str(row) + '-' + str(column) + '.png'
        
        os.rename(source_dir + source, source_dir + out_string)
        print('│    Renamed ' + str(source_dir) + str(source) + ' to ' + out_string)
    
def rename_folder_content(folder_dir, rc, offset_r = 0, offset_c = 0):
    file_array = os.listdir(folder_dir)
    print('╭─Renaming files in ' + str(folder_dir))
    for x in file_array:
        rename_file(x, rc, folder_dir, offset_r, offset_c)
    print('╰─Renamed all files in', folder_dir, 'with row/columng offset', offset_r, offset_c)

# ---------------------------------------------------------------------------- #

print(' ')
print(' ─Source files total:', str(source_files))

# Set-up variables
image_size = Image.open(start_layer + '_source/' + '/0-0.png').size[0]

#############
#   SETUP   #
#############
for x in range(sublayer_count):
    # Set-up variables
    working_layer = int(start_layer) + x
    tile_cut_size = str(int(get_power(working_layer - 1, image_size)))

    source_row    = 0
    source_column = 0

    # Re-create folders
    os.system('rm -rf ' + str(working_layer) + '/')
    print('╭─Removed old ' + str(working_layer) + '/')
    os.system('mkdir ' + str(working_layer))
    print('╰─Made folder ' + str(working_layer) + '/')


# for x in range(source_files):
#     # Set-up source_row/column
#     source_row     = int(source_files_arr[x].split('-')[0])
#     source_columng = int(source_files_arr[x].split('-')[1].split('.')[0])
#     print('### Working on', source_row, source_columng, '###')

#     for x in range(sublayer_count):
#         # Set-up variables
#         working_layer = int(start_layer) + x
#         tile_cut_size = str(int(get_power(working_layer - 1, image_size)))

#         # Slice image
#         print('╭─Slicing ' + str(start_layer) + '_source/' + str(source_column) + '-' + str(source_row) + '.png into pieces of ' + tile_cut_size)
#         os.system('convert ' + str(start_layer) + '_source/' + str(source_column) + '-' + str(source_row) + '.png -crop ' + tile_cut_size + 'x' + tile_cut_size + ' -resize 256x256\> ' + str(working_layer) + '/%d-a.png')
#         print('╰─Sliced!')

#         # Rename files
#         rename_folder_content(str(working_layer)+'/', get_cuts(working_layer), pow(2, working_layer-1)*source_row, pow(2, working_layer-1)*source_column)

for y in range(source_files):
    print(' ')
    # Set-up source_row/column
    source_row    = int(source_files_arr[y].split('-')[0])
    source_column = int(source_files_arr[y].split('-')[1].split('.')[0])
    print('### Working on', source_row, source_column, '-', source_files_arr[y], '###')

    for x in range(sublayer_count):
        # Set-up variables
        working_layer = int(start_layer) + x
        tile_cut_size = str(int(get_power(working_layer - 1, image_size)))

        # Slice image
        print('╭─Slicing ' + str(start_layer) + '_source/' + str(source_column) + '-' + str(source_row) + '.png into pieces of ' + tile_cut_size)
        os.system('convert ' + str(start_layer) + '_source/' + str(source_column) + '-' + str(source_row) + '.png -crop ' + tile_cut_size + 'x' + tile_cut_size + ' -resize 256x256\> ' + str(working_layer) + '/%d-a.png')
        print('╰─Sliced!')

        # Rename files
        rename_folder_content(str(working_layer)+'/', get_cuts(working_layer), pow(2, working_layer-1)*source_column, pow(2, working_layer-1)*source_row)

# for x in range(sublayer_count):
#     # Set-up variables
#     working_layer = int(start_layer) + x
#     tile_cut_size = str(int(get_power(working_layer - 1, image_size)))

#     # Slice image
#     print('╭─Slicing ' + str(start_layer) + '_source/0-0.png into pieces of ' + tile_cut_size)
#     os.system('convert ' + str(start_layer) + '_source/0-0.png -crop ' + tile_cut_size + 'x' + tile_cut_size + ' -resize 256x256\> ' + str(working_layer) + '/%d-a.png')
#     print('╰─Sliced!')

#     # Rename files
#     rename_folder_content(str(working_layer)+'/', get_cuts(working_layer), pow(2, working_layer-1)*source_column, pow(2, working_layer-1)*source_row)

# for x in range(sublayer_count):
#     # Set-up variables
#     working_layer = int(start_layer) + x
#     tile_cut_size = str(int(get_power(working_layer - 1, image_size)))

#     # Slice image
#     print('╭─Slicing ' + str(start_layer) + '_source/0-1.png into pieces of ' + tile_cut_size)
#     os.system('convert ' + str(start_layer) + '_source/0-1.png -crop ' + tile_cut_size + 'x' + tile_cut_size + ' -resize 256x256\> ' + str(working_layer) + '/%d-a.png')
#     print('╰─Sliced!')

#     # Rename files
#     rename_folder_content(str(working_layer)+'/', get_cuts(working_layer), pow(2, working_layer-1)*source_column, pow(2, working_layer-1)*source_row)


