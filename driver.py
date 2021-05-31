from .main import data_manager as dm
from .main import figure_trend as ft
from .main import manage_email as me


def main():
    result = dm.get_data()
    if result == -1:
        me.send_custom("coin_tracker now online")
    else: 
        desicion = ft.decide(result)
        if(desicion['thought'] == 'sell'):
            me.send_sell(desicion['price'])
            dm.write_new(desicion)
        else:
            dm.write_new(desicion)


if __name__ == '__main__':
    main()
