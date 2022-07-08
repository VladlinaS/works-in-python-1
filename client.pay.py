service_price       = 100

client_cash_amount  = int(input('Enter cash amount:'))


if client_cash_amount >= service_price:
    print('CASH PAYMENT SUCCESS!!!')
else:
    print('CASH PAYMENT FAILURE!!!')

    client_card_amount  = int(input('Enter cars amount:'))
    if client_card_amount >= service_price:
        print('CARD PAYMENT SUCCESS!!!')
    else:
        print('CARD PAYMENT FAILURE!!!')

        client_card_crypto  = int(input('Enter crypto amount:'))
        if client_card_crypto >= service_price:
            print('CRYPTO PAYMENT SUCCESS!!!')
        else:
            print('CRYPTO PAYMENT FAILURE!!!')