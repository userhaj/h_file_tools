def join_file(first_file):
    """Quickly join files split with .001 extension.
    Resulting file will be in same folder without '.001' extension"""
    first_file_no_numbers = first_file[:-3]  # Remove 001 from file name
    output_file_name = first_file[:-4]  # Remove .001 from file name
    file_number = 1  # Create counter starting at 1

    with open(output_file_name, 'wb') as output_file:  # Output file loop
        while True:  # For ever loop
            try:
                # Open file by pasting 3digit number as extension
                with open(first_file_no_numbers + ('%03d' % file_number), 'rb') as current_input:
                    # Read the whole file and write it to output file. (Maybe dangerous if file size > memory)
                    output_file.write(current_input.read())
                    # Go on to the next file
                    file_number += 1
            except FileNotFoundError:
                # End loop when no more 3digit extension files are found
                break
