import data_manager as dm
import figure_trend as ft
import email


def main():
    result = dm.get_data()
    if result == -1:
        email.send_custom("coin_tracker now online")
    else: 
        desicion = ft.decide(result)
        if(desicion['thought'] == 'sell'):
            email.send_sell(desicion['price'])
            dm.write_new(desicion)
        else:
            dm.write_new(desicion)


if __name__ == '__main__':
    main()
