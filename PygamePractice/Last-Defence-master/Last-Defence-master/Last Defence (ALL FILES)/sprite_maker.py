import pygame

WHITE = (255, 255, 255)

class Ship(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("Spaceship-1.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        if self.rect.x <= 624:
            self.rect.x += pixels

    def moveLeft(self, pixels):
        if self.rect.x >= 0:
            self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

class Asteroid(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("asteroid.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        if self.rect.x <= 624:
            self.rect.x += pixels

    def moveLeft(self, pixels):
        if self.rect.x >= 0:
            self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

class Star(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("stars.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        if self.rect.x <= 624:
            self.rect.x += pixels

    def moveLeft(self, pixels):
        if self.rect.x >= 0:
            self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

class Beam(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("beam.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -101 and self.rect.y <= 600:
            self.rect.y -= speed

class Big_Beam(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("big_beam.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -301 and self.rect.y <= 600:
            self.rect.y -= speed

class Gold_Beam(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("beam-S.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -101 and self.rect.y <= 600:
            self.rect.y -= speed

class Big_Gold_Beam(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("big_beam-S.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -301 and self.rect.y <= 600:
            self.rect.y -= speed

class Dist_Beam(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("beam-D.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -101 and self.rect.y <= 600:
            self.rect.y -= speed

class Big_Dist_Beam(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("big_beam-D.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -301 and self.rect.y <= 600:
            self.rect.y -= speed

class Torpidorito(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("Torpidorito.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveForward(self, speed):
        if self.rect.y >= -101 and self.rect.y <= 600:
            self.rect.y -= speed

class LilFlame(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("burning fuel (small).png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveBackward(self, speed):
        self.rect.y += (2 + (speed * 2))

class Flame(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("burning fuel.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moveBackward(self, speed):
        self.rect.y += (2 + (speed * 2))
