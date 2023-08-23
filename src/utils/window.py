import pygetwindow


def get_window():
    # sw = pygetwindow.getWindowsWithTitle('超能世界')


    print(pygetwindow.getAllTitles())
    print(pygetwindow.getAllWindows())
    print(pygetwindow.getActiveWindow().title)
    # print(pygetwindow.getWindowsWithTitle('超能世界')[0])
    # print(pygetwindow.getWindowsWithTitle('超能世界')[1])


if __name__ == "__main__":
    get_window()