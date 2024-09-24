import random

def draw_card(value, suit):
    suits_symbols = {
        'hearts': '♥',
        'diamonds': '♦',
        'clubs': '♣',
        'spades': '♠'
    }
    
    card = [
        "┌─────────┐",
        f"│{value:<2}       │",
        "│         │",
        "│         │",
        f"│    {suits_symbols[suit]}    │",
        "│         │",
        "│         │",
        f"│       {value:>2}│",
        "└─────────┘"
    ]
    
    return "\n".join(card)

def calculate_hand_score(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    score = 0
    num_aces = 0
    for card in hand:
        rank, _ = card  # Desempacotar o valor e o naipe
        score += values[rank]
        if rank == 'ace':
            num_aces += 1
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def display_hand(hand, title):
    print(title)
    card_lines = [[] for _ in range(9)]  # Lista para armazenar as linhas de cada carta

    for card in hand:
        card_ascii = draw_card(card[0], card[1]).split('\n')
        for i in range(9):
            card_lines[i].append(card_ascii[i])
    
    for line in card_lines:
        print('         '.join(line))  # Imprimir todas as linhas das cartas lado a lado

def new_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def blackjack():
    deck = new_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        display_hand(player_hand, "Sua Mão:")
        print(f"Sua Pontuação: {calculate_hand_score(player_hand)}")
        
        if calculate_hand_score(player_hand) > 21:
            print("Que pena! Você perdeu!")
            break
        
        action = input("Você quer 'Comprar' ou 'Passar'? (Digite 0 ou 1)\n").strip().lower()
        
        if action == '0':
            player_hand.append(deck.pop())
        elif action == '1':
            break
        else:
            print("Ação inválida, por favor, digite '0' ou '1'")
    
    if calculate_hand_score(player_hand) <= 21:
        while calculate_hand_score(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        
        display_hand(dealer_hand, "Mão da Banca:")
        dealer_score = calculate_hand_score(dealer_hand)
        player_score = calculate_hand_score(player_hand)
        
        print(f"Pontuação da Banca: {dealer_score}")
        print(f"Sua Pontuação: {player_score}")
        
        if dealer_score > 21:
            print("Parabéns! Você Venceu!")
        elif dealer_score > player_score:
            print("Banca Ganhou!")
        elif dealer_score < player_score:
            print("Você Venceu!")
        else:
            print("Empate!")

if __name__ == "__main__":
    blackjack() 