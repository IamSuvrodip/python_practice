# Coffee Customization

order_size = (input("What you like to order Small/Medium/large= ").lower())
extra_shot = (input("Are you want to extra_shot(Yes/No)= ").lower())


if extra_shot == 'yes':
    print(f"Order: This is your {order_size} coffee with extra shot..")
else:
    print(f"Order: This is your {order_size} coffee without extra shot..")