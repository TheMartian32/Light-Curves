"""
A script to plot the light of a star.
"""
import os
from Proxima.usr_inputs import UI_Inputs
import matplotlib.pyplot as plt
import numpy as np

ask = UI_Inputs()


def main():

    # TODO: Use ask.ask_for() for asking the user how many observations they have
    # TODO: Find a way to grab the current date and time without having to format it

    # * Number of observations the observer wants to record
    num_obsv = ask.ask_for(
        'How many observations would you like to record?: ', 'Error.', int)
    mag_array = []
    time_array = []

    for i in range(int(num_obsv)):
        # * Magnitude
        est_mag = ask.ask_for('\nEstimated magnitude: ', '\nError.', float)
        mag_array.append(int(est_mag))

        # * Times
        try:
            time = ask.ask_for('\nTime of observation: ', 'Error.', str)
            time_array.append(time)
        except:
            print('\nError.')

    y = np.array(mag_array)
    x = np.array(time_array)

    plt.ylabel('Estimated magnitude.')
    plt.xlabel('Time')
    curve = plt.plot(x, y, 'ro')

    # * Saving plot
    save_plot = ask.ask_for(
        '\nWould you like to save the plot? (Y/N): ', 'Error.', str).lower()
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

            print('\nThis directory or file already exists.')
            print('However, you can still save it in that directory.')
            # * Asks for the file name the user wants
            file_name = ask.ask_for(
                '\nFile name (File extension is .png): ', 'Error.', str)

            # * Saving the figure to the desired  path and name.
            plt.savefig(f'{path}/{file_name}.png', bbox_inches='tight')

        except FileNotFoundError:
            print("File wasn't found.")

    # * Case if the user doesn't want to save the plot
    elif save_plot == 'n':
        print('\nSounds good.')

    return curve, plt.show()


if __name__ == "__main__":
    main()
