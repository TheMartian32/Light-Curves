"""
A script to plot the light of a star.
"""

import os
from Proxima.usr_inputs import UI_Inputs
import matplotlib.pyplot as plt
import numpy as np

ask = UI_Inputs()


def main():
    """

    This is the function that does it all.
    It basically plots the data, saves files to the given directories,
    records the data, and hopefully soon enough can persist that data
    so you can keep recording observations for that star/objects and see
    how it goes over time.

    Returns:
        Plot: Returns a plot
    """

    # TODO: Use ask.ask_for() for asking the user how many observations they have
    # TODO: Find a way to grab the current date and time without having to format it

    # * Number of observations the observer wants to record
    num_obsv = ask.ask_for(
        '\nHow many observations would you like to record?: ', 'Error.', int)
    mag_array = []
    time_array = []

    print('\n*------------------------------------------------*')

    for _ in range(int(num_obsv)):
        # * Magnitude
        est_mag = ask.ask_for('Estimated magnitude: ', '\nError.', float)
        mag_array.append(int(est_mag))

        # * Times
        try:
            time = ask.ask_for('\nTime of observation (24 hour time): ', 'Error.', str)
            time_array.append(time)
        except:
            print('\nError.')

    print('*------------------------------------------------*')

    y = np.array(mag_array)
    x = np.array(time_array)

    plt.ylabel('Estimated magnitude.')
    plt.xlabel('Time')
    curve = plt.plot(x, y, 'ro')

    # * Saving plot
    print('\n*------------------------------------------------*')
    save_plot = ask.ask_for(
        'Would you like to save the plot? (Y/N): ', 'Error.', str).lower()
    if save_plot == 'y':

        path = ask.ask_for('\nPlease provide a file path: ', 'Error.', str)
        try:
            # * Tries to make the directory at the path the user provided.
            os.mkdir(path)

            # * File name for the soon to be saved file.
            file_name = ask.ask_for(
                '\nFile name (File extension is .png): ', 'Error.', str)
            plt.savefig(f'{path}/{file_name}.png', bbox_inches='tight')

        # * Exception if the file exists
        # TODO: Find a way to save the file to the same directory without bringing up this error
        except FileExistsError:
            print('\n*------------------------------------------------*')
            print('This directory or file already exists.')
            print('However, you can still save it in that directory.')
            # * Asks for the file name the user wants
            file_name = ask.ask_for(
                '\nFile name (File extension is .png): ', 'Error.', str)
            print('*------------------------------------------------*')

            # * Saving the figure to the desired  path and name.
            plt.savefig(f'{path}/{file_name}.png', bbox_inches='tight')

        except FileNotFoundError:
            print("\nFile wasn't found.")

    # * Case if the user doesn't want to save the plot
    elif save_plot == 'n':
        print('\nSounds good.')
    print('*------------------------------------------------*')

    return curve, plt.show()


if __name__ == "__main__":
    main()
    # * Executes at the end to see if the user wants to repeat the program.
    repeat = ''
    while True:

        # * Asks to repeat the script.
        print(
            '\nTyping Y will restart the script, typing N will terminate it.')

        repeat = input(
            '\n: ').lower()

        if repeat[0] == 'y':
            main()
            continue

        if repeat[0] == 'n':
            break