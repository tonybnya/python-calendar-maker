#!/usr/bin/env python3

"""
Project name:   Calendar Maker
Author:         tonybnya <nya.tony2010@gmail.com>
Purpose:        The program generates text files of calendar
                for the month and the year entered.
"""

import sys
import datetime
from colorama import Back, Fore, Style
import colorama

colorama.init(autoreset=True)

# Define constants.
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')


def usage():
    """
    Function to define the manual for the script.
    """

    with open('./usage.txt') as file_obj:
        contents = file_obj.read()

    return contents


def main():
    """Main program."""

    # Options for the command line.
    if len(sys.argv) != 3:
        print(usage())
        sys.exit()
    else:
        args = sys.argv[1:]

        # Get the year from the prompt shell.
        while True:
            if args[0].isdecimal() and int(args[0]) > 0:
                year = int(args[0])
                break

            print(usage())
            sys.exit()

        # Get the month from the prompt shell.
        while True:
            args = sys.argv[1:]
            if args[1].isdecimal() and 1 <= int(args[1]) <= 12:
                month = int(args[1])
                break

            print(usage())
            sys.exit()

    print(f"{Style.BRIGHT}{Fore.CYAN}\n{' ' * 20}-+-+-+\t+ CALENDAR MAKER +\t+-+-+-\n")

    calendar_text = get_calendar(year, month)
    # Display the calendar.
    print(calendar_text)

    # Save the calendar to a text file.
    calendar_file = f"calendar_{year}_{month}.txt"
    with open(calendar_file, 'w') as file_obj:
        file_obj.write(calendar_text)

    print('Saved to ' + calendar_file)


def get_calendar(year, month):
    """
    This function returns a multiline string for
    the given month and year.
    """

    # `calendar_text` will contain the string for the calendar.
    calendar_text = ''

    # Put at the top of the calendar the given month and year.
    # In an iterable, index begin by 0.
    # So, `month-1` is to get the right month in `MONTHS`.
    calendar_text += (' ' * 34) + Style.BRIGHT + Back.GREEN + Fore.BLACK + \
        ' ' + MONTHS[month - 1] + ' ' + str(year) + ' ' + Back.RESET + '\n'

    # Add labels for days.
    calendar_text += f"{Style.BRIGHT}{Fore.YELLOW}\n.....SUN........MON........TUE........WED........THU........FRI........SAT....\n"

    # Define a line to separate different weeks.
    line = ('+----------' * 7) + '+\n'
    # Define blanks to separate days.
    blank = ('|          ' * 7) + '|\n'

    # Define a variable for the first date of the given month.
    current_day = datetime.date(year, month, 1)
    # We have to roll back `current_day` until Sunday.
    # `weekday()` function returns 6 for Sunday.
    while current_day.weekday() != 6:
        current_day -= datetime.timedelta(days=1)

    # Loop over each week.
    while True:
        calendar_text += line

        # `day_row` is the row with a day.
        day_row = ''
        for i in range(7):
            # `string.rjust(length, char)`: method to right align
            # `string`, using `char` by the length `length`
            # length is required, `char` is optional (default space)
            day_label = str(current_day.day).rjust(2)
            day_row += '|' + day_label + (' ' * 8)
            # Go to the next day.
            current_day += datetime.timedelta(days=1)
        # Add a vertical line after the last day, Saturday.
        day_row += '|\n'

        # Add the day row and 3 blank rows to `calendar_text`.
        calendar_text += day_row
        for i in range(3):
            calendar_text += blank

        # Check if we're done with the month.
        if current_day.month != month:
            break

    # Add the horizontal line at the bottom of the calendar_text.
    calendar_text += line

    return calendar_text


if __name__ == '__main__':
    main()
