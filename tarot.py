import pygame, sys, random

# Define colors
PURPLE = (128, 0, 128)
GREEN = (0, 128, 0)

class Card:
    def __init__(self, name):
        self.name = name
        self.flipped = False
        self.color = PURPLE
        self.x = 0  # Initial x position (top-left corner)
        self.y = 0  # Initial y position (top-left corner)
        self.target_x = 0
        self.target_y = 0
        self.moving = False
        self.font = pygame.font.Font(None, 20)
        self.click_count = 0

    def click(self):
        self.click_count += 1
        if self.click_count == 2:
            self.flip()
            self.click_count = 0

    def flip(self):
        self.flipped = not self.flipped
        if self.flipped:
            self.color = GREEN

    def draw(self, surface, width, height):
        pygame.draw.rect(surface, self.color, (self.x, self.y, width, height))
        if not self.flipped:
            pygame.draw.rect(surface, self.color, (self.x, self.y, width, height))
        else:
            text = self.font.render(self.name, True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.x + width / 2, self.y + height / 2))
            surface.blit(text, text_rect)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def move(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
        self.moving = True

    def update(self):
        if self.moving:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            dist = pygame.math.Vector2(dx, dy).length()
            if dist > 2:
                speed = 2
                direction = pygame.math.Vector2(dx, dy).normalize()
                self.x += direction.x * speed
                self.y += direction.y * speed
            else:
                self.x = self.target_x
                self.y = self.target_y
                self.moving = False

# Initialize Pygame
pygame.init()

# Set the window size
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# Create 10 cards
card_width, card_height = 100, 150
card_names = [
    'The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor','The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune','Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star','The Moon', 'The Sun', 'Judgment', 'The World','Ace of Wands', 'Two of Wands', 'Three of Wands', 'Four of Wands', 'Five of Wands','Six of Wands', 'Seven of Wands', 'Eight of Wands', 'Nine of Wands', 'Ten of Wands','Ace of Cups', 'Two of Cups', 'Three of Cups', 'Four of Cups', 'Five of Cups','Six of Cups', 'Seven of Cups', 'Eight of Cups', 'Nine of Cups', 'Ten of Cups','Ace of Swords', 'Two of Swords', 'Three of Swords', 'Four of Swords', 'Five of Swords','Six of Swords', 'Seven of Swords', 'Eight of Swords', 'Nine of Swords', 'Ten of Swords','Ace of Pentacles', 'Two of Pentacles', 'Three of Pentacles', 'Four of Pentacles', 'Five of Pentacles','Six of Pentacles', 'Seven of Pentacles', 'Eight of Pentacles', 'Nine of Pentacles', 'Ten of Pentacles'
]
random.shuffle(card_names)
cards = [Card(name) for name in card_names]

# Position of the first card
start_x, start_y = 0, 0


# Main game loop
running = True
card_index = 0
target_positions = [(100-(card_width/2), (width - card_width) // 2), (300-(card_width/2), (width - card_width) // 2), (500-(card_width/2), (width - card_width) // 2)]
current_target_index = 0
clicked_cards = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and card_index < len(cards):
            clicked_card = None  # To keep track of which card was clicked

            # Check if the mouse click is within the bounds of any card
            for i, card in enumerate(cards):
                if not card.flipped and not card.moving:
                    if card.x <= event.pos[0] <= card.x + card_width and card.y <= event.pos[1] <= card.y + card_height:
                        clicked_card = card
                        break

            if clicked_card is not None and clicked_card not in clicked_cards:
                if not clicked_card.flipped:  # Check if the clicked card is unflipped
                    clicked_card.click()
                    target_x, target_y = target_positions[current_target_index]
                    clicked_card.move(target_x, target_y)
                    card_index += 0.5
                    current_target_index = (current_target_index + 1) % len(target_positions)  # Move to the next target position
                    clicked_cards.append(clicked_card)
            else:
                clicked_card.click()
                card_index += 0.5

    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # White background

    # Update card positions
    for card in cards:
        card.update()

    # Draw the cards
    for card in cards:
        card.draw(screen, card_width, card_height)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
