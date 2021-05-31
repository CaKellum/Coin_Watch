from .main import data_manager as dm
from .main import figure_trend as ft


def main():
    dm.update()
    ft.decide()


if __name__ == '__main__':
    main()
